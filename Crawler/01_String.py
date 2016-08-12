# 특정 문자 갯수
str1 = "Python for Data Analysis"
a = str1.count("a")
print(a)


# 특정 문자 위치
b1 = str1.index("y")
b2 = str1.index("y", 5)     # start index

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
