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
# Case Study: Hacker Statistics. Normal Distribution
# --------------------------------------------

import numpy as np

np.random.seed(1234)

print(np.random.rand())             # random float

print(np.random.randint(1, 7))      # random int


# Random Walk
all_walks = []
for i in range(1000) :
    random_walk = [0]

    for x in range(100) :
        # Set step : last element in random_walk
        step = random_walk[-1]

        # Roll the dice
        dice = np.random.randint(1,7)

        # Determine next step
        if dice <= 2:
            step = max(0, step - 1)     # 음수값 되면 0 리턴
        elif dice <= 5:
            step += 1
        else:
            step += np.random.randint(1, 7)

        # append next_step to random_walk
        random_walk.append(step)
    all_walks.append(random_walk)

# Print
np_all_walks = np.array(all_walks)
np_aw_t = np.transpose(np_all_walks)
print(np_aw_t)

# Plot
import matplotlib.pyplot as plt
plt.plot(np_aw_t)
plt.show()

# select last row - check normal distribution
ends = np_aw_t[-1]
print(ends)
plt.hist(ends)
plt.show()

