import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


dataset = pd.read_csv('UP_2019.csv')

X = dataset.iloc[:,0:-1].values
y = dataset.iloc[:,-1].values


from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
X[:,0] = le.fit_transform(X[:,0])
X[:,4] = le.fit_transform(X[:,4])


from sklearn.preprocessing import OneHotEncoder
Ohe = OneHotEncoder(categorical_features=[1, 4])
X = Ohe.fit_transform(X)
X = X.toarray()