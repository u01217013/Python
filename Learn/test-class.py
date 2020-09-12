#類別：封裝變數或函式（封裝的變數或函式，統稱類別的屬性）
#要先定義類別，再來才能使用類別中封裝的屬性 
#定義類別
#class 類別名稱:
    #定義封裝的變數
    #定義封裝的函式

#使用類別
#類別名稱.屬性名稱

# #範例 定義Ｔest類別 
# class Test:
#     x=3 #定義變數
#     def say(): #定義函式
#         print("hello")

# #範例 使用Test類別
# print(Test.x+3)#取得屬性x的資料3
# Test.say() #呼叫屬性say的函式

#以上是基本的，以下為影片範例
#定義類別與類別屬性（封裝在類別中的變數和函式）
#定義一個類別Io，有兩個屬性，supportedSrcs和read
class Io:
    supportedSrcs=["console","file"]
    def read(src):
        print("Read from:",src)
#使用類別
print(Io.supportedSrcs)
Io.read("file")

#以下為更進階
class Io:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in Io.supportedSrcs:
            print("Not Supported")
        else:
            print("Read from:",src)
#使用類別
print(Io.supportedSrcs)
Io.read("file")
Io.read("internet")

