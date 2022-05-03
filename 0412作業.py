# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:38:19 2022

@author: 123
"""
"""
1
22
333
4444
55555
"""

for i in range(1,6): #[1,2,3,4,5]
    for x in range(i): # i 是多少 就執行幾次
        print(i,end="")
    print()
    
print("-"*30)

"""
55555
4444
333
22
1
"""
for i in range(5,0,-1): #[5,4,3,2,1]
    for x in range(i): #i是多少就執行幾次
        print(i,end="")
    print()

print("-"*30)
"""
999999999
7777777
55555
333
1
"""    
for i in range(9,0,-2): #間隔值 -2
    for x in range(i):  #[0,1,2,3,4,5,6,7,8]
        print(i,end="") #end="" 印完後，不做斷行動作
    print()
    
print("-"*30)
     
    
    
#求1~100之間的質數 
# 只能被 1 及自己整除，其他的值都不可以整除它
#例:11 將 11之前的數拿出來除
# 11/2,11/3,11/4,11/5,11/6,11/7,11/8,11/9,11/10

#以12來說
# i = 12
#12/2,12/3,12/4,12/5,....,12/11
for i in range(1,101): #[2,3,...,100]
    isR = True #我先定義要進來的每一個值都是質數，所以設為True
    for x in range(2,i): #從2開始到i-1結束 若:i=10 ==> 2,3,4....9
        if i % x == 0:
            isR = False  #只要是False 時，表示該數 i 不是質數
                        
    #if isR == True:        
    if isR:  # 因為 isR 他是布林值。所以直接判斷
        print(i,"是質數")