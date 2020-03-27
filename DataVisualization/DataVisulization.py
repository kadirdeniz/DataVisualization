"""
Created on Wed Mar 25 20:12:26 2020
@author: deniz
"""
import pandas as pd
import numpy as np

veriler=pd.read_csv('veriler.csv')
ulke=veriler.iloc[:,0:1]
cinsiyet=veriler.iloc[:,4:5]
num=veriler.iloc[:,1:4]

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder()
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
ulke=ohe.fit_transform(ulke).toarray()
ulke = pd.DataFrame(ulke,columns=['tr','us','fr'])
cinsiyet = le.fit_transform(cinsiyet)
cinsiyet = pd.DataFrame(cinsiyet,columns=['cinsiyet'])

ulnum=pd.concat([ulke,num],axis=1)
sonuc = pd.concat([ulnum,cinsiyet],axis=1)

from sklearn.preprocessing import StandardScaler
ss = StandardScaler()
sonuc = ss.fit_transform(sonuc)












