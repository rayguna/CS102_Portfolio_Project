from sklearn import datasets
import pandas as pd

boston = datasets.load_boston()
#make a dataframe
df_boston=pd.DataFrame(boston.data,columns=boston.feature_names)

view_criteria=input("Welcome to Boston! Would you like to view the list of housing criteria (y/n)?")

if view_criteria=='y' or 'Y':
    print(boston.DESCR)

print(df_boston.CRIM)