#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 19:48:17 2017

@author: evanbaker
"""

#%load_ext autoreload
#%autoreload 2

import numpy as np
import pandas as pd
#from joblib import Parallel, delayed
import operator
import matplotlib.pyplot as plt

from crycompare import Price

#from ClusterLib.clusterlib import *
#from ClusterLib.distlib import *

#%matplotlib inline


#Successfully imported crycompare. 

# Price is defined in crycompare.
p = Price()

#coinList = p.coinList()
#coins = sorted(list( coinList['Data'].keys() ))

# With the histoDay() function we can fetch the historical data (OHLC prices and volumes) for a given pair. We keep only coins which have a non-trivial history (about 1350).


#h = History()



#df_dict = {}
#for coin in coins:
#    histo = h.histoDay(coin,'USD',allData=True)
#   if histo['Data']:
#        df_histo = pd.DataFrame(histo['Data'])
#       df_histo['time'] = pd.to_datetime(df_histo['time'],unit='s')
#        df_histo.index = df_histo['time']
#        del df_histo['time']
#        del df_histo['volumefrom']
#        del df_histo['volumeto']
        
#df_dict[coin] = df_histo
               
#crypto_histo = pd.concat(df_dict.values(), axis=1, keys=df_dict.keys())
        
#histo_coins = [elem for elem in crypto_histo.columns.levels[0] if not elem == 'MYC']

#histo_length = {}
#for coin in histo_coins:
#    histo_length[coin] = np.sum( ~np.isnan(crypto_histo[coin]['close'].values) )
    
#sorted_length = sorted(histo_length.items(), key=operator.itemgetter(1),reverse=True)





       

