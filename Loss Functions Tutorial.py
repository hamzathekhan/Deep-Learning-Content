# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FnvNo8vhF_aEAM9Psl7bbKIMsnO89nV-
"""

import pandas as pd
import numpy as np

y_predicted = np.array([1,1,0,0,1])
y_true = np.array([0.3,0.7,1,0,0.5])

def mae(y_true,y_predicted):
  return np.mean(abs(y_true-y_predicted))

# Note:
# total of all errror is called Loss Function , While their mean is called as cost function

mae(y_true,y_predicted)

def mse(y_true,y_predicted):
  return np.mean(np.square(y_true-y_predicted))

mse(y_true,y_predicted)

epsilon = 1e-15

y_predict_new = [max(i,epsilon) for i in y_predicted]

y_predict_new = [min(i,1-epsilon) for i in y_predict_new]

y_predict_new = np.array(y_predict_new)
y_predict_new

-np.mean(y_true*np.log(y_predict_new)+(1-y_true)*np.log(1-y_predict_new))

# Find MSE with and without numpy
# without numpy


def mean_se(y_true,y_predicted):
  total = y_true - y_predicted
  square = total*total
  mean = square.sum() / len(y_true)
  return mean

mean_se(y_true,y_predicted)

# with numpy

def mean_sq_er(y_true,y_predicted):
  return np.mean(np.square(y_true-y_predicted))

mean_sq_er(y_true, y_predicted)