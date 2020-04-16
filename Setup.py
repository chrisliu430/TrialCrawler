import LawCrawler

def entrance(target):
    wflink = { # Want Find Link
        0 : ["Patent", "https://www1.tipo.gov.tw/lp.asp?CtNode=7199&CtUnit=3259&BaseDSD=7&mp=1"],
        1 : ["Trade", "https://www1.tipo.gov.tw/lp.asp?ctNode=7076&CtUnit=3515&BaseDSD=7&mp=1"]
    }
    ftarget = 0
    while (ftarget < len(wflink)):
        find = 0
        clink = wflink[ftarget][1]
        lc = LawCrawler.LawCrawler(link = wflink[ftarget][1], fname = wflink[ftarget][0], urlroot = "https://www1.tipo.gov.tw/")
        while(find < target):
            lc.find_externallink()
            find = lc.get_count()
            if (find >= 10):
                clink = wflink[ftarget][1] + "&nowPage=" + str(lc.get_count() // 10 + 1) + "&pagesize=10"
            lc.change_link(clink)
        lc.default_exit()
        ftarget += 1
    
if __name__ == "__main__":
    entrance(target = 10)