from bs4 import BeautifulSoup
import requests

class LawCrawler():
    def __init__(self, link="", fname="default", count=1, durl="", autoconfig=True, ferr="./Error/err.log", urlroot=""):
        self.link = link
        self.fname = fname
        self.count = count
        self.durl = durl
        self.autoconfig = autoconfig
        self.ferr = open(ferr, "w")
        self.urlroot = urlroot
        self._get_html_parser()

    def _get_html_parser(self):
        rs = requests.get(self.link)
        self.parser = BeautifulSoup(rs.text, "html.parser")

    def find_download_url(self, elink=""):
        rs = requests.get(elink)
        parser = BeautifulSoup(rs.text, "html.parser")
        targets = parser.find(class_='attachment').find(class_='filename').find_all('a')
        for target in targets:
            self.durl = self.urlroot + target['href']
            self.download_file()

    def write_download_url(self, wurl="", fwrite="./Data/Default.txt"):
        pass

    def change_link(self, link = ""):
        self.link = link
        self._get_html_parser()

    def get_count(self):
        return self.count // 2

    def find_externallink(self):
        elinks = self.parser.find(class_='list').find('table').find_all('a')
        for elink in elinks:
            self.find_download_url(elink=self.urlroot + elink['href'])

    def download_file(self, dformat=".pdf"):
        self.durl = self.durl.rstrip('\n')
        rs = requests.get(self.durl)
        if (rs.headers['content-type'] != "text/html; Charset=utf-8"):
            with open('./' + self.fname + str(self.count) + dformat, 'wb') as writef:
                writef.write(rs.content)
                self.count += 1
        else:
            self.ferr.write(self.durl + "\n")

    def load_download_target(self, dformat="", fread="./Data/Default.txt"):
        if (fread != ""):
            fread = open(fread, "r")
            for durl in fread:
                self.durl = durl
                self.download_file(dformat)
            fread.close()
    
    def default_exit(self):
        self.ferr.close()
