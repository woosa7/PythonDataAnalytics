# --------------------------------------------
# Numpy
# --------------------------------------------

import numpy as np

# --------------------------------------------
# Numpy array = R vector

height = [74, 74, 72, 72, 73, 69, 69, 71, 76, 71, 73, 73, 74, 74, 69, 70, 73, 75, 78, 79, 76, 74, 76, 72, 71, 75, 77, 74, 73, 74]
weight = [180, 215, 210, 210, 188, 176, 209, 200, 231, 180, 188, 180, 185, 160, 180, 185, 189, 185, 219, 230, 205, 230, 195, 180, 192, 225, 203, 195, 182, 188]
len(height)
len(weight)

np_height = np.array(height) * 0.0254   # convert inches to meters
np_weight = np.array(weight) * 0.453592 # convert pounds to kg
print(type(np_height))

bmi = np_weight / (np_height ** 2)
print(bmi)

print(bmi[bmi < 21])

print(np_weight[5])
print(np_height[20:30])


# --------------------------------------------
# 2D Numpy Array

baseball = [[74, 180], [74, 215], [72, 210], [72, 210], [73, 188], [69, 176], [69, 209], [71, 200], [76, 231], [71, 180]]
len(baseball)

np_baseball = np.array(baseball)

print(type(np_baseball))
print(np_baseball.shape)

print(np_baseball[9,:])        # 10th row
print(np_baseball[3,0])        # height of 4th player

conversion = np.array([0.0254, 0.453592])   # [height, weight]
print(np_baseball * conversion)

height = np_baseball[:,0]
weight = np_baseball[:,1]

avg = np.mean(height)
med = np.median(height)
stddev = np.std(height)
print("Average: " + str(avg) + " / Median: " + str(med) + " / SD: " + str(stddev))

corr = np.corrcoef(height, weight)
print("Correlation: " + str(corr))

