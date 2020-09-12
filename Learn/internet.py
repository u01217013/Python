#網路連線，公開資料串接，以下為程式碼簡介
# import urllib.request as request #urllib.request為內建模組
# #下載特定網址資料
# with request.urlopen() as response:   urlopen(輸入欲下載的網址)
#     data=response.read()
# print(data)

# 要找適合的資料來源（公開資料）下載，如下
# 影片中的"台北市政府公開資料" 改版為 台北市資料大平台
# 網址 https://data.taipei/#/

#確認資料格式
#json、csv、其他格式，解讀json格式用內建的json模組
#程式範例
#網路連線
import urllib.request as request
src="http://www.ntu.edu.tw/"
with request.urlopen(src) as response:
    data=response.read().decode("utf-8") #會取得台灣大學網站的原始碼（HTML、CSS、JS)，現在網站都用utf-8編碼，加後面decode("utf-8")這段可以解碼中文，就可以看到中文
print(data)
#串接、擷取公開資料 API,API就是可以讓我們用程式自動去下載的資料
#範例用台北市政府公開資料：內湖科技園區廠商名錄
import urllib.request as request
import json 
src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire" #這是內湖科技園區的API網址，是json格式，所以要在import json模組
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組處理json資料格式
#print(data) #這只是取得所有資料，沒有經過整理的話沒有意義，所以接續做下面程式碼
#將公司名稱列表出來
Ａlist=data["result"]["results"] #為什麼會抓result、results是因為ＡＰＩ是json格式，公司名稱是在result列表裡面的results列表，可看第15集14:00處
#將抓取到的資料放入檔案內
with open("內湖科技園區公司名稱.txt",mode="w") as file:
#print(Alist) #可以抓取比較乾淨的公司資料，然後可執行以下程式碼，單純抓取公司名稱
    for company in Alist: 
        file.write(company["公司名稱"]+"\n")

