#函式：程式碼包裝在一個區塊中，方便隨時呼叫使用，沒有呼叫就無法使用
#要先定義（建立）函式，才能呼叫（使用）函式
#def 函式名稱（參數名稱）： 程式碼
#定義一個印出Hello的函式
def sayhello():
    print("hello")
#定義可以印出任何訊息的函式
def say(msg):
    print(msg)

#定義一個可以做加法的函式
def add(n1,n2):
    result=n1+n2
    print(result)

#呼叫函式 函式名稱（參數資料）
#呼叫上方定義的函式，取得回傳值（return)
sayhello()
say("hello python, I love you")
say("安安安安安安")
add(10,5)
add(1,2)

#回傳值  
# def 函式名稱（參數名稱）：
     #函示內部程式碼
     #return #代表結束函示,回傳None
     #return 資料 #結束函示，回傳資料（數字、字串、布林值、列表、字典、物件）、

#示範用
def say1(anything):
    print(anything)
    return
value=say1("啦啦啦啊啦啦啦")
print(value)

#示範用
def add1(n1,n2):
    result=n1+n2
    return "Ｈello"
value=add1(3,5)
print(value)

#根據計算結果，回傳結果
def add1(n1,n2):
    result=n1+n2
    return n1+n2
value=add1(3,5)
print(value)

def add2(n1,n2):
    return n1*n2
value=add2(3,5)+add2(8,10)
print(value)   

#最重要的用法 函式的包裝
def calculate():
    sum=0
    for n in range(1,11):
        sum+=n
    return sum

value=calculate()
print(value)

def calculate1(max):
    sum=0
    for n in range(1,max+1):
        sum+=n
    return sum #可以用return回傳值再輸出結果，也可以直接在函示內輸出結果，一切看自己要如何使用，故也可以不return,直接寫print(sum) 範例如下

value=calculate1(20)
print(value)


#結合上面兩個
def calculate2(max):
    sum=0
    for n in range(1,max+1):
        sum+=n
    print(sum) 

calculate2(10)
calculate2(20)