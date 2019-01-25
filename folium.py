# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 15:44:16 2019

@author: user
"""

import folium
import pandas as pd




country_geo = "G:\\Forsk\\day4\\world-countries.json"

data = pd.read_csv("G:\\Forsk\\day4\\indicators.csv")
data.shape

data.head()





# select Life expectancy for females for all countries in 2013
hist_indicator =  'Life expectancy at birth'
hist_year = 2013

mask1 = data['IndicatorName'].str.contains(hist_indicator) 
mask2 = data['Year'].isin([hist_year])


# apply our mask
stage = data[mask1 & mask2]
stage.head()


#Creating a data frame with just the country codes and the values we want plotted.
data_to_plot = stage[['CountryCode','Value']]
data_to_plot.head()


# labelling the legend
hist_indicator = stage.iloc[0]['IndicatorName']




# Setup a folium map at a high-level zoom
map = folium.Map(location=[100, 0], zoom_start=1.5)


# choropleth maps bind Pandas Data Frames and json geometries.
#This allows us to quickly visualize data combinations
map.choropleth(geo_data=country_geo, plot_data=data,
             columns=['CountryCode', 'Value'],
             key_on='feature.id',
             fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.2,
             legend_name=hist_indicator)

map.save('plot_data.html')


# Import the Folium interactive html file
from IPython.display import HTML
HTML('<iframe src=plot_data.html width=700 height=450></iframe>')