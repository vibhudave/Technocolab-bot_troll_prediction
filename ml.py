# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 13:15:44 2021

@author: 10THHPi3
"""

import numpy as np
import pandas as pd
import warnings
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import accuracy_score

X = pd.read_csv('X_train.csv')
Y = pd.read_csv('y_train.csv')

model = LogisticRegression(random_state = 10)
model.fit(X,Y)

pickle.dump(model, open('model.pkl', 'wb'))