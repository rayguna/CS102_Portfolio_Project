#import sorting
import haversine as hs #the output is in km
from haversine import Unit
from random import randint

import pandas as pd

import matplotlib.pyplot as plt



def view_criteria(housing):
    """Let user view the description of the housing dataset

       inputs:
        housing: a list of the housing dataset
        criteria: 'y' or 'n'
    """

    criteria=input("Please enter 'y' or 'n' to view the available list of housing criteria. ")

    if criteria=='y':
        print(housing.DESCR)
    elif criteria=='n': 
        pass
    else:
        view_criteria(housing)

def sort_by_column(housing, sort_type):
    """Let user select the sorting column

       inputs:
        housing (list): a list of the housing dataset
        sort_type (str): 'asc' or 'desc'

       return:
        None
    
       output:
        print the sorted list in a form of a dataframe
    """

    #sort_col=input("Please select the sorting column from the following, %s:" %housing.feature_names)
    
    col_idx=select_column(housing)

    #if sort_col in housing.feature_names:
    
    #print(heap_sort(df_housing, sort_col, sort_type))
    #use merge sort
    #print(perform_merge_sort(housing, sort_col, sort_type))
    #or
    #use quick sort
    #col_idx=housing.feature_names.index(sort_col)

    res=perform_quick_sort(housing.data,col_idx)
    
    if sort_type=='asc': #return first 100 elements of sorted
        res=res[:100]

    elif sort_type=='desc': #return the last 100 elements of reverse sorted
        res=res[:-101:-1]

    #convert result to dataframe for easy viewing
    df_sorted_housing=pd.DataFrame(res, columns=housing.feature_names)
    print(df_sorted_housing.to_string()) #show all 100 elements


def view_all_data(df_housing, no_rows):
    """View all of the housing data for a specified number of rows

       inputs:
        df_housing (dataframe): pandas dataframe of housing dataset
        no_rows (int): no or rows to display
    """

    if (no_rows.isnumeric()) and (int(no_rows)<len(df_housing.index)):
        print(df_housing.head(int(no_rows)).to_string())
    else:
        print("Please enter a valid number.")
        view_all_data(no_rows)

def select_column(housing):
    """Recursively ask user to select a valid column
    
       Inputs:
        housing (obj): the california housing dataset object
        col_name (str): any of the columns names within housing.data

       Outputs:
        col_idx (int): index number corresponding to the valid, selected column. 
    """

    sort_col=input("Please select the sorting column from the following, %s:" %housing.feature_names)

    if sort_col in housing.feature_names:
        
        col_idx=housing.feature_names.index(sort_col)
        return col_idx

    else:
        select_column(housing)


def select_to_do(housing, df_housing):
    """Let user decide what to do

       inputs: 
        housing (2d list): a 2d array of housing data
        df_housing (dataframe): a dataframe of housing data

       output: 
        None
    """

    to_do=input("What would you like to do? Select from the following: (1) View the top or bottom 20 sorted list, (2) Filter housing data, or (3) View all data. Otherwise, press 'q' to quit, or press 'v' to view the available list of housing criteria.")
    if to_do=='1':#sort by column
        sort_type=input("How do you want to sort the data ('asc' or 'desc')?")
        sort_by_column(housing, sort_type)
    
    elif to_do=='2': #filtering
        
        try:
            lst_housing=housing.data        
            col_idx=select_column(housing)

            print("CHECK INDEX")
            print(col_idx)

            #get min and max limits
            min_limit=min(df_housing.iloc[:,col_idx])
            max_limit=max(df_housing.iloc[:,col_idx])

            #must convert from string input to float
            get_min=float(input("Please enter the minimum value between %s and %s: " %(min_limit, max_limit)))
            get_max=float(input("Please enter the maximum value between %s and %s: " %(min_limit, max_limit)))

            lst_filtered_housing_data=filter_data_by_one_criteria(lst_housing, col_idx, get_min, get_max) #a list of filtered data
            #print(lst_filtered_housing_data)

            #print into a dataframe for easy viewing
            df_filtered_housing_data=pd.DataFrame(lst_filtered_housing_data, columns=housing.feature_names)
            print(df_filtered_housing_data.to_string()) #display all data

            #show the housing locations
            df_filtered_housing_data.plot(kind="scatter", x="Longitude", y="Latitude",
                s=df_filtered_housing_data['Population']/100, label="Population",
                c="MedInc", cmap=plt.get_cmap("summer"),
                colorbar=True, alpha=0.6, marker='8')
            plt.legend()
            plt.show()

        except:
            print("Error plotting data. Please try again.")

        
    elif to_do=='3': #view x rows of data
        no_rows=input("How many rows of data would you like to view?")
        view_all_data(df_housing, no_rows)

    elif to_do=='q':
        return

    elif to_do=='v':
        view_criteria('y')

    else:
        print("Please enter a valid option: (1) View the top or bottom 20 sorted list, (2) Filter housing data, or (3) View all data.")
        select_to_do(housing, df_housing)

    #repeat the question until the user press q to quit.
    select_to_do(housing, df_housing)

def perform_merge_sort(housing, col, sort_type='asc'):
    """Turn dataset into a min or max heap. 
        --- Currently not being used. Using perform_quick_sort instead. 

       Limitation: Only perform sorting of a 1D array.
                   For sorting a 2d array, use the perform_quick_sort function instead.

       inputs: 
        housing (obj): the housing dataset object
        col (str): column name which needs to be sorted
        type (str): 'asc' or 'desc'

       output:
        a sorted dataset (list)  

       *This function is currently not being used because it only works with a 1d array input.
         The housing dataset is a 2d array.
    """

    #sort use sorting library
    #use lambda function of the form (lambda x: sortingmerge(arraylist derived from x))(x)
    idx=housing.feature_names.index(col)
    lst_sorted_data=(lambda x: sorting.merge([i[idx] for i in x]))(housing.data)

    if sort_type=='asc': #sort forward    
        return lst_sorted_data[:25]
    elif sort_type=='desc': #sort backward
        return lst_sorted_data[:-26:-1]
    else:
        print("Please specify a valid sort type ('asc' or 'desc').")

def calc_rel_distance(df_housing):
    """Convert two locations to a relative distance in miles

       input: 
        loc1 (tuple of floats): (lat1, long1) 
        loc2 (tuple of floats): (lat1, long1)
    """

    avg_lat_long=(df_housing.Latitude.mean(), df_housing.Longitude.mean()) #the average latitude and longitude
    df_rel_dist=df_housing.apply(lambda x: hs.haversine((x.Latitude, x.Longitude),(avg_lat_long), unit=Unit.MILES), axis=1)
    
    return df_rel_dist 


def perform_quick_sort(lst_housing, col_idx):
    """Perform a quick sort on a 2d array on selected index of the sub-array.

       input:
        lst_housing (2d array): the california housing data, housing.data.
        col_idx (int): housing dataset column index 

       output:
        lst_res (2d array): a sorted 2d list.
    """

    #return the result if the input array contains fewer than two elements
    if len(lst_housing) < 2:
        return lst_housing

    lst_low, lst_same, lst_high = [], [], []

    #Randomly select the pivot element
    pivot = lst_housing[randint(0, len(lst_housing) - 1)]

    for item in lst_housing:
        #compare element corresponding to col_idx
        
        # low list: elements < pivot
        if item[col_idx] < pivot[col_idx]:
            lst_low.append(item)
        # same list: elements=pivot
        elif item[col_idx] == pivot[col_idx]:
            lst_same.append(item)
        # high list: elements > pivot 
        elif item[col_idx] > pivot[col_idx]:
            lst_high.append(item)

    # res: combine sorted low list with same and high list
    # no need to specify the sorted_type
    lst_res=perform_quick_sort(lst_low, col_idx) + lst_same + perform_quick_sort(lst_high, col_idx)
    return lst_res


def perform_binary_search(lst_sorted_housing, col_idx, low, high, search_value):
    """Perform a binary search on a sorted list

       Inputs:
        lst_sorted_housing (2d array):
        col_idx (int): column index of the lst_sorted_housing data
        search_value (int): the value to search which can be a min or a max 

       Output:
        idx (int): The index of the first value that satisfies the search value.

       Issue:
        There are multiple indices having the search value and you need to include all of it.
        Binary search only finds one of the many recurring values in the list.

       Solution:
        Accomodated this issue by doing a linear search along the solution - see the end of 
         filter_data_by_one_criteria() function.
    """

    # Base case
    if high >= low:
        mid = (high + low) // 2

        # Element present at the middle
        if lst_sorted_housing[mid][col_idx] == search_value:
            return mid
        # Element < mid in left subarray
        elif lst_sorted_housing[mid][col_idx] > search_value:
            return perform_binary_search(lst_sorted_housing, col_idx, low, mid - 1, search_value)
        # Element > mid in right subarray
        else:
            return perform_binary_search(lst_sorted_housing, col_idx, mid + 1, high, search_value)

    else:
        # Element not found
        return -1


def filter_data_by_one_criteria(lst_housing, col_idx, min_val, max_val):
    """Filter a 2d array by col_idx column to yield values between min and max
       Approach: 
        First, sort the dat by col_idx.
        Next, perform a binary search.
    
       Inputs:
        lst_housing (2d array): the housing dataset.
        col_idx (int): the housing dataset column index
        min_val (int): minimum value
        max_val (int): maximum value

       Output:
        lst_res (2d array): a filtered 2d list  
    """

    #first, sort the data by col_idx
    lst_sorted_housing=perform_quick_sort(lst_housing, col_idx)
    #second, use a binary search to find the first value > min
    # and to find the first value > max.
    min_idx=perform_binary_search(lst_sorted_housing, col_idx, 0, len(lst_sorted_housing)-1, min_val) #lst_sorted_housing, col_idx, low, high, search_value
    max_idx=perform_binary_search(lst_sorted_housing, col_idx, 0, len(lst_sorted_housing)-1, max_val)

    #update to the actual min_idx and max_idx values. 
    #find the first min_idx because binary search randomly finds one of the multiples occurrence of the search_value 
    
    track_min_idx=min_idx
    track_max_idx=max_idx

    for item in lst_sorted_housing[min_idx::-1]: #traverse in reverse
        if item[col_idx]==min_val:
            track_min_idx-=1
        else: #stop tracking
            break
    
    #find the last max_idx because binary search randomly finds one of the multiples occurrence of the search_value
    for item in lst_sorted_housing[max_idx:]: #traverse in reverse
        if item[col_idx]==max_val:
            track_max_idx+=1
        else: #stop tracking
            break
    

    lst_filtered_housing_data=lst_sorted_housing[track_min_idx:track_max_idx]
    return lst_filtered_housing_data 