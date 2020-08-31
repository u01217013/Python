# -*- coding: utf-8 -*-
#數字運算
x=3/6
print(x)
#兩條//會變成整數除法，也就是python不會除到小數
x=9//2
print(x)
#Ａ的3次方可以用Ａ**3表示
x=3**2
print(x)
#取餘數的符號 ％
x=7%3
print(x)
#變數加減乘除運算
x=x+1 #x+=1運算結果就等於x=x+1，減乘除也是一樣
print(x)

#字串運算
s="hellooo"#字串可以用“雙引號也可以用‘單引號，自己選擇
print(s)
s="hello\"oooo" #\可以將字串內原本的引號跳脫，不要讓他跟字串的雙引號打架，這樣就可以顯示出字串內的引號
print(s)
s="Hello"+"Ryan"+"you are cool" #字串的串接可以用＋也可用空格，例如"Hello" "Ryan" "you are cool"
print(s)
s="hello\nworld" #\n表示換行 
print(s)
s="""連打3個雙引號或是單引號 #雙引號跟單引號的換行方式

就可以在程式碼內直接換行喔"""
print(s)
s="hellooo"*3 #這個文字會出現3次
print(s)
#字串會對內部的字元編號（索引），從0開始算起
s="hello"
print(s[1]) #加[]就是要取哪一個字元編號
s="hello"
print(s[1:4]) #表示可以取編號1、2、3的字元，但不含包4(hello的o是編號4)，也就是包含開頭但不包含結尾
s="hello"
print(s[1:]) #表示從編號1開始，之後的全部都一起抓出來
s="hello"
print(s[:4]) #表示從編號0開始，但不含包4(hello的o是編號4)，也就是包含開頭但不包含結尾





