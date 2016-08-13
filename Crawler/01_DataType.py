"""
01 DataTypes
"""

# --- String ---

# 특정 문자 갯수
str1 = 'Python for Data Analysis'
a = str1.count('a')
print(a)

# 특정 문자 위치
b1 = str1.index('y')
b2 = str1.index('y', 5)     # start index

print(b1)
print(b2)

# 좌우 공백 제거
str1.strip()
str1.lstrip()
str1.rstrip()

# 문자열 바꾸기
str1.replace("a", "x")
str1.replace("a", "x", 2)   # max

# 문자열 나누기
c1 = str1.split(" ")
c2 = str1.split(" ", 2)     # split count

print(c1)
print(c2)



# --- List / Tuple ---

# List : 데이터 추가, 삭제 가능
# Tuple : 생성된 후 내용 변경 불가능

# 리스트에 데이터 추가 삭제
list1 = [1, "Data Science", 100, 9]

list1.insert(1, "R")
list1.append(99)

del list1[1]
list1.remove(100)

# 정렬
list2 = [828, 71, 92, 682, 38, 7, 45]
list2.sort()
list2.reverse()

# list in list
list3 = ["p", "y", "t", "h", ["q", "u"], "o", "n"]

a = list3[4]
b = list3[4][1]


# --- Dictionary(Map) ---

girl = {'hobby':'python', 'fruit':'orange', 'sports':'swim'}    # key : value

girl['sports']
girl['phone'] = 'iPhone7'       # add
girl['hobby'] = 'reading book'  # modify

print(girl)

print('phone' in girl)      # 존재여부

# Set : dictionary 에서 value 제외하고 key 만 가지고 있음
sg = set(girl)
print(sg)


