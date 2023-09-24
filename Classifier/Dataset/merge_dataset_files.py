import pandas as pd
import numpy as np
import json 


title = []
classes = []
description = []


df = pd.read_csv("train.csv")
print(df.columns)
Title = list(df['Title'])
classIndex = list(df['Class Index'])
class_dict = {3:"BUSINESS",4:"SCIENCE/TECHNOLOGY",1:'WORLD NEWS',2:'SPORT'}
classIndex  = [ class_dict[classIndex[i]] for i  in range(len(classIndex))]
Description = list(df['Description'])
#create csv file with news 

title.extend(Title)
classes.extend(classIndex)
description.extend(Description)



#open json file
f =  open("News_Category_Dataset_v3.json","r")
Lines = f.readlines()
 

json_data = []

news_dict ={}
# Strips the newline character
for line in Lines:
    json_data.append(json.loads(line.strip()))

class_dict = {
    "THE WORLDPOST":"WORLD NEWS",
    "WORLDPOST" : "WORLD NEWS",
    "U.S. NEWS" : "WORLD NEWS",
    "TECH" : "SCIENCE/TECHNOLOGY",
    "SCIENCE" : "SCIENCE/TECHNOLOGY",
    "ARTS" : "ARTS & CULTURE",
    "CULTURE & ARTS" :"ARTS & CULTURE",
    "STYLE" : "STYLE & BEAUTY",
    "SPORT" : "SPORTS"


}
remove_classes = { "LATINO VOICES":0,
"QUEER VOICES":0,
"FIFTY":0,
"PARENTING":0,
"PARENTS":0,
"DIVORSE":0,
"BLACK VOICE":0,
"WOMEN":0,
"WEIRD NEWS":0,
"BLACK VOICES":0,
"TASTE" : 0


}
category = []
headline = [] 
short_description = []
for data in json_data:
    c = data['category']
    h = data['headline']
    d = data['short_description']
    if c in remove_classes.keys():
        pass
    else:
        if c in class_dict:
            c = class_dict[c]
        category.append(c)
        headline.append(h)
        short_description.append(d)
title.extend(headline)
classes.extend(category)
description.extend(short_description)
c = set(category)
print(len(c),c)


print(json_data[0].keys())
#heading #description #class
print(len(title),len(classes),len(description))

dataframe = {"title":title,
             "description":description,
             "class": classes}

result_frame =pd.DataFrame(dataframe)
result_frame.to_csv("prepared_dataset.csv",index=False)
