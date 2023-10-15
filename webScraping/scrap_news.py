import requests
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date
today = date.today()
d = today.strftime("%m-%d-%y")
print("date =" ,d)
date = 10-27-21

nbc_business = "https://www.ndtv.com/latest"
res = requests.get(nbc_business)
soup = BeautifulSoup(res.content, 'html.parser')



#get the latest news 
headlines = soup.find_all('div',attrs={'class':'s-ls_txt'})
for row in soup.find_all('div',attrs={'class':'s-ls_txt'}):
    for text in row.find_all('a'):
        print(text['href'])
    print("########")

print(len(headlines))