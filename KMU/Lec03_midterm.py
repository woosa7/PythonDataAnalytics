# 문제 1: 문자열 속 숫자들의 합 구하기

def sum_str(x):
    strings = x.split(sep=',')
    numbers = [int(i) for i in strings]
    sumx = sum(numbers)
    return sumx


print(sum_str('1,7,4,6,2'))


# 문제 2: 설날까지 남은 시간

def until_new_year():
    import arrow
    now = arrow.now('Asia/Seoul')  # 현재 시각
    # now = arrow.get('2016-10-18 10:00').to('Asia/Seoul')
    newyearday = arrow.get('2017-01-30 00:00').to('Asia/Seoul').replace(hours=-9)  # 다음 설날
    days = (newyearday - now).days
    return days


print(until_new_year())


# 문제 3: UserAgentString 분석

def ua_string(x):
    if x.find('AppleWebKit') > 0:
        if x.find('Chrome') > 0:
            ua_gubun = 'C'
        else:
            ua_gubun = 'S'
    elif x.find('Firefox') > 0:
        ua_gubun = 'F'
    else:
        ua_gubun = 'I'

    return ua_gubun


user_agent_1 = 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko'
user_agent_2 = 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)'
user_agent_3 = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
user_agent_4 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A'
user_agent_5 = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1'

print(ua_string(user_agent_1))
print(ua_string(user_agent_2))
print(ua_string(user_agent_3))
print(ua_string(user_agent_4))
print(ua_string(user_agent_5))

# 문제 4: 결측값 제거

import pandas
import numpy


def del_nan_row(df):
    return df.dropna(how='all')


data = pandas.DataFrame({'a': [1, numpy.nan, numpy.nan], 'b': [3, 4, numpy.nan]})
print(data)
print(del_nan_row(data))
