#類別與實體物件、實體屬性（上篇學的）、實體方法（這篇才會教）
#這邊要學的是在實體物件中建立實體方法
#實體屬性：封裝在實體物件中的變數
#實體方法：封裝在實體物件中的函式

# 實體方法基本語法
# class 類別名稱:
#     定義初始化函式
#     def __init__(self):
#         定義實體屬性
#     定義實體方法/函式
# 建立實體物件ㄝ,存入變數中
# obj=類別名稱()

#由上面延伸出來就會變成下面這段
# class 類別名稱:
#     定義初始化函式
#     def __init__(self):
#         封裝在實體物件中的變數
#     def 方法名稱(self,更多自訂參數)
#         方法主體,透過self操作實體物件
# 建立實體物件ㄝ,存入變數中
# obj=類別名稱()

#使用方法
#實體物件.實體方法名稱（參數資料）

#實體物件的設計：平面座標上的點
class point:
    #定義實體屬性
    def __init__(self,x,y):
        self.x=x
        self.y=y
    #以下為定義實體方法，一個實體物件中可以有很多個實體方法
    def Show(self):
        print(self.x,self.y)
    def distance(self,x1,y1):
        return(((self.x-x1)**2)+((self.y-y1)**2))**0.5 #return 回傳值之後，需要再給他一個變數存放資料，然後才能print出來
p=point(3,4)
p.Show() #呼叫實體方法（本質上是一個函式），在定義Show的時候沒有給後面的參數，所以沒有辦法設定參數
dis=p.distance(0,0)  #在定義distance的時候有給定x1、y1兩個參數，所以在呼叫時需給參數
print(dis)

# 實體物件的設計：包裝檔案讀取得程式 
class file:
    #定義初始化函示
    def __init__(self,name):
        self.name=name
        self.file=None #尚未開啟檔案：初期是none
    #定義實體方法
    def open(self):
        self.file=open(self.name,mode="r",encoding="utf-8")
    #定義實體方法
    def read(self):
        return self.file.read()
#讀取第一個檔案
f1=file("data.txt")
f1.open()
data=f1.read()
print(data)
#讀取第二個檔案
f2=file("data1.txt")
f2.open()
data=f2.read()
print(data)



