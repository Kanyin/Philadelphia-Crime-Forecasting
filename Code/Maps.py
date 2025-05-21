#Spatial Visualization of Crime in Philly January to July 2024


import matplotlib.pyplot as plt
import pandas as pd
import numpy as n
import plotly as px
import plotly.express as p
import pandas as pd

df=pd.read_csv("/Users/kanyin/Documents/Kanyin/Data Science/Data Projects/2024 Philly Crime/Data/2024_crime full.csv")
df["lat"]=df["lat"].astype(float)
df["lng"]=df["lng"].astype(float)
df.head()


def repl_strng(df, column, strng_pairs):
    '''
    In order to combine similar categories, 
    finds and replaces strings in a dataframe column.

    Args:
    df : the data frame
    column : the column to be modified
    strng_pairs: dictionary of keys to find
    '''
    df[column] = df[column].replace(strng_pairs, regex=False)
    return df
df2=df
df2['org_code']=df2['text_general_code']
thft={'Theft from Vehicle':'Theft', 'Thefts':'Theft'}
brg={'Burglary Residential':'Burglary', 'Burglary Non-Residential':'Burglary'}
sx={'Rape':'Sexual Offense', "Other Sex Offenses (Not Commercialized)":'Sexual Offense'}
hm= {"Homicide - Justifiable":"Homicide","Homicide - Criminal":"Homicide"}
rb= {"Robbery Firearm": "Robbery", "Robbery No Firearm":"Robbery"}
aslt={"Aggravated Assault No Firearm": "Assault", "Aggravated Assault Firearm":"Assault", "Other Assaults":"Assault",
     "Aggravated Assault":"Assault"}
df2=repl_strng(df2, 'text_general_code', thft)
df2=repl_strng(df2, 'text_general_code', brg)
df2=repl_strng(df2, 'text_general_code', sx)
df2=repl_strng(df2, 'text_general_code', hm)
df2=repl_strng(df2, 'text_general_code', rb)
df2=repl_strng(df2, 'text_general_code', aslt)

df2=df2[~df2['text_general_code'].isin(['Gambling Violations','Liquor Law Violations', 'Vagrancy/Loitering', 'Embezzlement',
                                       'All Other Offenses'])] #removing categories that are not as prominent

daily=df.groupby(["dispatch_date","text_general_code"],as_index=False).size().reset_index(names="cnt")
daily
blck=df2.groupby(["text_general_code",'location_block']).size().reset_index(name="cnt") #how many of each crime in each block
loc=df2.groupby(["text_general_code", "location_block"], as_index=True)[['lat','lng']].mean() #the average of their location for each block
dftwo=pd.merge(blck, loc, on=['text_general_code', 'location_block'], how='right')
dftwo #a data frame showing how many of each crime happened within each block
dftwo=dftwo[['lat','lng','cnt','text_general_code','location_block']] #rearrange




#### a visual map of crime in Philly

fig = p.scatter_map(dftwo,
                     lat="lat",
                     lon="lng",
                     color="text_general_code", # Use a categorical variable for colors
                     hover_name="text_general_code",
                     hover_data=["location_block","text_general_code"], # Display details on hover
                     size="cnt", # Use incident type to determine marker siz,
                     color_continuous_scale=p.colors.cyclical.IceFire,
                     zoom=12, # Set the zoom level
                     center=dict(lat=39.95233, lon=-75.16379)) # Center the map

fig.show()

# A spatial heatmap although these are now out of style 

df3=dftwo[['lat','lng','cnt']]
from folium.plugins import HeatMap, HeatMapWithTime
hm = folium.Map(location=(39.95233, -75.16379),zoom_start=11.5,
               tiles="Cartodb Positron")

HeatMap(df3, 
        min_opacity=0.4,
        blur = 30, size=.01
               ).add_to(folium.FeatureGroup(name='Heat Map').add_to(hm))
folium.LayerControl().add_to(hm)

hm

###

wt=df.groupby(['lat', 'lng', 'dispatch_date'])['text_general_code'].size().reset_index(name='cnt')
wt

time=list(wt['dispatch_date'].sort_values().astype('str').unique())
wt['dispatch_date']=wt['dispatch_date'].sort_values(ascending=True)
ovrtime=[]
for _, date in wt.groupby('dispatch_date'):
    ovrtime.append([[row['lat'], row['lng'], row['cnt']] for _, row in date.iterrows()])

hmwt = folium.Map(location=(39.95233, -75.16379),zoom_start=11.5,
               tiles="OpenStreetMap")

HeatMapWithTime(ovrtime,
                index=time,
                auto_play=False,
                use_local_extrema=True).add_to(hmwt)
hmwt

