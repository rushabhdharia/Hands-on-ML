#Code is copied from Chap 1 of the book Hands on Machine Learning with Scikit-Learn and Tensorflow

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
import sklearn.linear_model
import sklearn.neighbors

def prepare_country_stats(oecd_bli, gdp_per_capita):
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita, left_index=True, right_index=True)
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    remove_indices = [0, 1, 6, 8, 33, 34, 35]
    keep_indices = list(set(range(36)) - set(remove_indices))
    return full_country_stats[["GDP per capita", 'Life satisfaction']].iloc[keep_indices]

#Load the data
oecd_bli = pd.read_csv("BLI_25012019044455549.csv", thousands = ',')
gdp_per_capita = pd.read_csv("WEO_Data.xls", thousands = ',', delimiter = '\t', encoding = 'latin1', na_values='n/a')

# Prepare the data
country_stats = prepare_country_stats(oecd_bli, gdp_per_capita)
X = np.c_[country_stats["GDP per capita"]]
y = np.c_[country_stats["Life satisfaction"]]

# Visualize the data
country_stats.plot(kind = 'scatter', x = 'GDP per capita', y ='Life satisfaction')
plt.show()

#Select a linear model
lin_reg_model = sklearn.linear_model.LinearRegression()

#Train the model
lin_reg_model.fit(X,y)

# Make a prediction for Cyprus
X_new = [[22587]] # Cyprus' GDP per capita
print(lin_reg_model.predict(X_new))

#-------------------------------------------------------------------------------------------------
# For k-nearest neighbors 
clf = sklearn.neighbors.KNeighborsRegressor(n_neighbors=3)
#Train the model
clf.fit(X,y)

# Make a prediction for Cyprus
X_new = [[22587]] # Cyprus' GDP per capita
print(clf.predict(X_new))