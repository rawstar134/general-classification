from ast import Num
import torch
import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import torch.nn.functional as F
from utils import load_pickle
class NewsSentenceLevelClassificationDataset(Dataset):
    def __init__(self,data_path,label_path,num,mode):
        self.data_path = data_path
        self.label_path = label_path
        self.mode = mode
        self.num = num
        #load dataset
        title, classes, class_count = load_pickle(self.data_path,self.label_path,self.num,self.mode)
        #sentence embedding
        #embedded_title = sentence_embedding(title)

        #label encoding

        #label_encode= label_encoding(classes)
        self.data = title
        self.classes = classes
        self.num_class = class_count
        print(len(self.data))

    def __len__(self):
        return len(self.data)

    def __getitem__(self,idx):
        X = self.data[idx]
        Y = F.one_hot(torch.tensor(self.classes[idx]), num_classes=self.num_class)
        return X, Y
