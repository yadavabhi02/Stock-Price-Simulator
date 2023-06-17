import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
!pip install yfinance
import yfinance as yf
import datetime as dt
!wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
!tar -xzvf ta-lib-0.4.0-src.tar.gz
%cd ta-lib
!./configure --prefix=/usr
!make
!make install
!pip install Ta-Lib
from scipy.stats import norm
from scipy.stats import skewnorm
#data scraping for past 30days
start_date = dt.date(2023, 1, 30);
end_date = dt.date(2023, 2, 28);
infosys=yf.Ticker('INFY.NS')
data = infosys.history(start = start_date, end = end_date)
data
#Selecting the Close column
price=data['Close']
price
#Calculating historical return in price(percent change)
price.pct_change()
#Dropping NaN values and storing in returns variable
returns=price.pct_change().dropna(how='any')
returns
l=norm.ppf(0.25)
u=norm.ppf(0.70)
mean=returns.mean()
stdev=returns.std()
np.random.seed(42)
n=np.random.normal(size=(30,10))
net_return=np.random.normal(size=(30,10))
newprice=np.random.normal(size=(30,10))
rows=n.shape[0]
cols=n.shape[1]
for k in range (0,cols):
  newprice[0][k]=price[price.size-1]
for i in range (1,rows):
  for j in range (0,cols):
    if n[i][j]>u:
      n[i][j]=u
    elif n[i][j]<l:
      n[i][j]=l
    else:
      n[i][j]=n[i][j]
    n[i][j]=(n[i][j]*stdev) + mean 
    net_return[i][j]=n[i][j]+1
    newprice[i][j]=newprice[i-1][j]*net_return[i][j]
final_price=newprice
final_price
plt.figure(figsize=(20,10))
plt.title('Stock Simulations', fontsize=100, color='g')
plt.plot(final_price)
#data scraping for next 30days
start_date = dt.date(2023, 3, 1);
end_date = dt.date(2023, 4, 19);
infosys=yf.Ticker('INFY.NS')
data1 = infosys.history(start = start_date, end = end_date)
data1
#Selecting the Close column
price1=data1['Close']
price1
plt.figure(figsize=(20,10))
X = np.arange(0,30,1);
plt.title('Stock Simulations', fontsize=100, color='g')
plt.plot(X,final_price,color='b',label='predicted');
plt.plot(X,price1,color='r',label='predicted');