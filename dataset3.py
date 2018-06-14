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


fig, ax1 = plt.subplots()
ax1.set_xlabel("Year")
ax1.set_ylabel("Grants")
ax1.bar(year, grants, label = "Grants", color = 'b', alpha = 0.2)
plt.legend(bbox_to_anchor=(0.22, 0.9))

ax2 = ax1.twinx()
ax2.set_ylabel("Growth Rate")
ax2.plot(year, growth_rate, label = "Growth Rate", color='green')
plt.legend(bbox_to_anchor=(0.3, 1))
plt.show()
