#搭配教學第12集
#封包就是包含模組的資料夾：用來整理、分類模組程式 > 檔案對應到模組，資料夾對應到封包
#專案的檔案配置
#專案資料夾
#-主程式.py
#--封包資料夾
#---_init_.py #一定要有這個檔案，才會讓整個資料夾變成封包
#---模組一.py

#使用封包
#import 封包名稱.模組名稱
#import 封包名稱.模組名稱 as 模組別名

#主程式在此
import main.point
result=main.point.distance(3,4)
print("距離:",result)

import main.line
result1=main.line.slope(1,1,3,3)
print("斜率:",result1)