#sentence embedding code
import pickle
import pandas as pd
from sent2vec.vectorizer import Vectorizer
jump = 256
def sentence_embedding(text_list):
  f = open("embedding.pkl","wb")
  for i in range(0,len(text_list),jump):
    vector_obj =Vectorizer()
    sentence_vector = []
    vector_obj.run(text_list[i:i+jump])

    vectors = vector_obj.vectors
    for vec in vectors :
        sentence_vector.append(vec)
    # sentence_vector
    print("Dumped",i, i+jump)
    pickle.dump(sentence_vector,f)


df = pd.read_csv("/content/drive/MyDrive/NEWS Classification/preprocessed_data.csv")
df = df.dropna()
# df = df.sample(n=num)
title = list(df['title'])
sentence_embedding(title)