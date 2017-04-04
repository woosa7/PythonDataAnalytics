#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# stock_desc.py

import time
import json
import pandas as pd
import requests
from bs4 import BeautifulSoup
import requests
import mysql.connector
from sqlalchemy import create_engine


# pwd=input('Enter Password for server:')
pwd = 'finda888'


# sector, wics, name_en
def get_naver_sector(code):
    name_en, sector, wics, market = 'nan', 'nan', 'nan', 'nan'
    url = 'http://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd=' + code
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    td = soup.find('td', {'class':'cmp-table-cell td0101'})
    if td == None:
        return sector, wics, name_en
        
    dts = td.findAll('dt')

    # dts[1], name_en
    name_en = dts[1].text
    
    # dts[2], sector
    s = dts[2]
    if s.text.find('KOSPI :') >= 0:
        market = 'KOSPI'
        sector = s.text.split(' : ')[1]
    elif dts[2].text.find('KOSDAQ :') >= 0:
        market = 'KOSDAQ'
        sector = s.text.split(' : ')[1]
            
    # dts[3], wics
    s = dts[3]
    if s.text.find('WICS :') >= 0:
        wics = s.text.split(' : ')[1]

    return market, wics, name_en

# desc, desc_date
def get_naver_desc(code):
    url = 'http://companyinfo.stock.naver.com/v1/company/cmpcomment.aspx'
 
    cmt_text = ' '
    cmt_date = time.strftime("%Y-%m-%d")
 
    if code[-1] == '5': # pre_order
        code = code[0:-1] + '0'
    if code[-1] == '7': # pre_order
        code = code[0:-1] + '0'
 
    headers = {'Host':'companyinfo.stock.naver.com'}
    r = requests.post(url, data={'cmp_cd': code}, headers=headers)
    if r.text == "":
        return (cmt_text, cmt_date)
 
    j = json.loads(r.text)
    cmt_date = j['dt'].replace('.', '-') + " 00:00:00"
    cmts = j['data'][0]
    cmts = [cmts['COMMENT_1'], cmts['COMMENT_2'], cmts['COMMENT_3'],  cmts['COMMENT_4'], cmts['COMMENT_5'] ]
    cmt_text = '. '.join(cmts)
    return (cmt_text, cmt_date)

# homepage url, phone, address
def get_naver_addres(code):
    homepage, phone, address = '', '', ''
    url = 'http://companyinfo.stock.naver.com/v1/company/c1020001.aspx?cmp_cd=' + code
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    tab = soup.find('table', {'id':'cTB201'})
    if tab == None:
        return homepage, phone, address
    
    td = tab.find('td', {'class':'c2 txt'})
    if td.a:
        homepage = td.a['href'].strip()

    td = tab.find('td', {'class':'c4 txt'})
    phone = td.text.strip()

    td = tab.find('td', {'class':'txt', 'colspan':'3'})
    address = td.text.strip()

    return homepage, phone, address
    

if __name__ == "__main__":
    
    # stock_price 테이블 생성
    create_table_sql = '''create table if not exists stock_desc (
        `code` varchar(20)  not null primary key,
        `name` varchar(50),
        `market` varchar(50),
        `wics` varchar(50),
        `phone` varchar(50),
        `homepage` varchar(255),
        `address` varchar(255),
        `name_en` varchar(255),
        `desc` varchar(2014),
        `desc_date` datetime
    );
    '''

    insert_update_sql = """insert into stock_desc
        (`code`, `name`, `homepage`, `phone`, `address`, `market`, `wics`, `name_en`, `desc`, `desc_date`) 
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        on duplicate key update
            `code`=values(code),
            `name`=values(name),
            `homepage`=values(homepage),
            `phone`=values(phone),
            `address`=values(address),
            `market`=values(market),
            `wics`=values(wics),
            `name_en`=values(name_en),
            `desc`=values(`desc`),
            `desc_date`=values(desc_date)
    """

    cnx_str = 'mysql+mysqlconnector://woosa7:'+pwd+'@localhost/findb'
    engine = create_engine(cnx_str, echo=False)

    # create table if not exists
    # engine.execute(create_table_sql)
    
    df_master = pd.read_sql("SELECT * FROM stock_master", engine)
    for idx, r in df_master.iterrows():
        homepage, phone, address = get_naver_addres(r['code'])
        market, wics, name_en = get_naver_sector(r['code'])
        desc, desc_date = get_naver_desc(r['code'])
        engine.execute(insert_update_sql, (r['code'], r['name'], homepage, phone, address, market, wics, name_en, desc, desc_date) )
        print(r['code'], r['name'])
    