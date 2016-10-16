# List

# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas = [hall, kit, liv, bed, bath]
print(areas)
print(areas[1])
print(areas[-3])       # 뒤에서 3번째

areas.index(20.0)
areas.count(9.50)
areas.append(24.5)
areas.append(15.45)

sorted(areas)

areas.reverse()     # Reverse the orders of the elements in list
print(areas)

# lists in list
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv],
         ["bedroom", bed],
         ["bathroom", bath]]
print(house)
print(house[2][0])

house = house + [["rooftop", 22.34]]
print(house[:3])
print(house[4:])

del(house[5])


# -----------------------------------------------
# String Methods
room = "poolhouse"
room.upper( )
room.count('o')


# -----------------------------------------------
# import packages
import math

r = 0.43
C = 2*math.pi*r
A = math.pi*r**2
print("Circumference: " + str(C))
print("Area: " + str(A))

from math import radians

r = 192500              # 지름
dist = r * radians(12)  # 12도 이동한 거리
print(dist)

