### The Housing Dataset Recommendation System

#### TOC

1. [About the Project](# 1)
2. [The Recommendation System](# 2)
3. [Conclusions](# 3)

***

#### <a name="1"> 1. About the Project</a>

This project uses the open-source housing dataset that can be loaded from the scikitlearn python library as follows:

```
from sklearn.datasets import fetch_california_housing
import pandas as pd

housing = fetch_california_housing()
```

To view the description of the dataset, type:

```
print(housing.DESCR)
```

The output is as follows:

.. _california_housing_dataset:

California Housing dataset
--------------------------

**Data Set Characteristics:**

    :Number of Instances: 20640
    
    :Number of Attributes: 8 numeric, predictive attributes and the target
    
    :Attribute Information:
        - MedInc        median income in block group
        - HouseAge      median house age in block group
        - AveRooms      average number of rooms per household
        - AveBedrms     average number of bedrooms per household
        - Population    block group population
        - AveOccup      average number of household members
        - Latitude      block group latitude
        - Longitude     block group longitude
    
    :Missing Attribute Values: None

This dataset was obtained from the StatLib repository.
https://www.dcc.fc.up.pt/~ltorgo/Regression/cal_housing.html

The target variable is the median house value for California districts,
expressed in hundreds of thousands of dollars ($100,000).

This dataset was derived from the 1990 U.S. census, using one row per census
block group. A block group is the smallest geographical unit for which the U.S.
Census Bureau publishes sample data (a block group typically has a population
of 600 to 3,000 people).

An household is a group of people residing within a home. Since the average
number of rooms and bedrooms in this dataset are provided per household, these
columns may take surpinsingly large values for block groups with few households
and many empty houses, such as vacation resorts.

It can be downloaded/loaded using the
:func:`sklearn.datasets.fetch_california_housing` function.

.. topic:: References

    - Pace, R. Kelley and Ronald Barry, Sparse Spatial Autoregressions,
      Statistics and Probability Letters, 33 (1997) 291-297

#### <a name="2"> 2. The Recommendation System </a>

---Work in progress

#### <a name="3"> 3. Conclusions </a>

---Work in progress

***
