#資料索引：像excel內的Ａ1、Ｂ2一樣

#載入padnas模組
import pandas as pd
#資料索引
data=pd.Series([5,4,-2,3,7], index=["a","b","c","d","e"]) #index 自訂索引,索引數量要同series的資料數量
#print(data) #print出來的左邊欄就是索引

#觀察資料
# print("資料型態",data.dtype)
# print("資料數量",data.size)
# print("資料索引",data.index)

#取得資料：根據順序、根據索引
# print(data[2],data[0]) #根據資料順序
# print(data["e"],data["d"]) #根據索引

#數字運算：基本、統計、順序
# print("最大值",data.max())
# print("總和",data.sum())
# print("標準差",data.std())
# print("中位數",data.median())
# print("最大的三個數",data.nlargest(3))
# print("最小的二個數",data.nsmallest(2))

#字串運算：基本、串接、、搜尋、取代
data1=pd.Series(["您好","Python","Pandas"])
print(data1.str.lower()) #字串操作一定要加str,這是基本操作 ,lower是全部字串變小寫
print(data1.str.len()) #計算字串長度
print(data1.str.cat(sep="-")) #cat是將series的字串列表通通合再一起。sep則是可以自訂字串合併時，字串跟字串之前要用什麼串接、區隔
print(data1.str.contains("P")) #判斷字串中是否包含P,判斷每個字串是否判斷每個字串是否包含特定字元
print(data1.str.replace("您好","Hello")) #將原本字串替換成指定的字串