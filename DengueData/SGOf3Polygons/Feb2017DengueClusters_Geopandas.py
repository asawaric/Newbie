import matplotlib.pyplot as plt
import pandas as pd
from geopandas import GeoDataFrame
from shapely.geometry import Point

Coords3 = pd.read_csv('/home/asawari/Desktop/Lab/DengueData/SGof3polygons/coords3.csv')
Coords2 = pd.read_csv('/home/asawari/Desktop/Lab/DengueData/SGof3polygons/coords2.csv')
Coords1 = pd.read_csv('/home/asawari/Desktop/Lab/DengueData/SGof3polygons/coords1.csv')

# SG mainland polygon1
crs = {'init': 'epsg:4326'}
geometry = [Point(xy) for xy in zip(Coords1.Longitude, Coords1.Latitude)]
Coords1 = Coords1.drop(['Longitude', 'Latitude'], axis=1)
geo_df = GeoDataFrame(Coords1, crs=crs, geometry=geometry)

# SG polygon2
Coords2 = pd.read_csv('/home/asawari/Desktop/Lab/DengueData/SGof3polygons/coords2.csv')
geometry = [Point(xy) for xy in zip(Coords2.Longitude, Coords2.Latitude)]
Coords2 = Coords2.drop(['Longitude', 'Latitude'], axis=1)
geo_df2 = GeoDataFrame(Coords2, crs=crs, geometry=geometry)

# SG polygon3
Coords3 = pd.read_csv('/home/asawari/Desktop/Lab/DengueData/SGof3polygons/coords3.csv')
geometry = [Point(xy) for xy in zip(Coords3.Longitude, Coords3.Latitude)]
Coords3 = Coords3.drop(['Longitude', 'Latitude'], axis=1)
geo_df3 = GeoDataFrame(Coords3, crs=crs, geometry=geometry)

# Dengue clusters in Feb 2017.
DC = pd.read_csv('/home/asawari/Desktop/Lab/DengueData/GeocodeswithDate_Feb2017.csv')
geometry = [Point(xy) for xy in zip(DC.Longitude, DC.Latitude)]
DC = DC.drop(['Longitude', 'Latitude'], axis=1)
geo_DC = GeoDataFrame(DC, crs=crs, geometry=geometry)

#plot all the graphs
ax = geo_df.plot(color='b')
geo_df2.plot(color='g', ax=ax)
geo_df3.plot(color='r', ax=ax)
geo_DC.plot(color='black', ax=ax)
plt.title('Dengue Clusters in Feb2017')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
#plt.show()
plt.savefig('Feb2017DengueClusters2.png')
