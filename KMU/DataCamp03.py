# --------------------------------------------
# Dictionary
# --------------------------------------------

europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo', 'australia':'vienna'}

print(europe.keys())
print(europe['norway'])

europe['italy'] = 'rome'    # add or update
europe['poland'] = 'warsaw'

del(europe['australia'])    # Remove

print('italy' in europe)
print(europe)               # 순서는 고정 안됨


# Dictionary of dictionaries

europe = {'spain': {'capital':'madrid', 'population':46.77},
          'france': {'capital':'paris', 'population':66.03},
          'germany': {'capital':'berlin', 'population':80.62},
          'norway': {'capital':'oslo', 'population':5.084}}

print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital':'rome', 'population':59.83}
europe['italy'] = data

print(europe)


# --------------------------------------------
# Pandas
# --------------------------------------------

import pandas as pd

names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

my_dict = {
    'country':names,
    'drives_right':dr,
    'cars_per_cap':cpc
}

# Build a DataFrame
cars = pd.DataFrame(my_dict)
cars.index = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

print(cars)

# data import from csv
cars = pd.read_csv('cars.csv', index_col = 0)

print(cars)

print(cars["country"])      # output as Pandas Series

print(cars[["country"]])    # output as Pandas DataFrame
print(cars[["country", "drives_right"]])

# loc & iloc
print(cars.loc[['RU', 'AUS']])
print(cars.iloc[[4, 1]])

print(cars.loc['MOR', 'drives_right'])

print(cars.loc[['RU','MOR'], ['country', 'drives_right']])  # sub-DataFrame














