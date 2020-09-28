#DataFrame:雙維度的資料，一個完整的列表，有欄有列

#載入Pandas模組
import pandas as pd

#資料索引：pd.DataFrame(字典,index=索引列表)
data=pd.DataFrame({
    "name":["Amy","Bob","Jamy"],
    "salary":[30000,50000,40000]
},index=["a","b","c"])
print(data)
print("========") #區隔用而已
#觀察資料
# print("資料數量",data.size)
# print("資料形狀（列,欄）",data.shape)
# print("資料索引",data.index)
#取得列(Row/橫向)的Series資料，根據順序 iloc，根據索引 loc
print("第二列資料",data.iloc[1],sep="\n")
print("========")
print("第c列資料",data.loc["c"],sep="\n")
#取得(Column/直向)的Series資料，根據欄位名稱
print("取得name欄位",data["name"],sep="\n")
#進階操作
names=data["name"] #取得單維度的Series資料
#開始進行Series的操作
print("全部轉大寫",names.str.upper(),sep="\n")
salaries=data["salary"]
print("薪水平均值",salaries.mean())

#建立新的欄位
data["revenue"]=[500000,600000,800000] #data[新欄位名稱]＝列表
data["rank"]=pd.Series([3,6,1],index=["a","b","c"])#data[新欄位名稱]＝Series的資料
data["CP"]=data["revenue"]/data["salary"]#計算員工ＣＰ值
print(data)





#建立新的欄位