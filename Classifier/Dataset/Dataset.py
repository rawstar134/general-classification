import torch
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import torch.nn.functional as F
from utils import load_data, sentence_embedding, label_encoding

class NewsSentenceLevelClassificationDataset(Dataset):
    def __init__(
        self,file_path
    ):
        self.file_path = file_path

        #load dataset
        title, classes, class_count = load_data(self.file_path)
        #sentence embedding
        embedded_title = sentence_embedding(title)

        #label encoding
        label_encode= label_encoding(classes)
        self.embedding = np.array(embedded_title)
        self.classes = np.array(label_encode)
        self.num_class = int(class_count)


    def __len__(self):
        print(len(self.embedding))
        return len(self.embedding)

    def __getitem__(self,idx):
        Y = F.one_hot(torch.tensor(self.classes[idx]), num_classes=self.num_class)
        return self.embedding[idx], Y
