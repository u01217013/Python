#類別的兩種用法
#1.類別與類別屬性 （可看test-class.py)，2.類別與實體物件、實體屬性 （這次要學的）
#先定義類別，再透過類別建立實體物件，建立實體物件後，才能使用實體屬性
#基本語法
#class 類別名稱：
    #定義初始化函式 __init__(self)，self是固定的
    #def __init__(self):
        #透過操作self來定義實體屬性
#建立實體物件，放入變數obj中
#obj=類別名稱() #呼叫初始化函式

#程式碼範例，平面座標上的點
class point:
    def __init__(self):
        self.x=3
        self.y=4
#建立實體物件
#此實體物件包含x、y兩個實體屬性
p1=point()
#使用實體，實體物件.實體屬性名稱
print(p1.x,p1.y)

#進階版
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
#建立第一個實體物件
p1=point(1,5)
print(p1.x,p1.y)
#建立第二個實體物件
p2=point(9,7)
print(p2.x,p2.y)
#建立第三個實體物件
p3=point(2,6)
print(p3.x+p3.y) #p就是實體物件，x、y是實體屬性名稱


#再進階，分開紀錄姓、名的資料全名
class fullname:
    def __init__(self):
        self.first="Yuan"
        self.last="Ryan"
name1=fullname()
print(name1.first,name1.last)


class fullname1:
    def __init__(self,first,last):
        self.first=first
        self.last=last
name1=fullname1("Yuan","Ryan")
print(name1.first,name1.last)
name2=fullname1("NNN","YYY")
print(name2.first,name2.last)
