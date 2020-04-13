from bs4 import BeautifulSoup
import requests

f = open("./test.txt","w+")
total = 0

def writeLink(sUrl):
    nUrl = "https://www1.tipo.gov.tw/" + sUrl
    nRs = requests.get(nUrl)
    nSoup = BeautifulSoup(nRs.text, 'html.parser')
    nTags = nSoup.find(class_='attachment').find(class_='filename').find_all('a')
    for nTag in nTags:
        f.write("https://www1.tipo.gov.tw/" + nTag['href'] + "\n")

def twoHundred():
    global total
    while (total < 10):
        url = 'https://www1.tipo.gov.tw/lp.asp?ctNode=7076&CtUnit=3515&BaseDSD=7&mp=1'
        if (total >= 10):
            nPage = total // 10 + 1
            url = url + "&nowPage=" + str(nPage) + "&pagesize=10"
        rs = requests.get(url)
        soup = BeautifulSoup(rs.text, 'html.parser')
        tags = soup.find(class_='list').find('table').find_all('a')
        for tag in tags:
            writeLink(tag['href'])
            total += 1

if __name__ == "__main__":
    twoHundred()
    f.close()
