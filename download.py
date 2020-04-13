import requests
import time

count = 0
TMcount = 1
f = open("find.txt", "r")
for i in f:
    # wFile = requests.get("https://www1.tipo.gov.tw/" + url, allow_redirects=True)
    # wget.download("https://www1.tipo.gov.tw/" + i, './' + str (TMcount) + '.pdf')
    # TMcount += 1
    file = requests.get(i, allow_redirects=True)
    open('./PDF' + str(TMcount) + ".pdf", 'wb').write(file.content)
    TMcount += 1
f.close()