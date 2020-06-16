import requests
url='http://file.finance.sina.com.cn/211.154.219.97:9494/MRGG/CNSESZ_STOCK/2020/2020-3/2020-03-18/5946123.PDF'
res=requests.get(url)
with open('test2.pdf','wb') as file:
    file.write(res.content)
    file.close()
