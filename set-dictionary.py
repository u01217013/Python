 # -*- coding: utf-8 -*-
#集合＝一群資料，沒有順序性 用{}
#判斷資料是否存在，使用in、not in 運算符號
#交集＆，聯集｜
#差集-，反交集^
#字串可以拆解成集合 set=(字串)
s1={3,4,5}
print(3 in s1)
print(10 not in s1)
s1={3,4,5}
s2={4,5,6,7}
s3=s1&s2 #s1交集s2 &＝交集，取兩個集合中，重疊的資料
s4=s1|s2 #s1聯集s2 ｜＝聯集，取兩個集合中全部的資料，但不重複取
s5=s1-s2 #s1差集s2 -＝差集，從s1中，減掉跟s2重疊的資料
s6=s1^s2 #s1反交集s2 ＾＝反交集，取兩個集合中，不重疊的資料
print(s3)
print(s4)
print(s5)
print(s6)
s=set("hello") #set(字串），可以自動把字串中的字母拆解成集合(會自動去掉重複的值)，因為集合沒有順序性，所以print出來的資料是沒有順序性的
print(s)
print("h" in s)


#字典觀念，key-value Pair，key對應Value，字典[key]，字典[key]=Value 
#字典使用{}
#同集合，可使用in、not in判斷資料(key)是否存在，可用del刪除字典中的配對，也可以從列表建立字典 
dic={"Apple":"蘋果","Bug":"蟲蟲"}
print(dic["Apple"])
dic["Apple"]="小蘋果"
print(dic["Apple"])
print("Apple" in dic) #判斷Key值是否存在
del dic["Apple"] #刪除字典中的key-value Pair(鍵值對)
print(dic)
#從列表的資料產生字典
dic={x:x*2 for x in [3,4,5]} #for跟in是固定的，in後面要放的是列表資料
print(dic)



