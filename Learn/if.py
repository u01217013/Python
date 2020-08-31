# -*- coding: utf-8 -*-
# if 判斷式 ，還有一種判斷式叫switch,但python3.6不支援switch語法
x=input("請輸入數值：") #使用著輸入的會是字串型態
x=int(x) #將字串型態轉換成數字型態才可以開始比較
if x>200: #python if、elif、else最後都要加：
    print("大於200")
elif x>100: #else if
    print("大於100，小於200")
else:
    print("小於100")
#四則運算
n1=int(input("請輸入數字一： ")) #字串直接轉換成數字型態
n2=int(input("請輸入數字二： "))
op=input("請輸入運算符號 +、-、*、/: ")
if op=="+": #==兩個等於才是比較資料的大小與運算，若是只有一個＝，會變成指定資料料給變數
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("不支援此運算符號，請重新輸入")



