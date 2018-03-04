#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## NOTE: spyder does NOT autosave.  MAKE SURE YOU SAVE REGULARLY

# Note2: NEVER close the damn terminal.  That force closes spyder and you will LOSE EVERYTHING

# Where this came from: https://gmarti.gitlab.io/cryptocurrency/2017/08/25/download-cryptocoins-api-python.html

"""
Created on Sat Nov 18 21:12:22 2017

@author: evanbaker
"""
from math import log10
import numpy as np
import pandas as pd

import plotly 
plotly.tools.set_credentials_file(username='ebaker88', api_key='KqbUvmUGGBb8wEZgRAcb')

import plotly.plotly as py
import plotly.graph_objs as go
import operator
import matplotlib.pyplot as plt

# Create a sub-function that imports locally all of the necessary functions and data.
# The goal is to be able to make progress while offline.

from crycompare import Price
from crycompare import History

p = Price()

coinList = p.coinList()

# Stores the names of all 1250 coins in the variable coins
coins = sorted(list( coinList['Data'].keys() ))


h = History()

# Top 22 coins as of 2017.11.28
#coins = ['BTC','ETH','BCH','XRP','BTG','LTC','DASH','MIOTA','ETC','XMR','NEO','XEM','EOS','XLM','QTUM','ZEC','OMG','LSK','HSR','STRAT']
# missing MIOTA, 
coins = ['BTC','ETH','BCH','XRP','BTG','LTC','DASH','ETC','XMR','NEO','XEM','EOS','XLM','QTUM','ZEC','OMG','LSK','HSR','STRAT']
# Instead of pulling in all 1250 coins, i simplify and just pull in this smaller subset
#coins = ['BTC','VTC','XMR','LTC','ETH','BCH'] #Expand this to other coins you care about.

        # NEO, ZEC, BTG, DASH, 
        
df_dict = {}
for coin in coins:
    histo = h.histoDay(coin,'USD',allData=True)
    if histo['Data']:
        df_histo = pd.DataFrame(histo['Data'])
        df_histo['time'] = pd.to_datetime(df_histo['time'],unit='s')
        df_histo.index = df_histo['time']
        del df_histo['time']
        del df_histo['volumefrom']
        del df_histo['volumeto']
        
        df_dict[coin] = df_histo
               
crypto_histo = pd.concat(df_dict.values(), axis=1, keys=df_dict.keys())

histo_coins = [elem for elem in crypto_histo.columns.levels[0] if not elem == 'MYC']

histo_length = {}
for coin in histo_coins:
    histo_length[coin] = np.sum( ~np.isnan(crypto_histo[coin]['close'].values) )
    
sorted_length = sorted(histo_length.items(), key=operator.itemgetter(1),reverse=True)
        
# we keep the 300 coins having the longest time series of historical prices
sub_coins = [sorted_length[i][0] for i in range(len(coins))]

sub_crypto_histo = crypto_histo[sub_coins]
sub_crypto_histo.tail()

N = len(sub_coins)
recent_histo = sub_crypto_histo[-1000:]

returns_dict = {}
for coin in sub_coins:
    coin_histo = recent_histo[coin]
    coin_returns = pd.DataFrame(np.diff(np.log(coin_histo.get_values()),axis=0))
    returns_dict[coin] = coin_returns

recent_returns = pd.concat(returns_dict.values(),axis=1,keys=returns_dict.keys())
recent_returns.index = recent_histo.index[1:]

recent_returns.isnull().values.any()

False

# Create a plot of coin returns over time

plt.figure(figsize=(40,10))
lines = []
for coin in sub_coins:
    lines += plt.plot(recent_returns[coin], label=coin)
#plt.legend(sub_coins,loc='upper left')
plt.xlabel('time',fontsize=18)
plt.ylabel('returns \'X/USD\'',fontsize=18)
plt.legend(lines,coins)
plt.show()


# Create a plot of coin price over time
plt.figure(figsize=(40,10))
lines = []
for coin in sub_coins:
    lines += plt.plot(recent_histo[coin].close, label=coin)
plt.xlabel('time',fontsize=18)
plt.ylabel('Coin Price \'X/USD\'',FONTSIZE=18)
plt.legend(lines,coins)
plt.show()

# Create a log plot of coin price over time
plt.figure(figsize=(40,10))
lines = []
for coin in sub_coins:
    lines += plt.plot(recent_histo[coin].close.apply(lambda x: log10(x)), label=coin)
plt.xlabel('time',fontsize=18)
plt.ylabel('log Coin Price \'X/USD\'',FONTSIZE=18)
plt.legend(lines,coins)
plt.show()

# calculate the return on investment of any specific coin on some number of days before the current day.
def roi(coin,returnDay):
    roiOut = recent_histo[coin].close[-1]/recent_histo[coin].close[-1-returnDay]-1
    return roiOut

roiDictionary = {}
returnDayList = [1,7,15,30,60,120,365]         
for coin in coins:
    for returnDay in returnDayList:
        roiDictionary[coin,returnDay] = roi(coin,returnDay)


tempIndexString = ''
indexStringList = []

for percReturn in returnDayList:
    tempIndexString = str(percReturn) + ' day return'
    indexStringList.append(tempIndexString)

roiTableDictionary = {}
for coin in coins:
    roiTableDictionary[coin] = [roi(coin,returnDayList[0]),roi(coin,returnDayList[1]),
                      roi(coin,returnDayList[2]),roi(coin,returnDayList[3]),roi(coin,returnDayList[4]),roi(coin,returnDayList[5]),roi(coin,returnDayList[6])]


for coin in coins:
    for index, value in enumerate(roiTableDictionary[coin]):
        roiTableDictionary[coin][index] = np.round(value*100,1)
    #roiTableDictionary[coin] = roiTableDictionary[coin]

temp = []
keylist = []
for key, value in roiTableDictionary.items():
    temp = [key]
    keylist.append(temp)
    
temp = []
for small_list in keylist:
    temp += small_list
newlist = temp    

keylist = newlist 
    #lists
temp = []
dictlist = []
for key, value in roiTableDictionary.items():
    temp = [value]
    dictlist.append(temp)


roiTableDictionary

df = pd.DataFrame(roiTableDictionary,index=indexStringList)

# Transpose the data frame so that coins are on the left and coin stats are on top. 
df.T



#df2 = pd.DataFrame.from_dict(roiTableDictionary)

#df2 = pd.DataFrame.from_dict(roiDictionary)
    
# Convert the dataframe to a list of lists.  Then display that using the table below.

#setindex

headerColor = 'grey'
rowEvenColor = 'lightgrey'
rowOddColor = 'white'

trace0 = go.Table(
  type = 'table',
  header = dict(
    values = [['<b>Cryptos</b>'],
                  ['<b>1day</b>'],
                  ['<b>7day</b>'],
                  ['<b>15day</b>'],
                  ['<b>30day</b>']],
    line = dict(color = '#506784'),
    fill = dict(color = headerColor),
    align = ['left','center'],
    font = dict(color = 'white', size = 12)
  ),
  cells = dict(
    values = dictlist,      
    #values = [['Salaries', 'Office', 'Merchandise', 'Legal', '<b>TOTAL</b>']],
      #[[1200000, 20000, 80000, 2000, 12120000]],
      #[[1300000, 20000, 70000, 2000, 130902000]],
      #[[1300000, 20000, 120000, 2000, 131222000]],
      #[[1400000, 20000, 90000, 2000, 14102000]]],
    line = dict(color = '#506784'),
    fill = dict(color = [[rowOddColor,rowEvenColor,rowOddColor,
                               rowEvenColor,rowOddColor]]),
    align = ['left', 'center'],
    font = dict(color = '#506784', size = 11)
    ))

data = [trace0]

py.iplot(data, filename = "alternating row colors")        
        
        
#line_up, = plt.plot([1,2,3], label='Line 2')
#line_down, = plt.plot([3,2,1], label='Line 1')
#plt.legend(handles=[line_up, line_down])


#p = [1,2,3,4]

#print 'test' p 'test'
#disp(p)
#plt.plot(p)

# TODO: 2017.11.28

# Display Volume.  Display Volume Growth over long periods of time

# Display Social (whatever that means) Display social growth.

# Add all the top 20 coins to this list. 