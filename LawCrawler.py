from bs4 import BeautifulSoup
import requests

class LawCrawler():
    def __init__(self, link = "", number = 0, count = 0, durl = "", autoconfig = True, ferr = "./Error/err.log"):
        self.link = link
        self.number = number
        self.count = count
        self.durl = durl
        self.autoconfig = autoconfig
        self.ferr = open(ferr, "w")

    def _get_html_parser(self):
        rs = requests.get(self.link)
        self.parser = BeautifulSoup(rs.text, "html.parser")

    def write_link(self, fname="./Data/Default.txt"):
        pass

    def search_tag(self, target = ""):
        pass

    def search_all_tags(self, target = ""):
        self._get_html_parser()
        print(self.link)
        ftarget = self.parser.find(target)
        print(ftarget.encode('utf-8'))
        # for aftarget in ftarget:
        #     print(aftarget.encode('utf-8'))

    def download_file(self, dformat = ""):
        self.durl = self.durl.rstrip('\n')
        rs = requests.get(self.durl)
        if (rs.headers['content-type'] != "text/html; Charset=utf-8"):
            with open('./Patent' + str(self.count) + dformat, 'wb') as writef:
                writef.write(rs.content)
                self.count += 1
        else:
            self.ferr.write(self.durl + "\n")

    def load_download_target(self, dformat = "", fread = ""):
        if (fread != ""):
            fread = open(fread, "r")
            for durl in fread:
                self.durl = durl
                self.download_file(dformat)
            fread.close()
    
    def default_exit(self):
        self.ferr.close()
