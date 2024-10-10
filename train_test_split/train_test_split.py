housing = pd.read_csv("/content/housing.csv")
housing.head()

################################ Manual ::::::Method 1 of Split train test ################################################
# Spliting Train Test data Manually with permutation method
from numpy.random import permutation , seed

def split_train_test(data,test_ratio):
  seed(42) # It will keep the permutation same when run again
  shuffled_indices = permutation(len(data))
  test_set_size = int(len(data) * 0.2)
  test_indices = shuffled_indices[:test_set_size]
  train_indices = shuffled_indices[test_set_size:]
  return data.iloc[train_indices] , data.iloc[test_indices]

train_data , test_data = split_train_test(housing,0.2)

'''Saving Train and Test data for later use it will keep the order same'''
# train_data.to_csv("train_data.csv",index=False)
# test_data.to_csv("test_data.csv",index=False)

# new_train_data = pd.read_csv("/content/train_data.csv")
# new_test_data = pd.read_csv("/content/test_data.csv")

################################## By Using Algorithm :Method 2 of Train Test Split #############################################
# Splitting Train Test  with sklearn.model_selection.train_test_split
from sklearn.model_selection import train_test_split
x_train , x_test , y_train , y_test = train_test_split(housing.drop("ocean_proximity",axis=1),housing["ocean_proximity"],test_size=0.2)
len(x_test) ##### x_test = 4128
