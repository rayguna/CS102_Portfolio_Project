"""
Goal:
 -Implement any of the sorting algorithms to sort datasets
 -Implement a search algorithm to filter datasets

refs:
1. heapq: https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/; https://realpython.com/python-heapq-module/
2. map plotting: https://www.bigendiandata.com/2017-06-27-Mapping_in_Jupyter/
3. python sorting library: https://pypi.org/project/sorting/
4. converting latitude and longitude to distance: https://towardsdatascience.com/calculating-distance-between-two-geolocations-in-python-26ad3afe287b?gi=972a94d8e007

To-dos:
*SORTING
 -Use a tuple to label each row and later reconcile the sorted column with the dataframe.
 -Plot only the map of the filtered dataset!

*SEARCHING
 -Select and implement a search algorithm that goes by log(N) to iteratively filter the dataset using multiple criteria. 

12302022
-Added relative distance column w.r.t. average lat and long.
-Looking to add some sort of meaningful distance to create a graph, perhaps to the nearest major city.
-Consider what to do with the graph data structure.
"""

from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
from utils import *




print("Loading dataset... Please wait...")

#load the housing dataset
housing = fetch_california_housing()
#make a dataframe
df_housing=pd.DataFrame(housing.data,columns=housing.feature_names)
#add distance from the first row.
#latitude, longitude
df_housing['rel_distance']=calc_rel_distance(df_housing)


print("""
*************************
*                       *
* WELCOME TO CALIFORNIA *
*                       *
*************************
""")

print("Dataset loading is complete!")
print("Please close the map to proceed.")

#show the housing locations
df_housing.plot(kind="scatter", x="Longitude", y="Latitude",
    s=df_housing['Population']/100, label="Population",
    c="MedInc", cmap=plt.get_cmap("summer"),
    colorbar=True, alpha=0.6, marker='8')
plt.legend()
plt.show()

criteria=input("Welcome to California! Would you like to view the available list of housing criteria (y/n)?")
view_criteria(housing, criteria)

#print(df_housing.head()) #check
select_to_do(housing, df_housing)

