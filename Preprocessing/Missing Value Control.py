# Getting Rid of missing values
===================================================================================================
#### Option1 : Drop null values indexes only
opt1_housing = housing.dropna(subset=["total_bedrooms"])
opt1_housing.info()

==================================================================================================
#### Option 2 : Drop the whole columns
opt2_housing = housing.drop("total_bedrooms",axis=1)
opt2_housing.info()
==================================================================================================
#### Option 3 : Fill Missing values with median , mean , modes
median = housing["total_bedrooms"].median()
housing["total_bedrooms"].fillna(median,inplace=True)


==================================================================================================

### Using SimpleImputer to Control Missing Values to can be used in test set as well

from sklearn.impute import SimpleImputer

impute = SimpleImputer(strategy="median")

housing_num = housing.drop("ocean_proximity",axis=1)

# fitting the imputer on training data

impute.fit(housing_num)


# checking Imputer for statistics
impute.statistics_

# housing_num.median().values


X = impute.transform(housing_num)

housing_tr = pd.DataFrame(X,columns=housing_num.columns)
