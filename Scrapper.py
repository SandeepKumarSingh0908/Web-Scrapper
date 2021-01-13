# Importing the required libraries

import requests
from bs4 import BeautifulSoup
import time
import csv
import send_mail
from datetime import date

urls = ["https://in.finance.yahoo.com/quote/AMZN?p=AMZN","https://in.finance.yahoo.com/quote/FB?p=FB","https://in.finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch","https://in.finance.yahoo.com/quote/GOOG?p=GOOG&.tsrc=fin-srch"]
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}

today = str(date.today()) + ".csv"
csv_file = open(today, "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Stock Name', 'Current Price', 'Previous Close', 'Open', 'Bid', 'Ask', 'Day Range', '52 Week Range', 'Volume', 'Avg. Volume'])


for url in urls:
    stocks_data = [] # Creating empty list for storing data of all company stocks

    page_source_code = requests.get(url, headers=headers)
    soup = BeautifulSoup(page_source_code.content, 'lxml')

    header_info = soup.find_all('div', id= "quote-header-info")[0]
    stock_title = header_info.find('h1').text
    stock_price = header_info.find("div", class_ = "My(6px) Pos(r) smartphone_Mt(6px)").find("span").text

    # Appending the title and currentprice
    stocks_data.append(stock_title)
    stocks_data.append(stock_price)


    table_info = soup.find_all("div", class_= "D(ib) W(1/2) Bxz(bb) Pend(12px) Va(t) ie-7_D(i) smartphone_D(b) smartphone_W(100%) smartphone_Pend(0px) smartphone_BdY smartphone_Bdc($seperatorColor)")[0].find_all("tr")
    for i in range(0,len(table_info)):
        value = table_info[i].find_all("td")[1].text
        stocks_data.append(value)
    # Writing in csv file
    csv_writer.writerow(stocks_data)
    time.sleep(5) # Making new request after every five seconds

csv_file.close()

send_mail.send(filename=today)