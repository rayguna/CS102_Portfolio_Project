"""
Goal:
 -Implement heap data structure to sort datasets
 -Implement a search algorithm to filter datasets

refs:
1. heapq: https://www.geeksforgeeks.org/heap-queue-or-heapq-in-python/; https://realpython.com/python-heapq-module/
2. map plotting: https://www.bigendiandata.com/2017-06-27-Mapping_in_Jupyter/

To-dos:
*SORTING
 -Need to know how to properly implement heapq to sort the selected column.
 -Use a tuple to label each row and later reconcile the sorted column with the dataframe.

*SEARCHING
 -Select and implement a search algorithm that goes by log(N) to iteratively filter the dataset using multiple criteria. 
"""

from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt

import heapq


def heap_sort(df_data, col, sort_type='asc'):
    """Turn dataset into a min or max heap.

       inputs: 
        df_data: a dataframe input dataset
        col: column name which needs to be sorted
        type: 'asc' or 'desc'
       output:
        a sorted dataset  
    """
    
    #heapify the selected column
    lst_data=df_data[col].to_list()
    heapq.heapify(lst_data)

    if sort_type=='asc':    
        return lst_data[:20]
    elif sort_type=='desc':
        return lst_data[-20:]
    else:
        print("Please specify a valid sort type ('asc' or 'desc').")



print("Loading dataset... Please wait...")

housing = fetch_california_housing()
#boston = datasets.load_boston()
#make a dataframe

df_housing=pd.DataFrame(housing.data,columns=housing.feature_names)

print("""
*************************
*                       *
* WELCOME TO CALIFORNIA *
*                       *
*************************
""")

print("Dataset loading is complete!")
print("Please close the map to proceed.")

#show the housing location
df_housing.plot(kind="scatter", x="Longitude", y="Latitude",
    s=df_housing['Population']/100, label="Population",
    c="MedInc", cmap=plt.get_cmap("summer"),
    colorbar=True, alpha=0.6, marker='8')
plt.legend()
plt.show()

view_criteria=input("Welcome to Boston! Would you like to view the list of housing criteria (y/n)?")

if view_criteria=='y' or 'Y':
    print(housing.DESCR)

#print(df_housing.head()) #check

def select_sorting_column(sort_type):
    """Let user select the sorting column
    """

    sort_col=input("Please select the sorting column from the following, %s:" %df_housing.columns)
    
    if sort_col in df_housing.columns:
        print(heap_sort(df_housing, sort_col, sort_type))
    else:
        select_sorting_column()

def select_to_do():
    """Let user decide what to do
    """

    to_do=input("What would you like to do? Select from the following: (1) View the top or bottom 20 sorted list, (2) Filter housing data, or (3) View all data.")
    if to_do=='1':
        sort_type=input("How do you want to sort the data ('asc' or 'desc')?")
        select_sorting_column(sort_type)
    
    elif to_do=='2':
        print("Work in progress...")

    elif to_do=='3':
        print("Work in progress...")

    else:
        print("Please enter a valid option: (1) View the top or bottom 20 sorted list, (2) Filter housing data, or (3) View all data.")
        select_to_do()


select_to_do()