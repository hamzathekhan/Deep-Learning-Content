from sklearn.datasets import load_iris
from matplotlib.pyplot as plt

X , y = load_iris(return_X_y=True)

from sklearn.neighbors import KNeighborsRegressor

mod = KNeighborsRegressor()
mod.fit(X,y)

pred_data = mod.predict(X)
plt.scatter(pred_data,y)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()
