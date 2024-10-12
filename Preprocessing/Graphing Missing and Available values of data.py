import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
%matplotlib inline

df = pd.read_csv("/content/cancer-probabilities.csv")
df.info()

missing_values = df.isnull().sum()/len(df)*100
available_values = 100-missing_values


available_values.plot(kind="bar",ylabel="Percentage",color="blue",label="Available")
missing_values.plot(kind="bar",ylabel="Percentage",color="red",label="Missing")
plt.legend()
