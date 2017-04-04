#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# stock_master.py
# findb 데이터베이스, stock_master 테이블

import io
import requests
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# pwd=input('Enter Password for server:')
pwd = 'finda888'


def get_krx_stock_master():
    # STEP 01: Generate OTP
    gen_otp_url = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx'
    gen_otp_data = {
        'name':'fileDown',
        'filetype':'xls',
        'url':'MKD/04/0406/04060100/mkd04060100_01',
        'market_gubun':'ALL', # ''ALL':전체, STK': 코스피
        'isu_cdnm':'전체',
        'sort_type':'A',
        'std_ind_cd':'01',
        'cpt':'1',
        'in_cpt':'',
        'in_cpt2':'',
        'pagePath':'/contents/MKD/04/0406/04060100/MKD04060100.jsp',
    }

    r = requests.post(gen_otp_url, gen_otp_data)
    code = r.content

    # STEP 02: download
    down_url = 'http://file.krx.co.kr/download.jspx'
    down_data = {
        'code': code,
    }

    r = requests.post(down_url, down_data)
    f = io.BytesIO(r.content)
    
    usecols = ['종목코드', '기업명', '업종코드', '업종', '대표전화', '주소']
    df = pd.read_excel(f, converters={'종목코드': str, '업종코드': str}, usecols=usecols)
    df.columns = ['code', 'name', 'sector_code', 'sector', 'telephone', 'address']
    return df


create_table_sql = """
    create table if not exists stock_master (
        code varchar(20) not null primary key,
        name varchar(50),
        sector_code varchar(30),
        sector varchar(80)
    )
"""

insert_update_sql = """
    insert into stock_master (code, name, sector_code, sector) 
    values (%s,%s,%s,%s)
    on duplicate key update
        code=values(code),
        name=values(name),
        sector_code=values(sector_code),
        sector=values(sector)
"""
    
if __name__ == "__main__":
    cnx_str = 'mysql+mysqlconnector://woosa7:'+pwd+'@localhost/findb'
    engine = create_engine(cnx_str, echo=False)

    # create table if not exists
    # engine.execute(create_table_sql)

    # get all stock codes and insert it
    df = get_krx_stock_master()
    df_master = df[['code', 'name', 'sector_code', 'sector']]
    for ix, r in df_master.iterrows():
        engine.execute(insert_update_sql, (r['code'], r['name'], r['sector_code'], r['sector']))
        print(r['code'], r['name'])
