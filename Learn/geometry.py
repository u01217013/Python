# 在這個模組中定義幾何運算功能
#module.py的模組檔案
def distance(x1,y1,x2,y2):     
    return ((x2-x1)**2+(y2-y1)**2)**0.5    #算2點距離
def slope(x1,y1,x2,y2):
    return(y2-y1)/(x2-x1)  #算斜率
