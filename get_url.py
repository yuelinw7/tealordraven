import requests
from bs4 import BeautifulSoup
import re
import csv
import numpy as np

with open('./country_code.csv') as csvfile:
    reader=csv.reader(csvfile)
    column=[row[1] for row in reader]
    # print(column)


for cc in column[1:2]:
    web=requests.get('https://www.google.com/search?q=filetype:pdf+site:'+cc+'&start=40')
    html = web.text.encode('utf8')
    # with open('./test.html','wb') as f:
    #     f.write(html)

    soup = BeautifulSoup(html, 'html.parser')

    pdf_links=soup.find_all('a',{'href':re.compile(r'.*?\.pdf')})
    # print(pdf_links)
    pdf_list=[]

    for link in pdf_links:
        link_str=link['href']
        # print(link_str)
        pdf_list.append(link_str.split('url?q=')[1].split('&sa=U')[0])
    
    with open('./pdf_list.txt','a') as f:
        for pdf in pdf_list:
            f.write(pdf+'\n')
            print(pdf)
