# Time Series & Forecasting Applications

## Project Overview
This project focuses on applying time series analysis and forecasting techniques to various datasets. The goal is to compare classical forecasting methods (e.g., ARIMA/SARIMA) with machine learning approaches (e.g., LSTM, GRU, Prophet) and evaluate their performance on different time series problems.

### Team Members
- **22051662**
- **22052352**
- **22053747**
- **22051659**

---
### Objectives
1. **Data Wrangling**: Handle timestamps, missing data, and resample data to consistent intervals.
2. **Feature Engineering**: Incorporate features like moving averages, rolling windows, and external data (e.g., holidays, weather).
3. **Model Comparison**: Compare ARIMA/SARIMA, machine learning (RF, XGBoost), and deep learning (LSTM, GRU) models using metrics like MSE, RMSE, MAE, and MAPE.
4. **Explainability**: Use SHAP or feature importance plots to interpret model predictions.
5. **Visualizations**: Create plots to compare forecasted vs. actual values, and highlight seasonality, trends, and anomalies.

### Datasets
1. **Household Power Consumption**
   - [Dataset Link](https://archive.ics.uci.edu/ml/datasets/individual+household+electric+power+consumption)
   - **Goal**: Forecast hourly/daily energy usage.

2. **Predictive Maintenance Dataset**
   - [Dataset Link](https://www.kaggle.com/datasets/aftershock619/predictive-maintenance)
   - **Goal**: Predict and detect potential machine failures based on sensor data.

3. **Walmart or Rossmann Store Sales**
   - [Walmart Dataset](https://www.kaggle.com/c/walmart-recruiting-store-sales-forecasting)
   - [Rossmann Dataset](https://www.kaggle.com/c/rossmann-store-sales)
   - **Goal**: Forecast retail sales over time using seasonal effects, promotions, and holidays.

4. **Historical Stock Market Data**
   - [Dataset Link](https://www.kaggle.com/datasets/szrlee/stock-time-series-20050101-to-20171231)
   - **Goal**: Predict closing prices or detect potential trading signals.

### Notes

Each directory in `./src` consists of one of the problems assigned. Each person has contributed equally to this project. Python version management is not restricted to pyenv. People may use what they like, but for repository coherence and feasibility of report production, we shall keep [pyenv](https://github.com/pyenv/pyenv) as the default version management. [venv](https://docs.python.org/3/library/venv.html) shall be used for requirement management.

Because each member might have different Operating system / Workflow; for easy asssesment we have decided to keep a single requirement file and python version. The python version can be found in [python-version](.python-version) file.

Any potential users are required to hence install the mentioned python version. Next, they are required to install the requirements, after making a virtual environment in the aforementioned python version. They can then continue into [`src`](src/) directory to evaluate the projects.