#有序、可變動列表List 用[]
grades=[12,60,15,70,90]
print(grades)
#使用索引（跟String的字元編碼一樣，從0開始，0代表第一個位置）
grades=[12,60,15,70,90]
print(grades[0])
#更新列表中資料
grades=[12,60,15,70,90]
grades[0]=55 #把55放到列表中第一個位置
print(grades)
#可以跟String一樣，用[1:4]取得索引(string時稱作字元)指定位置的資料，但不包含第4個資料，也就是包含開頭但不含結尾
grades=[12,60,15,70,90]
print(grades[1:4])
#刪除列表資料
grades=[12,60,15,70,90]
grades[1:4]=[] #連續刪除列表中編號1到編號4(不包括)的資料
print(grades)
#列表串接
grades=grades+[12,33]
print(grades)
#使用Len取得列表長度
length=len(grades) 
print(length)
print(len(grades)) #進階寫法，答案一樣
#巢狀列表
data=[[3,4,5],[6,7,8]]
print(data[0][1]) #取索引0的資料=[3,4,5]，再取得[3,4,5]內索引1的資料，故＝4
data[0][0:2]=[5,5,5] #更改列表內資料，若多一位，則新列表也會自動增加一位（data[0]指的是[3,4,5]，[0:2]指的是[3,4,5]內的3,4
print(data)

#有序、不可變動列表Tuple 用()，操作都同 List
data=(3,4,5)
#data[0]=5 #會是錯誤的，因為Tuple列表內的資料是不可變動的，故這就是與List不同地方(故要成功執行程式，就要把這行去掉，不可以更動Tuple資料)
print (data)

