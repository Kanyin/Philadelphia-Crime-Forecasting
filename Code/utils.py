def by_week(df):
    global weekday_crime
    
    """
    Get the average crime for each weekday. 
    !Remember to change 'text_general_code' to the correct data column you want to count.
    
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

def by_month(df):
    global month_crime
    
    """
    Get the average worst day of time by month
    ! Remember to change 'text_general_code' to the correct data column you want to count.
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
