# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 04:12:58 2019

@author: User
"""

#Importing the  dataset
dataset =pd.read_csv('Social_Network_Ads.csv')
X = dataset.iloc[:, [2, 3]].values
y = dataset.iloc[:, 4].values



