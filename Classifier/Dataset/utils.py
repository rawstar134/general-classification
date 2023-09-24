import pandas as pd
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import sent_tokenize, word_tokenize
from sklearn.preprocessing import LabelEncoder
from sent2vec.vectorizer import Vectorizer

def create_vocubulary(path):
    df = pd.read_csv(path)
   
    title = list(df["title"])
    #remove stopping words 

    title = []

def load_data(path): 
    df =   pd.read_csv(path)
    df = df.dropna()
    title = list(df['title'])
    num_classes = len(df['class'].unique())
    classes =list(df['class'])
    title = title[:5000]
    classes = classes[:5000]
    return title, classes, num_classes

def sentence_embedding(title):
   
    vector_obj =Vectorizer()
    #stop_words = list(set(stopwords))
    sentence_vector = []
    vector_obj.run(title)
    vectors = vector_obj.vectors
    for vec in vectors :
        sentence_vector.append(vec)
    return sentence_vector


def label_encoding(classes):
    le = LabelEncoder()
    return le.fit_transform(classes)
