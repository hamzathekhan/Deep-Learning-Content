# Ordinal Encoding
from sklearn.preprocessing import OrdinalEncoder
ordinal_encoder = OrdinalEncoder()
housing_cat_encoded = ordinal_encoder.fit_transform(housing[["ocean_proximity"]])  # It return numpy array
ordinal_encoder.categories_
housing_cat_encoded[:5]


# One Hot Encoding

from sklearn.preprocessing import OneHotEncoder
cat_encoder = OneHotEncoder()

housing_cat_1hot = cat_encoder.fit_transform(housing[["ocean_proximity"]]) # It return scipy sparse matrix
housing_cat_1hot
housing_cat_1hot.toarray()  # It will convert sparse matrix into numpy array
cat_encoder.categories_ 
