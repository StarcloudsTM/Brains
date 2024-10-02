from statsmodels.tsa.arima.model import ARIMA
import numpy as np

# Sample Data
data = np.random.rand(100)

# ARIMA model
model = ARIMA(data, order=(5, 1, 0))
model_fit = model.fit()

# Forecast
forecast = model_fit.forecast(steps=10)
print(forecast)
