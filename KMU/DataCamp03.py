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

print(cars[1:4])

print(cars["country"])      # output as Pandas Series
print(cars[["country"]])    # output as Pandas DataFrame
print(cars[["country", "drives_right"]])

# loc & iloc
print(cars.loc[['RU', 'AUS']])
print(cars.iloc[[4, 1]])

print(cars.loc['MOR', 'drives_right'])
print(cars.loc[['RU','MOR'], ['country', 'drives_right']])  # sub-DataFrame

print(cars.loc[:, 'drives_right'])      # Series
print(cars.loc[:, ['drives_right']])    # DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])


# Filtering pandas dataframe
print( cars[cars['drives_right'] == True] )

many_cars = cars["cars_per_cap"] > 500
print( cars[many_cars] )


# --------------------------------------------
# Pandas Grouping
# --------------------------------------------
import numpy as np

car = pd.read_csv('automobile.csv')

print(car.shape)
print(car.head())

car.loc[car.wheels == '4wd']

# symboling : 차량 안전등급 지수
print( car.loc[car.wheels == '4wd', 'symboling'] )

a1 = car.loc[car.wheels == '4wd', 'symboling'].mean()
a2 = car.loc[car.wheels == 'fwd', 'symboling'].mean()

print(a1);print(a2)


# Grouping

grouped = car.groupby('wheels')

print( grouped.get_group('4wd') )

print( grouped['symboling'].mean() )


# aggregation

print( grouped['symboling'].agg([np.mean, np.sum]) )
print( grouped['symboling'].agg({'평균': np.mean, '합계': np.sum}) )


# Ordered Dictionary

from collections import OrderedDict

d = OrderedDict([('평균', np.mean), ('합계', np.sum)])
print(d)
print(d['평균'])

grouped['symboling'].agg(OrderedDict([('평균', np.mean), ('합계', np.sum)]))

