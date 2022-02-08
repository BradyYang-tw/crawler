import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/MobileComm/index.html"
# 將此頁面的HTML GET下來
r = requests.get("https://www.ptt.cc/bbs/MobileComm/index.html")
# 將網頁資料以html.parser
soup = BeautifulSoup(r.text, "html.parser")
# 取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
sel = soup.select("div.title a")

if __name__ == '__main__':
    print(sel)