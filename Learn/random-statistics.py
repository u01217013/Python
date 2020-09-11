#學習python內建模組 random、statistics 隨機模組與統計模組
#random
import random
#從列表中隨機選取一個資料
data=random.choice([0,1,5,8,10])
print(data)
#從列表中隨機選取兩個資料，sample可隨機選取n個資料
data=random.sample([0,1,5,8,10],3)
print(data)

#隨機調換順序
#將列表的資料『就地』隨機調換順序
data=[0,1,5,8,10,20]
random.shuffle(data)
print(data)

#取得隨機亂數
#取得0.0~1.0之間的隨機亂數
data=random.random() #這個只會取0~1之間的隨機亂數
print(data)
data=random.uniform(5.0,15.0) #uniform表示機率相同，可以指定數字到數字之間
print(data)

#常態分配亂數
#取得平均數100、標準差10的常態分配亂數
data=random.normalvariate(100,10) #第一個參數=平均數,第二個參數＝標準差。以此例為例，取得的隨機亂數大部分會在90-110之間
print(data)

#統計模組 statistics
import statistics
#計算平均數
data=statistics.mean([1,4,5,8])
print(data)
#計算中位數 
data=statistics.median([1,2,3,4,5,8,100])
print(data)
#計算標準差（標準差表示資料散佈的狀況）
data=statistics.stdev([1,4,5,8])
print(data)

