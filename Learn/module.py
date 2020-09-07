#獨立的程式檔案，可以被其他的程式載入、使用，且可重複使用
#先載入模組，再使用模組中的函示模組中的函式或變數
#import 模組名稱 #模組名稱一般就是檔案名稱
#import 模組名稱 as 模組別名
#使用模組 > 模組名稱或別名.函式名稱(參數資料) or 組名稱或別名.變數名稱
#內建模組 sys模組-可取得系統相關資訊
import sys 
print(sys.platform)
print(sys.maxsize)

# import sys as s
# print(s.platform)
# print(s.maxsize)


#自訂模組 -建立幾何運算模組 geometry.py
# import geometry as g
# result=g.distance(1,1,5,5)
# result1=g.slope(1,2,5,6)
# print(result)
# print(result1)

#調整搜尋模組的路徑
# import sys 
# print(sys.path) #印出模組的搜尋路徑列表

#將geometry丟進modules資料夾內，Ｐython搜尋路徑就找不到了，所以要操作path
import sys
sys.path.append("modules") #在模組的搜尋路徑列表中『新增路徑』
print(sys.path)
import geometry as g
print(g.distance(1,1,5,5))





