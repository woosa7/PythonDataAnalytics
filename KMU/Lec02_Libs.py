# 유용한 라이브러리

# 설치법 (console 에서)
# 표준적인 Python 패키지 설치 방법
# pip install <pkg_name>

# 데이터 분석에서 자주 쓰이는 패키지의 경우 아나콘다를 이용해 설치하는 쪽이 더 낫다.
# conda install <pkg_name>

# 만약 아나콘다에서 지원하지 않는 패키지 중에 윈도에서 pip로 설치 되지 않는 경우
# Unofficial Windows Binaries for Python Extension Packages에서 다운로드 받음
# pip install <pkg_name.whl>


# --------------------------------------------------------------------
# arrow : Time flies like arrow
# 시간과 관련된 부분을 다루는 라이브러리. 표준 라이브러리 datetime과 호환되면서 사용법이 더 편리하다.
# pip install arrow

import arrow

now = arrow.now() # 현재 시각
now

utcnow = arrow.utcnow()  # 협정표준시(UTC) 현재 시각
utcnow

# 시간 변환
now.to('US/Pacific')
now.to('Asia/Singapore')
now.to('+03:00')
now.to('utc')
utcnow.to('local')

# 시간 문자열 읽기
arrow.get('2016-10-08')
arrow.get('2016-10-08 16:32')

# 시간 정보 수정
a = arrow.get('2016-10-08 16:32')
a.replace(tzinfo='local')  # 시간대를 현지시간으로 변환
a.replace(day=3)  # 날짜를 3일로 수정
a.replace(days=3) # 날짜를 3일 후로 수정
a.replace(days=-3)  # 날짜를 3일 전으로 수정
a.replace(year=2015, months=-1, day=10, hours=3, minute=44)
a.replace(weeks=4)

# 요일
a.weekday()

# 문자로 표시
a.humanize()
a.humanize(locale='ko')

a.format('YYYY년 MM월 DD일 hh시 mm분')
a.format('YY년 M월 D일 h시 m분')

