from bs4 import BeautifulSoup
import requests

f = open("./find.txt","w+")
total = 0

def writeLink(sUrl):
    nUrl = "https://www1.tipo.gov.tw/" + sUrl
    nRs = requests.get(nUrl)
    nSoup = BeautifulSoup(nRs.text, 'html.parser')
    nTags = nSoup.find(class_='attachment').find(class_='filename').find_all('a')
    count = 0
    for nTag in nTags:
        if (count == 1 and total == 0):
            f.write("https://www1.tipo.gov.tw/" + nTag['href'])
        elif (count == 1):
            f.write("\n" + "https://www1.tipo.gov.tw/" + nTag['href'])
        count += 1

def twoHundred():
    global total
    while (total < 10):
        url = 'https://www1.tipo.gov.tw/lp.asp?ctNode=7076&CtUnit=3515&BaseDSD=7&mp=1'
        rs = requests.get(url)
        soup = BeautifulSoup(rs.text, 'html.parser')
        tags = soup.find(class_='list').find('table').find_all('a')
        for tag in tags:
            writeLink(tag['href'])
            total += 1
            
if __name__ == "__main__":
    twoHundred()
    f.close()

# url = 'https://www1.tipo.gov.tw/lp.asp?ctNode=7076&CtUnit=3515&BaseDSD=7&mp=1'
# rs = requests.get(url)
# soup = BeautifulSoup(rs.text, 'html.parser')
# tags = soup.find(class_='list').find('table').find_all('a')
# for tag in tags:
#     print(tag['href'])
#     nUrl = "https://www1.tipo.gov.tw/" + (tag['href'])
#     nRs = requests.get(nUrl)
#     nSoup = BeautifulSoup(nRs.text, 'html.parser')
#     nTags = nSoup.find(class_='attachment').find(class_='filename').find_all('a')
#     count = 0
#     for nTag in nTags:
#         if (count == 1):
#             f.write(nTag['href'] + "\n")
#         count += 1
# f.close()