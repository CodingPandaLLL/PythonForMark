# -*- coding:utf-8 -*-  
'''
Created on 2018-04-13
@author: lll
'''
from telnetlib import BM
print("你好 世界")

name=["lll","gx","zj","xx"]
print(name[-2])

# 判断测试 
xmTail=1.75
xmWight=80.5
BMI=xmWight/(xmTail*xmTail)
print(BMI)

if BMI<18.5:
    print("小明过轻")
elif BMI>=18.5 and BMI<25:
    print("小明正常")
elif BMI>=25 and BMI < 28:
    print("小明过重")
elif BMI>=28 and BMI < 32:
    print("小明肥胖")
else :
    print("小明严重肥胖")
    
# 循环测试  
names=["xiaoli","dali","li","guan"]
for name in names:
 print(name)
numbers=[1,2,3,4,5]
# range(5)函数是生产序列数方法
for number in range(5):
    print(number)
# python中的dict 类似java中的map
dict = {'Michael': "kjksd",'Bob': "kkkk",'Tracy': "ooxx"}
print( dict['Michael'])
# 判断可以是否存在
print('Thomas' in dict)
# 如果jjk不存在返回None
print(dict.get("jjk"))
# 删除dict中的值
dict.pop('Bob')
print(dict)

# set 类似于数组无序 不重复
s = set([1, 2, 3])
print(s)
s.add("s")
print(s)
s.remove("s")
print(s)
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print("s1取交集 ")
print(s1 & s2)
print("s1取并集 ")
print(s1 | s2)