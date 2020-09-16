#cookie就是網站存放在瀏覽器的一小段內容
#cookie在與伺服器連線時，會被放在Request Headers中送出

#抓取ＰＴＴ八卦版原始碼的網頁(HTML)
import urllib.request as req
def getData(url):
    #加入底下這一段才會讓整段程式碼看起來像一個普通使用者，建立一個Request物件，付加Request Headers 的資訊
    request=req.Request(url,headers={
        "cookie":"over18=1",#要帶上cookie才能夠像使用者點擊滿18歲一樣，這樣才能進去八卦版
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15"
    })
    # 使用 with request.urlopen(網址) 連上網路，並將其重新取名為 response ，最後使用 read() 函數，將網頁結果放入 data 中。
    with req.urlopen(request) as response: # 原本 req.urlopen 的括號內會放網址而已，但為了讓我們更像一般使用者，這邊放入剛剛建立的物件request。
        data=response.read().decode("utf-8")# 取的網頁的原始碼。並用decode("uyf-8")來翻譯成中文（解碼）。
    print(data)

    #解析原始碼，取得每篇文章的標題
    import bs4
    root=bs4.BeautifulSoup(data,"html.parser") # 利用上方載入套件做解析：變數 data 是剛在網路上抓到的資料，丟給 beautifulsoup4，他會幫我們用 html 解析。 
    titles=root.find("div",class_="title") #尋找class="title"的div標籤
    print(root.title) # .title ：抓取網頁標題。<title> 以及 </titl3> 分別代表開始與結束。
    print(root.title.string) # .title.string ：抓取標籤內的文字。(不會再顯示印出上方時句首句末會出現的 <title> 以及 </titl3>)
    print(titles) # 印出剛剛上面找到的標籤。這裏 titles 代表上面找到的 div 標籤。
    print(titles.a.string) # 加上 ".a" 代表我們剛剛找到的那個 div 標籤底下的 <a> 裡面的東西； ".string" 則是抓取前面 "titles.a" 抓到的東西的文字。
    titles = root.find_all("div", class_="title") # 尋找所有 class = "title" 的 div 標籤。
    print(titles) # 印出剛剛上面找到的標籤。這裏 titles 代表上面找到的 div 標籤。
    for title in titles:
        if title.a != None: # 如果標題包含<a>標籤（沒有被刪除），印出來（！=是不等於）
            print(title.a.string) 
    #追蹤網頁連結，抓取ＰＴＴ上一頁的功能連結，這樣可以不斷地記錄每一頁ＰＴＴ的資料
    nextlink=root.find("a",string="‹ 上頁") #找到HTML程式碼內文是"‹ 上頁"的 a 標籤
    return nextlink["href"] #印出"‹ 上頁"的 a 標籤的href屬性
#連續一個頁面的標題
pageurl="https://www.ptt.cc/bbs/Gossiping/index.html"
count=0
while count<3: #抓3頁
    pageurl="https://www.ptt.cc"+getData(pageurl) #getData不會抓到前面https://www.ptt.cc這段文字，所以要自己加
    count+=1 









