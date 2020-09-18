#AJAX(另一個稱呼是XHR在檢查網頁原始碼時要找ＸＨＲ):是網頁前端的Javascript的程式技術，此技術會影響爬蟲的運作（看python影片第21集，有講解AJAX跟一般ＨＴＭＬ的差異）
#老師是用google示範認出網站運作模式並找到資料網址的，safari的原始碼呈現方式不太一樣，但都找得到，先跟老師一樣用GOOGLE找網址
#關鍵問題：認出網站運作模式，找出真正能抓到資料的網址

import urllib.request as req
url="https://medium.com/_/api/home-feed"
#加入底下這一段才會讓整段程式碼看起來像一個普通使用者，建立一個Request物件，付加Request Headers 的資訊
request=req.Request(url,headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.2 Safari/605.1.15"
})
# 使用 with request.urlopen(網址) 連上網路，並將其重新取名為 response ，最後使用 read() 函數，將網頁結果放入 data 中。
with req.urlopen(request) as response: # 原本 req.urlopen 的括號內會放網址而已，但為了讓我們更像一般使用者，這邊放入剛剛建立的物件request。
    data=response.read().decode("utf-8")# 取的網頁的原始碼。並用decode("uyf-8")來翻譯成中文（解碼），在此範例中，根據觀察網頁原始碼，抓到的資料格式是json格式

#解析Json格式，取得文章標題 （json格式是大括號跟中括號，大括號代表字典、中括號代表列表）
import json
data=data.replace("])}while(1);</x>","") #這組字串是網頁原始碼的字串，根據觀察，這一段程式碼會阻礙json格式解析(因為這段字串不是json格式)，所以將這段字串改為空字串後再執行程式
data=json.loads(data) #把原始資料解析成字典/列表的資料表現型式，讀取檔案內資料時才是load()，將資料轉換成字典/列表用loads()
print(data)
#取得json資料中的文章標題
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])

