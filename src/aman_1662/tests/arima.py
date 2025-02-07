from statsmodels.tsa.arima.model import ARIMA
import pandas as pd
import pickle

df = pd.read_csv('./data/power_consumption_with_moving_averages.csv', parse_dates=['datetime'], index_col='datetime')

target = 'Global_active_power'

p, d, q = 1, 0, 1
print("-" * 50)
print("Training ARIMA without Difference")
model_no_diff = ARIMA(df[target], order=(p, d, q))
model_no_diff_fit = model_no_diff.fit()
print('ARIMA Model without Differencing')
print(model_no_diff_fit.summary())


with open('./models/arima_model_no_diff_fit.pkl', 'wb') as file:
    pickle.dump(model_no_diff_fit, file)
    print("Saved Model, Succesfully.")

d = 1
print("-" * 50)
print("Training ARIMA with Difference")
model_diff = ARIMA(df[target], order=(p, d, q))
model_diff_fit = model_diff.fit()
print('\nARIMA Model with Differencing')
print(model_diff_fit.summary())

with open('./models/arima_model_diff_fit.pkl', 'wb') as file:
    pickle.dump(model_diff_fit, file)
    print("Saved Model, Succesfully.")
