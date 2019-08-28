# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 07:49:38 2019

@author: User
"""

# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
style.use('ggplot')

# Import the dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, -1].values
y = dataset.iloc[:,1].values

# Splitting the dataset into the Training set and Test s 0)