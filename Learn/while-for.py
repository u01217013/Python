 # -*- coding: utf-8 -*-
 #while迴圈 - While 布林值 :
n=1
sum=0 #記錄累加的結果
while n<=10:
    print("本次資料數字為： ",n)
    sum=sum+n #1加到10的數字
    n+=1
print(sum)

 #for迴圈 - for 變數名稱 in 列表：    for迴圈很常搭配range()，range()可以產出可以產出一個連續數字的列表(括號內數字是指字元編碼的數字)
for x in [1,3,5]:
    print(x)

for y in range(5):
    print(y)

for z in range(5,10): #同Tuple、string，包含開頭但不包含結尾
    print(z)

u=1
sum1=0
for xyz in range(1,11):
    print("本次資料為：",xyz)
    sum1=sum1+xyz
    xyz+=1
print(sum1)
