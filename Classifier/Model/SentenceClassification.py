import torch.nn as nn

class NewsClassificationModel(nn.Module):
    
    def __init__(self,num_classes):
        super(NewsClassificationModel, self).__init__()
        self.lstm =  nn.LSTM(input_size=768,hiddn_size=64, bidirectional=True,batch_first=True)
        self.dense = nn.Linear(66*2,num_classes)
        self.dropout = nn.Dropout(p=0.2)
        self.softmax = nn.Softmax(dim=2)
        self.lossfn = nn.CrossEntropyLoss()
    def forward(self, x):
        x = self.lstm(x)
        x = self.dropout(x)
        x = self.dense(x)
        x = self.softmax(x)

        return x
    
    def loss(self,data,label):
        prediction =self.forward(data)
        return self.lossfn(prediction,label)

    def predict(self,data):
        return self.forward(data)
