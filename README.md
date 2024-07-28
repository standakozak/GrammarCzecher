# Czech Spell Checker
This repository contains code for training a Czech spell checker based on a transformer architecture. It also uses hand-crafted techniques for data augmentation.

The model is trained through `transformers.ipynb` which loads a model and tokenizer, fine-tunes them on the new data and saves them in `model` directory.

The file `attention.ipynb` contains a PyTorch implementation of Bahdanau Attention layer. It uses a different dataset for training. Because of the limited resources, I was not able to train it to get meaningful results.

## Data Augmentation
Because of the lack of error datasets for Czech language, I use Czech corpus without errors ([Czech news dataset](https://huggingface.co/datasets/hynky/czech_news_dataset_v2/tree/main/data)) from HuggingFace. From this, a dataset with errors is produced by applying edit operations (insertion, deletion, substitution, transposition).

To use it, download the dataset from HuggingFace and store it in `data/czech_news_dataset_v2`. Then, run the notebook `data_augmentation.ipynb` to produce the new dataset for model training. 