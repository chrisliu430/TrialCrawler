from bs4 import BeautifulSoup
import requests

url = 'https://www1.tipo.gov.tw/ct.asp?xItem=725973&ctNode=7076&mp=1'
rs = requests.get(url)
soup = BeautifulSoup(rs.text, 'html.parser')
tags = soup.find(class_='attachment').find(class_='filename').find_all('a')
count = 0
f = open("./find.txt","w+")
for tag in tags:
    if (count == 1):
        f.write(tag['href'] + "\n")
    count += 1
f.close()