import LawCrawler

def entrance(target):
    find = 0
    # Patent Url
    tlink = "https://www1.tipo.gov.tw/lp.asp?CtNode=7199&CtUnit=3259&BaseDSD=7&mp=1"
    clink = tlink
    lc = LawCrawler.LawCrawler(link = tlink, fname = "Patent", urlroot = "https://www1.tipo.gov.tw/")
    while(find < target):
        lc.find_externallink()
        find = lc.get_count()
        if (find >= 10):
            clink = tlink + "&nowPage=" + str(lc.get_count() // 10 + 1) + "&pagesize=10"
        lc.change_link(clink)
    lc.default_exit()
    
if __name__ == "__main__":
    entrance(target = 10)