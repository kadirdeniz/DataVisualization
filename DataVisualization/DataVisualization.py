"""
Created on Wed Mar 25 20:12:26 2020
@author: deniz
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

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
sonuc = pd.DataFrame(sonuc,columns=['tr','us','fr','boy','kilo','yas','cinsiyet'])
'''
sonuc['boy'].plot(style='red')
sonuc['kilo'].plot(style='blue')
sonuc['yas'].plot(style='green')
plt.title('Boy Verileri')

sonuc['boy'].plot.barh(color='orange')
sonuc['kilo'].plot.barh(style='blue')
sonuc['yas'].plot.barh(style='green')
'''
'''
sonuc.hist(color='green')

sonuc.plot.scatter(x='boy',y='kilo')
plt.title('Purchase Week Vs Price Per User Class Based on Tx') 
'''
'''
#first figure
plt.figure(1)
plt.plot(sonuc)
plt.title('Sonuc Verileri')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
#second figure
plt.figure(2)
plt.subplot(sonuc)
'''

plt.plot(sonuc['boy'],color='red',linestyle='--',marker='x')
plt.plot(sonuc['kilo'],color='green',linestyle='--',marker='o')
legend_labels=['Boy','Kilo']
plt.legend(legend_labels,loc=8)
plt.title('Deneme123')
plt.xlabel('Boy')
plt.ylabel('Kilo')
plt.show()









