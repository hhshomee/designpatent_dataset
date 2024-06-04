import pandas as pd
import os
import requests
from PIL import Image
from io import BytesIO
from llava.conversation import conv_templates, SeparatorStyle
from llava.utils import disable_torch_init
from llava.constants import IMAGE_TOKEN_INDEX, DEFAULT_IMAGE_TOKEN, DEFAULT_IM_START_TOKEN, DEFAULT_IM_END_TOKEN
from llava.mm_utils import tokenizer_image_token, get_model_name_from_path, KeywordsStoppingCriteria
from transformers import TextStreamer


from transformers import AutoTokenizer, BitsAndBytesConfig
from llava.model import LlavaLlamaForCausalLM
import torch

model_path = "4bit/llava-v1.5-13b-3GB"
kwargs = {"device_map": "auto"}
kwargs['load_in_4bit'] = True
kwargs['quantization_config'] = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_use_double_quant=True,
    bnb_4bit_quant_type='nf4'
)
model = LlavaLlamaForCausalLM.from_pretrained(model_path, low_cpu_mem_usage=True, **kwargs)
tokenizer = AutoTokenizer.from_pretrained(model_path, use_fast=False)


vision_tower = model.get_vision_tower()

if not vision_tower.is_loaded:
    vision_tower.load_model()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
vision_tower.to(device)

image_processor = vision_tower.image_processor


def caption_image(image_file, prompt):
    if image_file.startswith('http') or image_file.startswith('https'):
        response = requests.get(image_file)
        image = Image.open(BytesIO(response.content)).convert('RGB')
    else:
        image = Image.open(image_file).convert('RGB')
    disable_torch_init()
    conv_mode = "llava_v0"
    conv = conv_templates[conv_mode].copy()
    roles = conv.roles
    image_tensor = image_processor.preprocess(image, return_tensors='pt')['pixel_values'].half().cuda()
    inp = f"{roles[0]}: {prompt}"
    inp = DEFAULT_IM_START_TOKEN + DEFAULT_IMAGE_TOKEN + DEFAULT_IM_END_TOKEN + '\n' + inp
    conv.append_message(conv.roles[0], inp)
    conv.append_message(conv.roles[1], None)
    raw_prompt = conv.get_prompt()
    input_ids = tokenizer_image_token(raw_prompt, tokenizer, IMAGE_TOKEN_INDEX, return_tensors='pt').unsqueeze(0).cuda()
    stop_str = conv.sep if conv.sep_style != SeparatorStyle.TWO else conv.sep2
    keywords = [stop_str]
    stopping_criteria = KeywordsStoppingCriteria(keywords, tokenizer, input_ids)
    with torch.inference_mode():
      output_ids = model.generate(input_ids, images=image_tensor, do_sample=True, temperature=0.2, 
                                  max_new_tokens=1024, use_cache=True, stopping_criteria=[stopping_criteria])
    outputs = tokenizer.decode(output_ids[0]).strip()
    conv.messages[-1][-1] = outputs
    output = outputs.strip('</s>')
    return image, output

patent_data = pd.read_csv('/2020/processed_xml_2020.csv')
for index,row in patent_data.iterrows():
            patent_title = row['title']
            folder_list = eval(row['file_names'])
            file_name=folder_list[0]
            folder_name = "-".join(file_name.split("-")[:2])
            folder_name=os.path.join(folder_name,file_name)
            try:
                image, output = caption_image(f'/2020/{folder_name}', f'This is the image of {patent_title}. What is the shape of the image?What is the functionality of {patent_title}?')
                patent_data.loc[index, 'caption'] = output
                patent_data.iloc[[patent_data.index.get_loc(index)]].to_csv('/clipdata/processed_xml_2020_captions_ongoing.csv', mode='a', header=False, index=False)
            except:
                print('error')

patent_data.to_csv('/2020/processed_xml_2020_ccaptions.csv', index=False) 
print('done')
