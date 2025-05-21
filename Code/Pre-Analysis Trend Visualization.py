#Observed weekly and monthly patterns of Philly Crime data in 2024

import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime
import pandas as pd
df=pd.read_csv("/Users/kanyin/Documents/Kanyin/Data Science/Data Projects/2024 Philly Crime/Data/2024_crime full.csv")
#df=df[df['dispatch_date'] < '2024-07-05']
df['dispatch_date_time']=pd.to_datetime(df['dispatch_date_time'])
df['date']=df['dispatch_date_time'].dt.date
df['time']=df['dispatch_date_time'].dt.time

df.info()
pltdata=df.groupby('dispatch_date')['text_general_code'].size().reset_index(name='cnt')
pltdata['dispatch_date']=pd.to_datetime(pltdata['dispatch_date'])
pltdata.set_index('dispatch_date', inplace=True) #using inplace, modify the dataframe correctly
plt.plot(pltdata, color='green')
plt.title('Philadelphia Crimes (Jan to July 2024)')
plt.xlabel('Date')
plt.ylabel('No. of Crimes')

#What day is the worst weekday for crime in 2024?

def by_week(df):
    global weekday_crime
    
    """
    Get the average worst day of time by weekday
    
    Argments:
    `df`: the dataframe
    
    Output:
    `weekday_crime`: grouped series of weekday
    """
    med=df.groupby('date')['text_general_code'].size().reset_index(name='cnt')
    med['date']=pd.to_datetime(med['date'])
    med['weekday'] = med['date'].dt.day_name()
    weekday_crime=med.groupby('weekday')['cnt'].mean().reindex(['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'])
    
    return weekday_crime

by_week(df)
weekday_crime.plot()
plt.title("Average Philadelphia Crime Throughout the Week")
plt.ylabel("Average Daily Crime")
plt.xlabel("Weekday")


def by_month(df):
    global month_crime
    
    """
    Get the average worst day of time by month
    
    Argments:
    `df`: the dataframe
    
    Output:
    `weekday_crime`: grouped series of month
    """
    med=df.groupby('date')['text_general_code'].size().reset_index(name='cnt')
    med['month'] = pd.to_datetime(med['date']).dt.month_name()
    month_crime=med.groupby('month')['cnt'].mean().reindex(['January','February','March','April','May','June','July', 'August',
                                                           'September','October','November','December'])
    
    return month_crime

by_month(df)
month_crime.plot(figsize=(10,4), color='pink')
plt.title("Average Philadelphia Crime By Months")
plt.ylabel("Average Monthly Crime")
plt.xlabel("Month")
