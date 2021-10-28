import pandas as pd
df = pd.read_csv('Train.csv')

import folium
from folium import plugins

countryArr = df[['y','x']].values

# print(type(countryArr))

m = folium.Map(location=[countryArr[0][0],countryArr[0][1]], zoom_start=12)
m.add_child(plugins.HeatMap(countryArr[:5], radius = 15))
m.save('heatmap.html')
