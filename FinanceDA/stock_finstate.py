#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# stock_finstate.py

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

def get_finstate_year(code):
    '''
    * code: 종목코드
    * fin_type = 재무제표 종류 (3: IFRS별도, 4:IFRS연결)
    * freq_type = 기간 (Y:년, Q:분기)
    '''
    url_tmpl = 'http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd=%s&fin_typ=4&freq_typ=Y'
    url = url_tmpl % (code)

    data = pd.read_html(url, encoding='utf-8')
    fin_df = data[0]
    if len(fin_df) <= 2:
        return None
    fin_df = fin_df.set_index('주요재무정보')  # index

    colnames = list(fin_df.columns)
    colnames.remove('연간')
    colnames = [get_date_str(x) for x in colnames]

    fin_df = fin_df.ix[:, :-1]  # 밀려서 생긴 마지막 컬럼 제거
    fin_df.columns = colnames

    trans_df = fin_df.T
    trans_df.rename(columns={'주요재무정보': 'date'}, inplace=True)
    trans_df.index = pd.to_datetime(trans_df.index)

    # 컬럼명 영문으로 변경
    colnames = ['sales','biz_profit','net_profit','assets','debts','gross_capital','capital','cash_oper',
                'cash_invest','cash_finance','capex','fcf','debt_interest','rob','ron',
                'roe','roa','debt_ratio','reserve_ratio','eps','per','bps','pbr',
                'dps','d_profit','d_tendency','totalshares']

    dfs = trans_df[['매출액','영업이익','당기순이익','자산총계','부채총계','자본총계','자본금','영업활동현금흐름',
                    '투자활동현금흐름','재무활동현금흐름','CAPEX','FCF','이자발생부채','영업이익률','순이익률',
                    'ROE(%)','ROA(%)','부채비율','자본유보율','EPS(원)','PER(배)','BPS(원)','PBR(배)',
                    '현금DPS(원)','현금배당수익률','현금배당성향(%)','발행주식수(보통주)']]
    dfs.columns = colnames

    return dfs
    
    
# 이전 데이터 삭제 (중복방지를 위해)
sql_del = "delete from stock_finstate where code=%s and fin_type=%s and freq_type=%s"

if __name__ == "__main__":
    cnx_str = 'mysql+mysqlconnector://woosa7:'+pwd+'@localhost/findb'
    engine = create_engine(cnx_str, echo=False)

    df_master = pd.read_sql("SELECT * FROM stock_master", engine)
    for idx, r in df_master.iterrows():
        print(r['code'], r['name'])
        
        # fin_type: '3' IFRS 분리, '4' IFRS 연결
        # freq_type = 'Q' 분기, 'Y' 년
        df = get_finstate_year(r['code'])
        if df is None:
            continue
        engine.execute(sql_del, (r['code'], '4', 'Y'))
        df.to_sql('stock_finstate', con=engine, if_exists='append', index=False)
                
