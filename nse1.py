#!/usr/bin/env python
# coding: utf-8

# In[82]:


# Import necessary packages
from bs4 import BeautifulSoup
import requests
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
from datetime import date
import re
import sys


# In[83]:


class Nse:
    def __init__(self):
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Apple'
                      'Webkit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'}
        self.session = requests.Session()
        self.session.get("http://nseindia.com", headers=self.headers)
        self.stockTypes = "NIFTY%20100"
        
    def live_market_data(self,stockTypes): 
        self.stockTypes = stockTypes
        print(self.stockTypes)
        self.strURL = "https://www.nseindia.com/api/equity-stockIndices?index=" + self.stockTypes
        print(self.strURL)
        data = self.session.get(self.strURL, headers=self.headers).json()["data"]
        df = pd.DataFrame(data)
        return df


# In[84]:


# Print number of arguments passed in
print (f'Number of arguments: {len(sys.argv)}')

stockTypes = "NIFTY 100"
if (len(sys.argv) > 1):   
    #live_market_index = ['NIFTY 50','NIFTY 100' 'NIFTY MIDCAP 50']   
    if(sys.argv[1] == "-f"):
        sys.argv[1] = "NIFTY 100" 
    #print(sys.argv[1])        
    #print(sys.argv[1].replace(' ','%20').replace('&','%26'))
    stockTypes = sys.argv[1]   

nse = Nse()
df = nse.live_market_data(stockTypes)
#print (df)


# In[85]:


today = date.today()
d1 = today.strftime("%d/%m/%Y")
print("===========Date", d1)
print("===========",stockTypes)
print ("=========== Open=High (Sell) ===========")
print ("======================================")
print ("%15s %10s %10s" % ("Symbol","Open","High"))
print ("======================================")
for index, row in df.iterrows():
    if (row.open.is_integer()):        
        if(row.open == row.dayHigh):            
            formatted_open = "{:.2f}".format(row.open)
            formatted_dayHigh = "{:.2f}".format(row.dayHigh)
            print ("%15s %10s %10s" %(row.symbol,row.open,row.dayHigh))

print ("\n")
print ("=========== Open=Low (Buy) ===========")
print ("======================================")
print ("%15s %10s %10s" % ("Symbol","Open","Low"))
print ("======================================")
for index, row in df.iterrows():
    if (row.open.is_integer()):        
        if(row.open == row.dayLow):
            formatted_open = "{:.2f}".format(row.open)
            formatted_dayLow = "{:.2f}".format(row.dayLow)
            print ("%15s %10s %10s" %(row.symbol,row.open,row.dayLow)) 


# In[ ]:




