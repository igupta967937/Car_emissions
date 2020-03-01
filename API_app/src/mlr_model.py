import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle as pkl
from sklearn.linear_model import LinearRegression

df = pd.read_csv('../data/Car_Emissions_Fuel.csv')
X = df[['ENGINESIZE','Gasoline','Prem_Gasoline']]
y = df.CO2EMISSIONS

mlr = LinearRegression()

# Fit model with full dataset as trainig set
mlr.fit(X, y)

# Save model to local disk
pkl.dump(mlr, open('mlr_model.pkl','wb'))