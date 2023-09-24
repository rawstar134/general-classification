from Dataset import NewsSentenceLevelClassificationDataset
from torch.utils.data import DataLoader

training_data = NewsSentenceLevelClassificationDataset("preprocessed_data.csv",3)
train_dataloader = DataLoader(training_data, batch_size=1, shuffle=True)
#test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)

for data,label in train_dataloader:
    print(data.shape)
    print(label.shape,label)
    break
