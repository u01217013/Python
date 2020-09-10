#文字檔案的讀取或儲存
#開啟檔案語法：檔案物件＝open(檔案路徑,mode=開啟模式) ,檔案物件之後會再說
#mode主要分為以下三種（還有很多種模式）
#讀取模式- r
#寫入模式- w
#讀寫模式- r+

#讀取檔案語法：檔案物件.read   這樣會直接一次讀取全部文字
#若要一行一行讀取要用以下語法
#for 變數 in 檔案物件：
    #從檔案依序讀取每行文字到變數中
    
#讀取json格式 （json格式是網路很常使用的格式，用來交換資料，可看老師的javascript影片，裡面有介紹）
#import json
#讀取到的資料＝json.load(檔案物件)

#寫入（儲存）檔案語法：檔案物件.write(字串)    這是用來寫入文字的
#寫入換行符號語法：檔案物件.write("這是範例文字\n")   \n代表換行
#寫入json格式語法：
#import json
#json.dump(要寫入的資料,檔案物件)


#關閉檔案語法：檔案物件.close()


#python有提供一段最佳實務語法如下：
#with open(檔案路徑,mode=開啟模式) as 檔案物件：
    #讀取或寫入檔案的程式
#以上這一段會自動、安全的關閉檔案，就不需要再多寫一段關閉檔案的語法



#以下開始為影片示範程式
#儲存檔案
file=open("data.txt",mode="w")  #開啟 萬一中文跑不出來時，須將這一行變更成file=open("data.txt",mode="w",encoding="utf-8") 
file.write("Hello,Nice to meet you\nGood job\n做得非常好，繼續加油喔！") #操作  \n換行
file.close() #關閉

#用最佳實務語法寫
with open("data1.txt",mode="w") as file:
    file.write("Hello,Nice to meet you\nGood job\n做得非常好，繼續加油喔！\n這是用最佳實務語法寫的喔")

#讀取檔案 這是全部讀取
with open("data1.txt",mode="r") as file:
    data=file.read()
print(data) 

#綜合以上，且要讀取一行一行的數字並計算加總
sum=0
with open("data2.txt",mode="w") as file:
    file.write("5\n3")
with open("data2.txt",mode="r") as file:
    for n in file: #一行一行的讀取
         sum+=int(n)
print(sum)


#使用json格式讀取、複寫檔案
import json
#從檔案中讀取json資料，放入變數data裡面
with open("config.json",mode="r") as file:
    data=json.load(file) 
print(data)  #data會呈現一個字典資料,因為config.json的格式
print("Name:",data["name"])
print("Version:",data["version"])
data["name"]="New name" #修改變數data的資料
#把最新的資料複寫回檔案中
with open("config.json",mode="w") as file:
    json.dump(data,file) 
