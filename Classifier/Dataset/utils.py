import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.preprocessing import LabelEncoder
#from sent2vec.vectorizer import Vectorizer
import pickle
import numpy as np


import sys, os

def load_pickle(data_path,label_path,num,mode):
    
    data_file = open(data_path,"rb")
    label_file = open(label_path,"rb")
    data =pickle.load(data_file)
    label = pickle.load(label_file)
   
    class_count =np.unique(label).shape[0]
   
    length =int(len(data) * num)
    if mode == "train":
       return data[:length],label[:length],class_count
    elif mode== "valid":
      length = int(len(data)*(1-num))
      return data[length:], label[length:], class_count
    else:
        return data, label, class_count
# def load_data(path,num):
#     df =   pd.read_csv(path)
#     df = df.dropna()
#     df = df.sample(n=num)
#     title = list(df['title'])
#     num_classes = len(df['class'].unique())
#     classes =list(df['class'])
#     return title, classes, num_classes

# def sentence_embedding(title):
#     string = []
#     string.append(title)


#     #stop_words = list(set(stopwords))
#     blockPrint()
#     vector_obj =Vectorizer()
#     sentence_vector = []
#     #print("Size of the length",type(title))
#     enablePrint()
#     vector_obj.run(string)

#     vectors = vector_obj.vectors
#     for vec in vectors :
#         sentence_vector.append(vec)
#     return sentence_vector


# def label_encoding(classes):
#     cls = []
#     cls.append(classes)
#     le = LabelEncoder()
#     return le.fit_transform(cls)
