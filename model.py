from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd
import numpy as np

SA_IDX = 0  #surface area idx
OH_IDX = 1  #overall height idx
GA_IDX = 2  #glazing area idx
HL_IDX = 3 #heating load idx

dataset = pd.read_csv('./data.csv')
print('hello')

# removing usesless columns if they exist
if ('Unnamed: 10' in dataset.columns):
    del dataset['Unnamed: 10']
if ('Unnamed: 11' in dataset.columns):
    del dataset['Unnamed: 11']

dataset.dropna(inplace=True,) #dropping enteries containing null or NaN

features = dataset[['Surface_Area','Overall_Height', 'Glazing_Area', 'Heating_Load']]
target = np.log(dataset['Cooling_Load'])

house_stats = features.mean().values.reshape(1, 4)

regr = LinearRegression().fit(features, target)

fitted_vals = regr.predict(features)

MSE = mean_squared_error(target, fitted_vals)
RMSE = np.sqrt(MSE)

def make_log_prediction(surface_area, overall_height, heating_load):
    house_stats[0][SA_IDX] = surface_area
    house_stats[0][OH_IDX] = overall_height
    house_stats[0][HL_IDX] = heating_load

    
    log_estimate = regr.predict(house_stats)
    log_upper = log_estimate + RMSE
    log_lower = log_estimate - RMSE
    
    estimate = np.e**log_estimate
    upper = np.e**log_upper 
    lower = np.e**log_lower

    return {"est": round(estimate[0],2), "upper_est":round(upper[0],2), "lower_est":round(lower[0], 2)}

