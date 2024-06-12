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

:hugs: PatentCLIP-ViT-B [checkpoint](https://huggingface.co/ellen625/PatentCLIP_ViT_B)

:hugs: PatentCLIP-Title-ViT-B [checkpoint](https://huggingface.co/ellen625/PatentCLIP_ViT_B_title)

#### Usage
Load a PatentCLIP model:
```
import open_clip
model, _, preprocess = open_clip.create_model_and_transforms('hf-hub:ellen625/PatentCLIP_ViT_B', device=device)
```
#### Demo on PatentCLIP and text-image retrieval

Text-image retrieval with PatentCLIP [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)]([https://colab.research.google.com/drive/1wzmlnfvfJqyZqeL5kJMJr-O3QMwWgCiM?usp=sharing])

#### Multimodal retrieval results 

|           |    Dataset    |  Backbone | Text-Image |       |       | Image-Text |       |          |
|:---------:|:-------------:|:---------:|:----------:|:-----:|:-----:|:----------:|:-----:|:--------:|
|           |               |           |     R@1    |  R@5  |  R@10 |     R@1    |  R@5  |   R@10   |
| Zero-shot |  Image-Title  |  ResNet50 |    0.52    |  2.10 |  3.32 |    0.20    |  0.72 |   1.64   |
|           |               | ResNet101 |    1.02    |  3.20 |  4.72 |    0.30    |  0.82 |   1.28   |
|           |               |  ViT-B-32 |    1.06    |  3.54 |  5.56 |    0.38    |  1.62 |   2.60   |
|           |               |  ViT-L-14 |    2.78    |  7.38 | 10.40 |    1.16    |  4.30 |   7.32   |
|           | Image-Caption |  ResNet50 |    0.82    |  2.52 |  4.08 |    0.78    |  2.32 |   3.48   |
|           |               | ResNet101 |    1.44    |  4.52 |  6.48 |    0.98    |  2.98 |   4.96   |
|           |               |  ViT-B-32 |    1.98    |  5.24 |  7.42 |    1.06    |  4.26 |   6.32   |
|           |               |  ViT-L-14 |    **4.46**    | **10.74** | **15.16** |    **3.42**    |  **8.90** |   **12.88**  |
| Finetuned | Image-Caption |  ResNet50 |    5.38    | 15.52 |  22.7 |     5.9    |  16.6 |   23.86  |
|           |               | ResNet101 |    7.44    |  20.6 | 28.48 |    7.02    | 19.70 |   27.58  |
|           |               |  ViT-B-32 |    10.24   | 25.56 | 35.06 |    9.88    | 25.90 |   35.08  |
|           |               |  ViT-L-14 |    **20.58**   | **43.14** | **53.00** |    **20.44**   | **42.34** | **52.56** |
