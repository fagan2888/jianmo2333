import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import re

def download_pdf(pdf_url):
    res = requests.get(pdf_url)
    global code
    with open('./reports_files/{}.pdf'.format(code), 'wb') as file:
        file.write(res.content)
        file.close()

def get_report(report_url):
    res=requests.get(report_url)
    # print(res.text)
    res.encoding='gb2312'
    soup=BeautifulSoup(res.text,'lxml')
    report_text=soup.find_all('div',class_="tagmain")[0]
    report_file_url=report_text.a.get('href')
    print(report_file_url)
    download_pdf(report_file_url)

def get_ndbg_url(code):
    outter_url='http://money.finance.sina.com.cn/corp/go.php/vCB_Bulletin/stockid/{}/page_type/ndbg.phtml'.format(code)
    # print(outter_url)

    res=requests.get(outter_url)

    res.encoding='gb2312'
    # print(res.text)
    # open('out.html','w').write(res.text)

    # soup=BeautifulSoup(res.text,'lxml')
    # print(soup.find_all(attrs={'class':'R'}))

    ids=re.findall("(?<=/corp/view/vCB_AllBulletinDetail.php\?).*?(?=')",res.text)
    # print(ids)
    report_url='http://money.finance.sina.com.cn/corp/view/vCB_AllBulletinDetail.php?{}'.format(ids[0])
    get_report(report_url)


global code


df=pd.read_csv('fetch_cfo.csv')
codes=df['code']
flag=0

for one in codes:
    code=one[:6]
    print(code,end=',')
    start_code='002338'
    if flag==0:
        if code==start_code:
            flag=1
        else:
            continue
    try:
        get_ndbg_url(code)
    except:
        print('NA')
