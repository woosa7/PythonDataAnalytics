#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
import mysql.connector
from sqlalchemy import create_engine

pwd = 'cansentme'
cnx_str = 'mysql+mysqlconnector://admin:'+pwd+'@'+ 'localhost/findb'


def get_last_page_num(code):
    npage = 1
    url = 'http://finance.naver.com/item/sise_day.nhn?code=%s&page=1' % (code)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    td = soup.find('td', attrs={'class':'pgRR'})
    if td:
        npage = td.a['href'].split('page=')[1]
    return int(npage)

def get_data_naver(code, start=datetime(1900,1,1), end=datetime(2100,1,1)):
    url_tmpl = 'http://finance.naver.com/item/sise_day.nhn?code=%s&page=%d'
    npages = get_last_page_num(code)
    df_price = pd.DataFrame()
    for p in range(1, npages+1):
        url = url_tmpl % (code, p)
        dfs = pd.read_html(url)
        
        # first page
        df = dfs[0] 
        df.columns = ['date', 'close', 'change', 'open', 'high', 'low', 'volume']
        df = df[1:]
        df = df.dropna()
        df = df.replace('\.', '-', regex=True)

        # select date range
        start_str = start.strftime("%Y-%m-%d")
        end_str = end.strftime("%Y-%m-%d")
        mask = (df['date'] >= start_str) & (df['date'] <= end_str)
        df_in = df[mask]

        # merge dataframe
        df_price = df_price.append(df_in)
        #print('%d page,' % p, end='', flush=True)
        #print(df['date'].max())
        if df['date'].max() <= start_str:
            break
    #print()
    df_price['date'] = pd.to_datetime(df_price['date'])
    int_cols = ['close', 'change', 'open', 'high', 'low', 'volume']
    df_price[int_cols] = df_price[int_cols].astype('int', raise_on_error=False)
    return df_price
    
if __name__ == "__main__":
    # stock_price 테이블 생성
    create_table_sql = '''create table if not exists `stock_price` (    
        `date` datetime,
        `code` varchar(20),
        `close` int,
        `change` int,
        `open` int,
        `high` int, 
        `low` int,  
        `volume` int,
        primary key (date, code)
    );
    '''

    insert_sql = """
        insert into stock_price (`date`, `code`, `close`, `change`, `open`, `high`, `low`, `volume`) values (%s,%s,%s,%s,%s,%s,%s,%s)
    """
    
    engine = create_engine(cnx_str, echo=False)

    # create table if not exists
    engine.execute(create_table_sql)
    
    df_master = pd.read_sql("SELECT * FROM stock_master", engine)
    for inx, row in df_master[136:].iterrows():
        print("%4s/%s" % (inx+1, len(df_master)), row['code'], row['name'])
        #  start: DB에 저장된 마지막 날짜 + 1일
        df_max = pd.read_sql('select * from stock_price where code="%s" order by date desc limit 1' % row['code'], engine)
        
        last_date = datetime(1900,1,1)
        if len(df_max) > 0 and df_max['date'].iloc[0] != None:
            last_date = datetime.strptime(str(df_max['date'].iloc[0]), "%Y-%m-%d %H:%M:%S")
        start = last_date + timedelta(1)

        # end: 전일
        yday = datetime.today() - timedelta(1)
        end = datetime(yday.year, yday.month, yday.day)

        df_price = get_data_naver(row['code'], start, end)
        df_price['code'] = row['code']
        for ix, r in df_price.iterrows():
            values = (r['date'].strftime('%Y-%m-%d %H:%M:%S'), r['code'], r['close'], r['change'], r['open'], r['high'], r['low'], r['volume'])
            engine.execute(insert_sql, values)
            print(r['code'], r['date'], r['close'])


  