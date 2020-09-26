# 單維度資料 series ：：就像是一個列表、或是試算表excel中的欄位資料
# 使用方法
# 載入pandas模組
# import pandas as pd
# 以列表資料為底，建立series
# data=pd.Series(列表)
# data.max() #找到最大值



# 雙維度資料 DataFrame : 就是一個完整列表，有欄、列的資料
# 使用方法
# 載入pandas模組
# import pandas as pd
# 以字典資料為底，建立DataFrame
# data=pd.DataFrame(字典)
# data["欄位名稱"] 取得特定欄位
# data.iloc[列編號] 列編號按順序由0開始累加 取得特定的列




#載入pandas 模組
import pandas as pd
#建立Series
data=pd.Series([20,10,15])
# 基本 Series 操作
# print(data)
# print(data.max()) #最大值
# print(data.median()) #中位數
# print(data*2)
data=data==20 #data有沒有等於20的資料
print(data)

#建立DataFrame 
data1=pd.DataFrame({
    "name":["Amy","John","Bob"],#字典就是Key:Value 在這裡的Key="name",Value="Amy","John","Bob"
    "salary":[30000, 50000, 40000]
})
# 基本 DataFrame 操作
print(data1)
print("===========")
#取得特定的欄位
print(data1["salary"]) #取得薪資欄
print("===========")
#取得特定的列
print(data1.iloc[0]) #取得第一列
