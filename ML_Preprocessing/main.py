import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.preprocessing

dataset = pd.read_csv('Python/Data.csv')
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Replacing missing data

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x[:, 1:3])
x[:, 1:3] = imputer.transform(x[:, 1:3])

from sklearn.preprocessing import OneHotEncoder, LabelEncoder

