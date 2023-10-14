# News-classification
Classification of College Name, Organization Name, Date, Object  etc...


#Sentence level classification
We gathered news classification data from different source including kaggle and huggingface. 
## Process 
    1) Fetched headline from different files and save into one csv file.
    2) Use same CSV file, preprocessed the headline including remove stopwords, remove multiple space and special character.
    3) Used the sent2Vec model for sentence embedding.
    4) Create the dataset and dataloader.ss
    5) Train the LSTM model.
    6) Measure the accuracy using F1-score.
#Word level classification
