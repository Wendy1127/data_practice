#coding:utf-8
#已知大公鸡5元，母鸡3元，小鸡1元，我有100块，可能买几只公鸡，几只母鸡，几只小鸡，把所有的可能都显示出来。
#i 表示公鸡，j表示母鸡，k表示小鸡
# for i in range(0,21):
#     for j in range(0,34):
#         for k in range(0,101):
#             #pass    #空操作，占位
#             if 5*i+3*j+k==100:
#                 print u'公鸡有：%d只，母鸡有：%d只，小鸡有：%d只'%(i,j,k)

#百元买白鸡，已知公鸡5元，母鸡4元，3只小鸡1元，100块买100只鸡，可能买几只公鸡，几只母鸡，几只小鸡
for i in range(0,21):
    for j in range(0,26):
        for k in range(0,301):
            #pass    #空操作，占位
            if (5*i+4*j+0.3*k==round(100)) and (i+j+k=100):
                print u'公鸡有：%d只，母鸡有：%d只，小鸡有：%d只'%(i,j,k)