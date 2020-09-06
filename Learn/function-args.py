#參數預設值 def函式名稱(參數名稱＝預設資料)：
#預設資料為"hello"
def say(msg="hello"):  #有兩種用法
    print(msg)
say("hello,python") #第一種，直接更改msg資料
say() #第二種，參數資料沒有輸入，故直接印出預設值hello

#範例二 開次方 用**表示
def math(base,exp=1): #exp=1，就是預設值
    print(base**exp)
math(3,3)
math(4) #會使用預設值去開方
    

#參數名稱對應 def函式名稱(參數名稱1,參數名稱2):
                   #print(參數名稱2＝3,參數名稱1＝6)
def divide(n1,n2):
    result=n1/n2
    print(result)
divide(2,4)
divide(n2=2,n1=4)

#無限/不定長度的參數
#def 函式名稱(*無限參數)：
     #無限參數以Tuple資料型態處理
     #函式內部程式碼
#呼叫函式，可傳入無限數量的參數資料
#函示名稱(資料1,資料2,資料3)
def say(*msgs):
    for msg in msgs:
        print(msg)
say("hello","Ryan","gogogo")
#範例二

def avg(*number):
    sum=0
    for n in number:
        sum+=n
    print(sum/len(number))
avg(3,4)
