#網路爬蟲基本流程:
#1.連線到特定網址，抓取想要的資料。
#2.解析資料，取得實際想要的部分。

#抓取資料，盡可能地讓程式模仿一個普通使用者的樣子
#解析資料，json格式就用json模組，但網路上的資料格式大多是HTML格式（<>角括號在HTML裡稱為標籤）可看第19集2:30秒
#抓取的資料為HTML格式時，使用第三方套件BeautifulSoup來解析 （安裝套件可用PIP套件管理工具，這個工具在安裝python時就已經安裝了）
#安裝套件的程式碼 pip install beautifulsoup4

#以下為程式範例
#抓取ＰＴＴ電影原始碼的網頁(HTML)

import urllib.request as req
url="https://www.ptt.cc/bbs/movie/index.html"
#加入底下這一段才會讓整段程式碼看起來像一個普通使用者，建立一個Request物件，付加Request Headers 的資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15"
})
# 使用 with request.urlopen(網址) 連上網路，並將其重新取名為 response ，最後使用 read() 函數，將網頁結果放入 data 中。
with req.urlopen(request) as response: # 原本 req.urlopen 的括號內會放網址而已，但為了讓我們更像一般使用者，這邊放入剛剛建立的物件request。
    data=response.read().decode("utf-8")# 取的網頁的原始碼。並用decode("uyf-8")來翻譯成中文（解碼）。
print(data)

#解析原始碼，取得每篇文章的標題
# 使用第三方套件： beautifulsoup4/直接在終端機打 pip install beautifulsoup4
# debug: 因為是用 macbook ，下載 BS4 相對麻煩些：
# Step1. 將 "curl https://bootstrap.pypa.io/get-pip.py -o get-pip.pysudo python get-pip.py" 貼上終端機。
# Step2. 將 "sudo python get-pip.py" 貼上終端機。 此處將會要求輸入電腦密碼。
# Step3. 下載 pip ，將 "sudo easy_install pip" 貼上終端機。
# Step4. 下載 BS4 ，將 "pip install beautifulsoup4" 貼上終端機。
# Step5. 再次下載 BS4 ，將 "pip3 install beautifulsoup4" 貼上終端機。
# 載入 bs4 套件。
import bs4
# 利用上方載入套件做解析：變數 data 是剛在網路上抓到的資料，丟給 Beautifulsoup，他會幫我們用 html 解析。 並用 root 代表整份網頁。
root=bs4.BeautifulSoup(data,"html.parser") # 利用上方載入套件做解析：變數 data 是剛在網路上抓到的資料，丟給 beautifulsoup4，他會幫我們用 html 解析。 
# 使用 ".find" 可以幫助我們找到符合一個以下條件的東西：
titles=root.find("div",class_="title") #尋找class="title"的div標籤
print(root.title) # .title ：抓取網頁標題。<title> 以及 </titl3> 分別代表開始與結束。
print(root.title.string) # .title.string ：抓取標籤內的文字。(不會再顯示印出上方時句首句末會出現的 <title> 以及 </titl3>)
print(titles) # 印出剛剛上面找到的標籤。這裏 titles 代表上面找到的 div 標籤。
print(titles.a.string) # 加上 ".a" 代表我們剛剛找到的那個 div 標籤底下的 <a> 裡面的東西； ".string" 則是抓取前面 "titles.a" 抓到的東西的文字。

# 使用 ".find_all" 可以幫助我們找到「全部」符合以下條件的東西：
titles = root.find_all("div", class_="title") # 尋找所有 class = "title" 的 div 標籤。
print(titles) # 印出剛剛上面找到的標籤。這裏 titles 代表上面找到的 div 標籤。

# 做完上面動作之後，會發現印出來的資料是一個列表的形式，所以我們嘗試使用 for 迴圈將標題資料抓出來：

for title in titles:
    if title.a != None: # 如果標題包含<a>標籤（沒有被刪除），印出來（！=是不等於）
        print(title.a.string) # 如果「不是None」這件事發生，則印出標題（"titles.a" 抓到的東西的文字）。
