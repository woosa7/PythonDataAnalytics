# 파일 입출력
# 쓰기 모드로 파일 열기
f = open('hello.txt', 'w')
f.close()

with open('hello.txt', 'w', encoding='utf8') as f:
    f.write('Hello, Python')
    f.close()


# ---------------------------------------------------------
# os: 운영체제 관련 기능들을 제공하는 라이브러리

import os
ndir = os.getcwd()
print(ndir)
os.mkdir(ndir + '/text')  # text 라는 폴더를 만든다
os.chdir('text')  # text 폴더로 이동한다

for i in range(1, 101):
    filename = '{}.txt'.format(i)
    f = open(filename, 'w')
    f.close()


# .format : 문자열에서 중괄호 위치에 값을 끼워넣는다

'안녕하세요, 저는 {}입니다'.format('Kate')
'이름: {}, 나이: {}'.format('Kate', 17)
'이름: {name}, 나이: {age}'.format(name='Kate', age=17)


os.listdir()[:10]  # 파일 목록 10개를 확인한다
os.rename('1.txt', '101.txt')  # 1.txt를 101.txt로 바꾼다

# 파일이 있는 확인
'1.txt' in os.listdir()
'101.txt' in os.listdir()

# 모든 파일 이름을 .txt에서 .csv로 바꾸기
for name in os.listdir():
    new_name = name.replace('.txt', '.csv')  # 파일명에서 .txt를 .csv로 찾아바꾼다
    os.rename(name, new_name)

os.listdir()[:10]


# ---------------------------------------------------------
# 정규표현식(Regular Expression) 관련 라이브러리

import re

re.match(r'1', '15.txt')
re.match(r'\d', '15.txt')
re.match(r'\d{1,2}', '15.txt')
re.match(r'\d+', '15.txt')
re.search(r'\d+', 'hello15.csv')
re.sub(r'hello(\d+)', r'\1hello', 'hello15.csv')   # replace

'{:03d}'.format(15)     # 15를 015형식으로
'{:.2f}'.format(1/3)    # 실수를 소수점 2자리까지 표시

for name in os.listdir():
    m = re.match('(\d+).csv', name)          # 파일명이 숫자.csv 형식에 맞는지(match) 검사
    if m:                                    # 맞으면
        num = int(m.group(1))                # 1번째 그룹을 정수(integer)로 변환
        new_name = '{:03d}.csv'.format(num)  # 새 파일명
        os.rename(name, new_name)            # 으로 바꾸기
os.listdir()[:10]
os.remove('002.csv')
'002.csv' in os.listdir()
os.chdir('..')
os.getcwd()
os.getcwd()
import shutil
zipfile = shutil.make_archive('data', 'zip', 'text')  # text 폴더를 data.zip으로 압축
shutil.copy(zipfile, 'data2.zip')  # 압축 파일을 data2.zip으로 복사
shutil.copy2(zipfile, 'data3.zip')  # copy와 같음. 단, 파일의 수정된 날짜를 원본 그대로 유지



