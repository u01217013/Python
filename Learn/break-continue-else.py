#break、continue一定要放在迴圈內，break是強制結束迴圈、continue是強制繼續迴圈
#while回圈 #command+/ 可以將全部程式碼變註解
n=0
while n<5:
    if n==3:
        break
    print(n) #印出回圈中的n
    n+=1
print("最後的n:",n) #印出回圈結束後的n

#for回圈
x=0
for y in [0,1,2,3]:
    if y%2==0: #y是偶數
        continue
    print(y)
    x+=1
print("最後的x：",x)

#else 是加在迴圈最後面（不再迴圈內），在迴圈結束前，先跑完else在結束回圈
sum=0
for n in range(1,11):
    sum+=n
else:
    print("總和：",sum)

#綜合範例，找出整數平方根
#讓使用者輸入可以得到平方根
#輸入9,得到3
#輸入25,得到5
#輸入11,得到沒有 （練習而已，先用沒有）
x=input("請輸入數字：")
x=int(x) #轉換成整數
for i in range(26):
    if i*i==x:
        print("整數平方根為：",i)
        break #用break強制結束回圈，就不會執行else區塊
else:
        print("沒有整數平方根，請重新輸入")













