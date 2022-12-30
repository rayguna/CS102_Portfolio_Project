import sorting

def view_criteria(housing, criteria):
    """Let user view the description of the housing dataset

       inputs:
        housing: a list of the housing dataset
        criteria: 'y' or 'n'
    """

    if criteria=='y':
        print(housing.DESCR)
    elif criteria=='n':
        pass
    else:
        print("Please enter 'y' or 'n' to view the available list of housing criteria.")

def select_sorting_column(housing, sort_type):
    """Let user select the sorting column

       inputs:
        housing (list): a list of the housing dataset
        sort_type (str): 'asc' or 'desc'
    """

    sort_col=input("Please select the sorting column from the following, %s:" %housing.feature_names)
    
    if sort_col in housing.feature_names:
        #print(heap_sort(df_housing, sort_col, sort_type))
        #use merge sort
        print(perform_merge_sort(housing, sort_col, sort_type))

    else:
        select_sorting_column(housing, sort_type)

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
        select_sorting_column(housing, sort_type)
    
    elif to_do=='2': #filter
        print("Work in progress...")

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

       inputs: 
        df_data (dataframe): a dataframe input dataset
        col (str): column name which needs to be sorted
        type (str): 'asc' or 'desc'

       output:
        a sorted dataset (list)  
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