# --------------------------------------------
# Loop
# --------------------------------------------

areas = [11.25, 18.0, 20.0, 10.75, 9.50]

for ar in areas :
    print(ar)


# Change for loop to use enumerate()

for index, a in enumerate(areas) :
    print("room " + str(index + 1) + " : " + str(a))



# Loop over list of lists

house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]

for room in house:
    print("the " + room[0] + " is " + str(room[1]) + " sqm")


# Loop over dictionary

europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn', 'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'australia':'vienna'}

for key, value in europe.items():
    print("the capital of " + key.upper() + " is " + value)



# Loop over Numpy array

import numpy as np

height = [74, 79, 72, 77, 73, 69, 67, 71, 76]
np_height = np.array(height)

for x in np_height :                # 1D array
    print(str(x) + " inches")


baseball = [[74, 180], [74, 215], [72, 210], [72, 210], [73, 188], [69, 176]]
np_baseball = np.array(baseball)

for x in np.nditer(np_baseball) :   # 2D array
    print(x)



# Loop over DataFrame

import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

for lab, row in cars.iterrows() :
    print(lab + ' ------------------------')
    print(row['country'] + " : " + str(row['cars_per_cap']))

# adds COUNTRY column
for lab, row in cars.iterrows() :
    cars.loc[lab, 'COUNTRY'] = row['country'].upper()

print(cars)



# --------------------------------------------
# Case Study: Hacker Statistics
# --------------------------------------------




