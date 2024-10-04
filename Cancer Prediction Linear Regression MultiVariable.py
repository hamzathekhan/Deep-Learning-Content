# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FnvNo8vhF_aEAM9Psl7bbKIMsnO89nV-
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
# %matplotlib inline

df = pd.read_csv("/content/cancer-probabilities.csv")
df.fillna("Never",inplace=True)
df["Smoking Habit"] = df["Smoking Habit"].replace(["Never","Occasional","Moderate","Heavy"],[0,1,2,3])
df["Drinking Habit"] = df["Drinking Habit"].replace(["Never","Occasional","Moderate","Frequent"],[0,1,2,3])
df["Biking Habit"] = df["Biking Habit"].replace(["Low","Medium","High"],[0,1,2])
df["Walking Habit"] = df["Walking Habit"].replace(["Low","Medium","High"],[0,1,2])
df["Jogging Habit"] = df["Jogging Habit"].replace(["Low","Medium","High"],[0,1,2])
df.head(5)

from sklearn.model_selection import train_test_split

X_train , X_test , y_train , y_test = train_test_split(df[["Smoking Habit",
                                                           "Drinking Habit",
                                                           "Biking Habit",
                                                           "Walking Habit",
                                                           "Jogging Habit"]],
                                df["Probability of Cancer"],test_size=0.2)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train,y_train)

model.score(X_test,y_test)

while True:
  smoking = int(input('''
  Smoking Habit:
  0. Never
  1. Occasional
  2. Moderate
  3. Heavy
  ===========>
  '''))
  drinking = int(input('''
  Drinking Habit:
  0. Never
  1. Occasional
  2. Moderate
  3. Frequent
  ===========>
  '''))
  biking = int(input('''
  Biking Habit:
  0.Low
  1.Medium
  2.High
  ===========>
  '''))
  walking = int(input('''
  Walking Habit:
  0.Low
  1.Medium
  2.High
  ===========>
  '''))
  jogging = int(input('''
  Jogging Habit:
  0.Low
  1.Medium
  2.High
  ===========>
  '''))
  print([smoking,drinking,biking,walking,jogging])
  print(model.predict([[smoking,drinking,biking,walking,jogging]]))
  print("=========================================================================")