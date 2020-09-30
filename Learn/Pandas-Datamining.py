#資料工程順序：資料收集、資料清理、分析資料、、基於資料的應用。
#google play store的資料工程範例

#收集資料：googleplaystore.csv
import pandas as pd

#讀取資料
data=pd.read_csv("googleplaystore.csv") #把CSV檔案讀取成一個DataFrame

#觀察資料
print("資料數量",data.shape)
print("資料欄位",data.columns)
print("======以上是觀察資料======")

#分析資料:評分的各種統計數據
#print(data["Rating"]) Ｒating評分的意思
#因"取得前一百個應用程式的平均分數"這邊有分數問題，故增加以下程式碼排除
condition=data["Rating"]<=5 #判斷是否有大於5分的資料
data1=data[condition] #改成data1只是為了不影響後續安裝數量的各種統計數據的資料有誤
#print(data) #最後找到是10472這筆資料分數大於5,所以再做計算時，只取<=5的資料，於是將condition=data["Rating"]>5改成ondition=data["Rating"]<=5

print("平均數",data1["Rating"].mean())
print("中位數",data1["Rating"].median())
print("取得前一百個應用程式的平均分數",data1["Rating"].nlargest(1000).mean()) #這裡第一次print的時候超過5分，有問題，所以回頭查為什麼出問題

print("======以上是評分的各種統計數據======")
#分析資料：安裝數量的各種統計數據
print(data["Installs"]) #根據此印出結果，判斷Installs的資料是字串形式，ex:100,000+
data["Installs"]=pd.to_numeric(data["Installs"].str.replace("[,+]","").replace("Free","")) #pandas內有to_numeric工具，這個工具可以把字串轉換成數字，但電腦不會認「,＋」，故要先將這兩個符號轉換成空字串，再執行字串轉數字，轉換完之後再直接覆蓋掉
#執行完上面字串轉數字後發現10472這筆資料有錯誤，檢查程式碼後發現10472這筆資料的字串是"Free"，故將Free也替換成空字串
print("平均數",data["Installs"].mean())
condition=data["Installs"]>100000
print("安裝數量大於10萬的應用程式有幾個",data[condition].shape[0])  #shape(0)是為了只要印出列就好，不用看欄
print("======以上是安裝數量的各種統計數據======")

#基於資料的應用：關鍵字搜尋應用程式
keyword=input("請輸入關鍵字：") #讓使用者輸入
condition=data["App"].str.contains(keyword,case=False) #進入資料內搜尋App欄位內是否有包含到使用者輸入的關鍵字。case=False是contains的一個功能，可以用來忽略大小寫，意思就是使用者不用在意輸入時的大小寫，程式會自動把所有跟關鍵字有關的大小寫資料通通抓出來
print("包含關鍵字的應用程式名稱",data[condition]["App"])  #有的話就將那一欄名稱印出來
print("包含關鍵字的應用程式數量",data[condition].shape[0])  #shape(0)是為了只要印出列就好，不用看欄





