df=pd.read_csv("/Users/kanyin/Documents/Kanyin/Data Science/Data Projects/2024 Philly Crime/Data/2024_crime full.csv")
df['dispatch_date_time']=pd.to_datetime(df['dispatch_date_time'])
df['date']=df['dispatch_date_time'].dt.date
df['time']=df['dispatch_date_time'].dt.time

#seasonal decomposition
import numpy as np
from statsmodels.tsa.seasonal import seasonal_decompose
dt=df.groupby('date')['text_general_code'].size().reset_index(name='cnt')
##dt.info()
dt['date']=pd.to_datetime(dt['date'])
dt=dt[dt['date'] < '2025-01-01']
dt.set_index('date', inplace=True)

dcmp=seasonal_decompose(dt, model='additive')

fig=dcmp.plot()
fig.set_size_inches((10,6))
fig.tight_layout()
plt.show()

#Dickey-Fuller test for stationary series
from statsmodels.tsa.stattools import adfuller

# Perform Dickey-Fuller test:
adf_test = adfuller(dt['cnt'])

adf_output = pd.Series(adf_test[0:4], index=['Test Statistic', 'p-value', '#Lags Used', 'Number of Observations Used'])
for key, value in adf_test[4].items():
    adf_output['Critical Value (%s)' % key] = value

adf_output


#auto correlation period of 7 chosed because it's daily crime

from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

dt_diff=dt-dt.shift(1) #Regular differencing
dt_szn_diff=dt_diff - dt_diff.shift(7) #Weekly differencing

# drop missing values resulted from differencing
dt_diff.dropna(inplace=True)
dt_szn_diff.dropna(inplace=True)

# Autocorrelation Function and Partial Autocorrelation
fig, (ax1, ax2) = plt.subplots( 2, 1, figsize=(14,12))

plot_acf(dt_szn_diff, ax=ax1)
plot_pacf(dt_szn_diff, ax=ax2, method='ywm')
plt.show()

#SARIMA Model

from statsmodels.tsa.statespace.sarimax import SARIMAX

# Fitting the SARIMA model with initial parameters
sarima_model = SARIMAX(dt, 
                        order=(1, 1, 1), 
                        seasonal_order=(1, 1, 0, 7),
                       
                        enforce_stationarity=False,
                        enforce_invertibility=False)

sarima_result = sarima_model.fit(disp=False)

# Display the summary results of the SARIMA model
sarima_result.summary()

#Plotting the data as well as the forecast

forecast= sarima_result.get_forecast(steps=14) # get the next month
forecast_index=pd.date_range(dt.index[-1] + pd.DateOffset(days=1),periods=14, freq='D')

forecast_mean= forecast.predicted_mean
forecast_conf_int= forecast.conf_int()

plt.figure(figsize=(11,5))


plt.plot(dt.index, dt['cnt'], label='Observed')

plt.plot(forecast_index, forecast_mean, label='Forecast', color='r')

plt.fill_between(forecast_index, forecast_conf_int.iloc[:,0], forecast_conf_int.iloc[:,1], color='pink', alpha=0.4)

plt.title('Philly Crime Forecast')
plt.xlabel('Date')
plt.ylabel('Number of Crimes')
plt.legend()
plt.show()


#Comparison to 2025 so far

df2=pd.read_csv("/Users/kanyin/Documents/Kanyin/Data Science/Data Projects/2024 Philly Crime/Data/2025_crime_toMay.csv")
dt2=df2.groupby('dispatch_date')['text_general_code'].size().reset_index(name='cnt')
dt2=dt2[dt2['dispatch_date'] >= '2024-12-31'] #filtering to only see a few weeks after the end of June
dt2['dispatch_date']=pd.to_datetime(dt2['dispatch_date'])
dt2.set_index('dispatch_date', inplace=True)

# SARIMA for 2025
sarima_model2 = SARIMAX(dt2, 
                        order=(1, 1, 1), 
                        seasonal_order=(1, 1, 0, 7),
                        enforce_stationarity=False,
                        enforce_invertibility=False)

sarima_result2 = sarima_model2.fit(disp=False)

forecast2= sarima_result2.get_forecast(steps=14) # get the next month
forecast_index2=pd.date_range(dt2.index[-1] + pd.DateOffset(days=1),periods=14, freq='D')

forecast_mean2= forecast2.predicted_mean
forecast_conf_int2= forecast2.conf_int()

plt.figure()
plt.plot(dt2.index, dt2['cnt'], label='Observed', color='grey')
plt.title('Extension of Philly Crime Data')


# Comparison of Observed to Actual

forecast= sarima_result.get_forecast(steps=14) # get the next month
forecast_index=pd.date_range(dt.index[-1] + pd.DateOffset(days=1),periods=14, freq='D')

forecast_mean= forecast.predicted_mean
forecast_conf_int= forecast.conf_int()

plt.figure(figsize=(12,4))


plt.plot(dt.index, dt['cnt'], label='Observed')

plt.plot(dt2.index, dt2['cnt'], label='Eventual', color='grey')

plt.plot(forecast_index, forecast_mean, label='Forecast', color='red')

plt.fill_between(forecast_index, forecast_conf_int.iloc[:,0], forecast_conf_int.iloc[:,1], color='pink', alpha=0.3)

plt.title('Philly Crime Forecast')
plt.xlabel('Date')
plt.ylabel('Number of Crimes')
plt.legend()
plt.xlim('2024-10-01','2025-02-05')
plt.show()
