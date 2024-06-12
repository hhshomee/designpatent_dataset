# PatentCLIP and multimodal retrieval tasks
:fire: PatentCLIP is based on [CLIP](https://github.com/openai/CLIP), and we use an open source [open_clip](https://github.com/mlfoundations/open_clip) implementation for finetuning and inference 

## PatentCLIP with IMPACT dataset
Please download [train](https://drive.google.com/file/d/1Tasis4QHKWaSfhaW0ZHktgBRPrSmWiH3/view?usp=drive_link) and [val](https://drive.google.com/file/d/1_AZs-8loZctEiZo0xB9aTS4Vmya71Vwt/view?usp=drive_link) set.

### Usage
Load a PatentCLIP model
```
import open_clip
model, _, preprocess = open_clip.create_model_and_transforms('hf-hub:ellen625/PatentCLIP_ViT_B', device=device)
```
