from Classifier.Model.SentenceClassification import NewsClassificationModel
from Classifier.Dataset.Dataset import NewsSentenceLevelClassificationDataset
import torch
from  torch.optim import AdamW
from torch.utils.data import DataLoader
import gc
import numpy as np
#model intialization
from torchmetrics.classification import F1Score
from tqdm import tqdm
f1 = F1Score(task="multiclass", num_classes=27)

def init():
    model = NewsClassificationModel(27)
    return model

def training_step(model,data,label):
    model.train()
    prediction,loss = model.loss(data,label)
    data = data.detach().cpu().numpy()
    label = label.detach().cpu().numpy()
    prediction = prediction.detach().cpu().numpy()
    prediction_map = []
    label_map = []
    for i  in range(len(prediction)):
        prediction_index = np.argmax(prediction[i])
        label_index = np.argmax(label[i])
        prediction_map.append(prediction_index)
        label_map.append(label_index)
    prediction_map = np.array(prediction_map,dtype=float)
    label_map = np.array(label_map,dtype=float)
    prediction_map = torch.from_numpy(prediction_map)
    label_map = torch.from_numpy(label_map)
    f1_score = f1(prediction_map,label_map)

    return loss,f1_score

def validation_step(model,data,label):
    model.eval()
    prediction,loss =model.loss(data,label)
    data = data.detach().cpu().numpy()
    label = label.detach().cpu().numpy()
    prediction = prediction.detach().cpu().numpy()
    prediction_map = []
    label_map = []
    for i  in range(len(prediction)):
        prediction_index = np.argmax(prediction[i])
        label_index = np.argmax(label[i])
        prediction_map.append(prediction_index)
        label_map.append(label_index)
    prediction_map = np.array(prediction_map,dtype=float)
    label_map = np.array(label_map,dtype=float)
    prediction_map = torch.from_numpy(prediction_map)
    label_map = torch.from_numpy(label_map)
#     print(prediction_map,label_map)
    f1_score = f1(prediction_map,label_map)
    return loss, f1_score

#begining
model = init()
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)
print(model)

print(device)
optimizer = AdamW(model.parameters(),lr=1e-4)


#set train and validation dataloader

torch.cuda.empty_cache()
gc.collect()


training_data = NewsSentenceLevelClassificationDataset(data_path="/content/drive/MyDrive/NEWS Classification/new_embedding.pkl",label_path="/content/drive/MyDrive/NEWS Classification/label.pkl",num=0.9,mode="train")
testing_data = NewsSentenceLevelClassificationDataset(data_path="/content/drive/MyDrive/NEWS Classification/new_embedding.pkl",label_path="/content/drive/MyDrive/NEWS Classification/label.pkl",num=0.1,mode="train")
train_dataloader = DataLoader(training_data, batch_size=256, shuffle=True)
test_dataloader = DataLoader(testing_data,batch_size=256,shuffle=True)


epochs = 50

for epoch in  range(0,epochs):
    print('Epoch',epoch)
    loss_train = []
    score_train = []
   
    for data,label in train_dataloader:
        optimizer.zero_grad()

        label = label.type(torch.FloatTensor)
        data = data.to(device)
        label = label.to(device)
        loss,f1_score = training_step(model,data,label)
        loss.backward()
        optimizer.step()
       
        
        loss_train.append(loss.item())
        score_train.append(f1_score)
 
    for data,label in test_dataloader:
        optimizer.zero_grad()
        label = label.type(torch.FloatTensor)
        data = data.to(device)
        label = label.to(device)
        loss,f1_score = training_step(model,data,label)
        loss.backward()
        optimizer.step()
       
       
       
        loss_train.append(loss.item())
        score_train.append(f1_score)

    loss_val =[]
    score_val = []
    for data,label in test_dataloader:

        label = label.type(torch.FloatTensor)
        data = data.to(device)
        label = label.to(device)

        loss,f1_score = validation_step(model,data,label)
        loss_val.append(loss.item())
        score_val.append(f1_score)
    loss_val = sum(loss_val)/len(loss_val)
    loss_train = sum(loss_train)/len(loss_train)
    score_train = sum(score_train)/len(score_train)
    score_val = sum(score_val)/len(score_val)
    torch.save({"model":model.state_dict(),
                            "o_model" : model,
                             "optimizer":optimizer.state_dict(),
                             "f1-score_training":  score_train,
                             "f1-score_val":score_val,
                             "loss_train":loss_val,
                             "loss_val" : loss_train
                           },'/content/drive/MyDrive/NEWS Classification/Models/Model-Layer-Stopping-Epoch:'+str(epoch+1)+'.pt')
                  # print("Early stopping called and stopped the training.")
    print("Epoch",(epoch+1),' Training Loss:', loss_train, ' F1-score',score_train,'Validation Loss:',loss_val,'F1-score',score_val)