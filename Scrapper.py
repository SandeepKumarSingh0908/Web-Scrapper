# Importing the required libraries

import requests
from bs4 import BeautifulSoup
import time

urls = ["https://in.finance.yahoo.com/quote/AMZN?p=AMZN","https://in.finance.yahoo.com/quote/FB?p=FB","https://in.finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch","https://in.finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch"]

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

for url in urls:

    page_source_code = requests.get(url, headers=headers)
    soup = BeautifulSoup(page_source_code.content, 'lxml')

    header_info = soup.find_all('div', id= "quote-header-info")[0]
    stock_title = header_info.find('h1').text
    stock_price = header_info.find("div", class_ = "My(6px) Pos(r) smartphone_Mt(6px)").find("span").text

    table_info = soup.find_all("div", class_= "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")


    print(stock_title)
    print(stock_price)


    for i in range(0,len(table_info)):
        heading = table_info[i].find_all("td")[0].text
        value = table_info[i].find_all("td")[1].text
        print(heading + " - " + value)

    print("-----------------------------------------------------------")
    time.sleep(5) #Making new request after every five seconds