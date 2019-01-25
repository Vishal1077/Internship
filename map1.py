# -*- coding: utf-8 -*-
"""
Created on Tue Jan 15 11:26:51 2019

@author: user
"""


import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd



# set the filepath and load in a shapefile
fp = "G:\\Forsk\\day3\\District_Boundary.shp"
map_df = gpd.read_file(fp)


# check data type so we can see that this is not a normal dataframe, but a GEOdataframe
map_df.head()


map_df.plot()

df = pd.read_csv("G:\\Forsk\\day3\\District_Boundary.xlsx", header=0)
df.head()

df = df[['Area_name','Happiness_score_2011-14_(out_of_10)', 'Anxiety_score_2011-14_(out_of_10)', 'Population_density_(per_hectare)_2017', 'Mortality_rate_from_causes_considered_preventable_2012/14']]

data_for_map = df.rename(index=str, columns={'Happiness_score_2011-14_(out_of_10)': "happiness",
"Anxiety_score_2011–14_(out_of_10)": "anxiety",
"Population_density_(per_hectare)_2017": "pop_density_per_hectare",
"Mortality_rate_from_causes_considered_preventable_2012/14": 'mortality'})
# check dat dataframe
data_for_map.head()


# join the geodataframe with the cleaned up csv dataframe
merged = map_df.set_index('NAME').join(data_for_map.set_index('Area_name'))
merged.head()



# set a variable that will call whatever column we want to visualise on the map
variable = 'pop_density_per_hectare'
# set the range for the choropleth
vmin, vmax = 120, 220
# create figure and axes for Matplotlib
fig, ax = plt.subplots(1, figsize=(10, 6))




# create map
merged.plot(column=variable, cmap='Blues', linewidth=0.8, ax=ax, edgecolor='0.8')





# remove the axis
ax.axis('off')



# add a title
ax.set_title('Preventable death rate in London', fontdict={'fontsize': '25', 'fontweight' : '3'})
# create an annotation for the data source
ax.annotate('Source: London Datastore,2014',xy=(0.1, .08),
            xycoords='figure fraction',
            horizontalalignment='left',
            verticalalignment='top',
            fontsize=12, color='#555555')
            
            
            
            
# Create colorbar as a legend
sm = plt.cm.ScalarMappable(cmap='Blues', norm=plt.Normalize(vmin=vmin, vmax=vmax))
# empty array for the data range
sm._A = []
# add the colorbar to the figure
cbar = fig.colorbar(sm)




fig.savefig("map_export.png", dpi=300)            