#map()传入的第一个参数是f，即函数对象本身。
#由于结果r是一个Iterator，Iterator是惰性序列，
#因此通过list()函数让它把整个序列都计算出来并返回一个list。
from _functools import reduce
def f(x):
    return x+x 
r = map(f,[1,2,3])
print(list(r))

#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，
#这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def add(x,y):
    return x+y
print(reduce(add,[1,3,5,7]))

#练习把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字
def returnName(Str):
    rStr=''
    for n,x in enumerate(Str,1):
        if x.islower() and n==1:
            x=x.upper() 
        elif x.isupper() and n !=1:
            x=x.lower();
        rStr=rStr+x
    return rStr
print(returnName("admin"))
print(list(map(returnName,['adam', 'LISA', 'barT'])))

#upper()  ：将字符串转成大写，并返回一个拷贝
#lower()  ：将字符串转成小写，并返回一个拷贝
#capitalize() ：将字符串首字母，并返回一个拷贝
#title() ：将每个单词的首字母大写，并返回一个拷贝
#isupper() ：判断一个字符串是否是大写
#islower() ：判断一个字符串是否是小写

#filter()也接收一个函数和一个序列。和map()不同的是，filter()把传入的函数依次作用于每个元素
#，然后根据返回值是True还是False决定保留还是丢弃该元素。
def is_odd(n):
    return n % 2 == 1

print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
print(list(map(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

#Python内置的sorted()函数就可以对list进行排序
print(sorted([36, 5, -12, 9, -21]))
#绝对值大小排序
print(sorted([36, 5, -12, 9, -21], key=abs))
#倒序排列
print(sorted([36, 5, -12, 9, -21],reverse=True))
#字母排序可实现忽略大小写的排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

#关键字lambda表示匿名函数，冒号前面的x表示函数参数
print(list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#装饰器  
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper
@log
def now():
    print('2015-3-25')
print(now())

#偏函数 进制转换
def int2(x, base=2):
    return int(x, base)
print(int2('1010101'))

