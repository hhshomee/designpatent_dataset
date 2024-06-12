# :art: IMPACT: A Large-scale Integrated Multimodal Patent Analysis and Creation Dataset for Design Patents 
We introduce IMPACT (Integrated Multimodal Patent Analysis and CreaTion Dataset) for Design Patents.

:black_nib: It is a large-scale multimodal patent dataset with detailed captions for design patent figures. 

:boom: Our dataset includes half a million design patents comprising 3.61 million figures along with captions from patents granted by the United States Patent and Trademark Office [USPTO](https://www.uspto.gov) over a 16-year period from 2007 to 2022.

<img width="2168" alt="main_fig" src="https://github.com/hhshomee/designpatent_dataset/assets/10067151/758947ff-8a5f-4ab9-a62f-e8c61938e7cc">

## Data
:green_book: Sample datas can be viewed and download [here](https://drive.google.com/file/d/1khIZ78GoBoOI_nvgyMJz5leJhW0UDb14/view?usp=drive_link).

## Patent Classification

```
python classification.py
```


## PatentCLIP and multimodal retrieval tasks
:fire: PatentCLIP is based on [CLIP](https://github.com/openai/CLIP), and we use an open source [open_clip](https://github.com/mlfoundations/open_clip) implementation for finetuning and inference 

### PatentCLIP with IMPACT dataset
Please download [train](https://drive.google.com/file/d/1Tasis4QHKWaSfhaW0ZHktgBRPrSmWiH3/view?usp=drive_link) and [val](https://drive.google.com/file/d/1_AZs-8loZctEiZo0xB9aTS4Vmya71Vwt/view?usp=drive_link) set.

#### Usage
Load a PatentCLIP model:
```
import open_clip
model, _, preprocess = open_clip.create_model_and_transforms('hf-hub:ellen625/PatentCLIP_ViT_B', device=device)
```
#### Demo on PatentCLIP and text-image retrieval

Text-image retrieval with PatentCLIP [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]([https://colab.research.google.com/drive/1wzmlnfvfJqyZqeL5kJMJr-O3QMwWgCiM?usp=sharing])
