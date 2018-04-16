# 函数的定义和调用
from _ast import Num
def sum_seris(x):
    sum=0
    for number in range(x):
        print(number)
        sum = sum + number
    return sum
# 调用函数
print(sum_seris(10))
# 不做任何处理用pass
def Test_number(x):
    s=0
    if x==5:
        s=100
    elif x==10:
        s=1000
    else:
        pass
    return s
print(Test_number(11))
# 参数检查
def Test_number1(x):
    if not isinstance(x, (int, float)):
        raise TypeError('参数类型不对')
    s=0
    if x==5:
        s=100
    elif x==10:
        s=1000
    else:
        pass
    return s
print(Test_number1(11))
# python可以有多个返回值

# 默认返回值
def infor(name,gender,age=7,city="wuhan"):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)
    
print(infor("lll","n"))
print(infor("zj","w",6))
print(infor("gx","w",6,'hefei'))

