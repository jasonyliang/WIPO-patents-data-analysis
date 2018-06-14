import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset3 = pd.read_excel("wipo_pub_941_2015-tech1/A03.xlsx", header = 5, skeprows = 4)
year = dataset3.iloc[:, 0].values
grants = dataset3.iloc[:, 1].values
growth_rate = dataset3.iloc[:, 2].values
growth_rate = pd.to_numeric(growth_rate, errors = 'coerce')
growth_rate = growth_rate.reshape(-1, 1)

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = "NaN", strategy = "mean")
growth_rate = imputer.fit_transform(growth_rate)        