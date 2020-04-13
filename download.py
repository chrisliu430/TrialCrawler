import requests

f = open("./find.txt", "r")
df = open("./find_filter.txt", "w")

TMCount = 1

for url in f:
    url = url.rstrip("\n")
    rs = requests.get(url)
    if (rs.headers['content-type'] != "text/html; Charset=utf-8"):
        with open('./Trade' + str(TMCount) + ".pdf", 'wb') as wf:
            wf.write(rs.content)
        TMCount += 1
    else:
        df.write(url + "\n")
f.close()