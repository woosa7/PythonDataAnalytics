#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# stock_dart.py

import os
import os.path
import time
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import requests
import os.path
import mysql.connector
from sqlalchemy import create_engine

# pwd=input('Enter Password for server:')
pwd = 'finda888'

def mkdir_sure(filename):
    folder=os.path.dirname(filename)
    if not os.path.exists(folder):
        os.makedirs(folder)
        
        
def wget(url, to=None):
    '''날짜별 공시리스트 html을 로컬 파일로 저장'''
    headers = {'Cookie':'DSAC001_MAXRESULTS=10000;'}
    local_filename = url.split('/')[-1]
    if to:
        local_filename = to
    r = requests.get(url, headers=headers, stream=True)
    f = open(local_filename, 'wb')
    for chunk in r.iter_content(chunk_size=1024): 
        if chunk:
            f.write(chunk)
            f.flush()
    return local_filename
    
    
def find_between(s, first, last):
    '''저장한 공시리스트 html에 오류가 있는지 확인'''
    try:
        start = s.rfind(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ''
        

def dart_html_to_db(fn, last_datetime, reqdate, con):
    '''
    * fn: HTML 파일명
    * last_datetime: 최종 저장된 리포트의 시간
    * con: DB커넥션
    '''

    with open(fn, encoding='utf8') as f:
        text = f.read()

    soup = BeautifulSoup(text, "lxml")

    sel_list = soup.select('div p b')
    counts = 0
    count_str = sel_list[0].text
    count_str = "".join(count_str.split())
    if not '페이지에오류' in count_str:
        count_str = find_between(count_str, '전체', '건')
        counts = int(count_str.replace(',', ''))

    insert_counts = 0
    if counts > 0:
        table = soup.select('div table')[0]
        trs = table.findAll('tr')
        for tr in trs[1:]:
            tds = tr.findAll('td')
            time = tds[0].text.strip()
            corp_name = tds[1].text.strip()                     # 공시대상회사
            market = tds[1].img['alt']                          # 시장구분
            title = " ".join(tds[2].text.split())               # 제목
            link = 'http://dart.fss.or.kr' + tds[2].a['href']   # 링크
            reporter = tds[3].text.strip()                      # 제출자
            date = tds[4].text.strip().replace('.', '-')
            date += ' ' + time                                  # 접수일
            doc_id = link.split('main.do?rcpNo=')[1]            # 공시번호
            
            date = datetime.strptime(date, '%Y-%m-%d %H:%M')
            last_datetime

            insert_sql = '''insert into stock_dart
                (doc_id, date, corp_name, market, title, link, reporter, postdate)
                values (%s,%s,%s,%s,%s,%s,%s,%s)
                on duplicate key update
                    doc_id = values(doc_id),
                    date = values(date),
                    postdate = values(postdate)
            '''
            # insert_sql = '''insert into stock_dart
            #     (doc_id, date, corp_name, market, title, link, reporter, postdate)
            #     values (%s,%s,%s,%s,%s,%s,%s,%s)
            # '''

            #if date > last_datetime:
            con.execute(insert_sql, (doc_id, date, corp_name, market, title, link, reporter, reqdate))
            insert_counts += 1
            print("%s %s, '%s'" % (reqdate, corp_name, title))
    return insert_counts
    
if __name__ == "__main__":

    # stock_dart 테이블 생성
    # create_table_sql = '''
    # create table if not exists stock_dart (
    #     `doc_id` varchar(25) not null unique,
    #     `date` datetime,
    #     `postdate` datetime,      # 접수일과 공시날짜가 다른 것이 많기 때문에 공시일 기준 request.
    #     `corp_name` varchar(50),
    #     `market` varchar(50),
    #     `title` varchar(255),
    #     `link` varchar(128),
    #     `reporter` varchar(50)
    # );
    # '''

    cnx_str = 'mysql+mysqlconnector://woosa7:'+pwd+'@localhost/findb'
    engine = create_engine(cnx_str, echo=False)
    con = engine.connect()
    
    # create table if not exists
    # con.execute(create_table_sql)

    # DB의 마지막 저장일(공시일자) 구하기
    last_datetime = None
    sql = "select max(postdate) as maxdate from stock_dart"
    result = con.execute(sql)
    result_list = result.fetchall()
    last_datetime = result_list[0][0]

    if last_datetime is None:
        last_datetime = datetime(2004, 1, 1)
    today = datetime.today()
    delta = today - last_datetime

    url_tmpl = 'http://dart.fss.or.kr/dsac001/search.ax?selectDate=%s'

    for i in range(delta.days + 1):
        reqdate = last_datetime + timedelta(days=i+1)
        print(reqdate)
        fn = "DART-%s.html" % reqdate.strftime("%Y%m%d")
        wget(url_tmpl % reqdate.strftime('%Y%m%d'), fn)    # html을 로컬 파일로 저장
        n = dart_html_to_db(fn, last_datetime, reqdate, con)  # 로컬 파일 데이터로 DB insert
        os.remove(fn)
        print(fn, n)
    
    con.close()
