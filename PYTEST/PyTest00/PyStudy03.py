#python 中的切片操作符slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])
print(L[:3])
print(L[0:])
LL=L = list(range(100))
print(LL[:10:2]) #前10个数，每两个取一个
print(LL[::5]) #取所有，每五个取一个

# 列表生成式代替循环
print([x * x for x in range(1, 11)])

#for循环后面还可以加上if判断 仅偶数的平方
print([x * x for x in range(1, 11) if x % 2 == 0])

#双重循环
print([m + n for m in 'ABC' for n in 'XYZ'])

#判断是否为数字或者字母
#用isdigit函数判断是否数字
str_1 = "123"
str_2 = "Abc"
str_3 = "123Abc"
print(str_1.isdigit())
#用isalpha判断是否字母
print(str_1.isalpha())  
#isalnum判断是否数字和字母的组合
print(str_1.isalpha())  

#生成器
g = (x * x for x in range(10))
print(next(g)) 
