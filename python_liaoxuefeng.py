## print 1024 * 768
print('1024 * 768 =', 1024*768)

## %s,%d
text = 'Hi, %s, you have $%d.' % ('jack', 1000)
print(text)

## 小明的成绩提升率：（之前72，现在85，提升了多少，  %  后面传递变量
s1 = 72
s2 = 85

r = (s2-s1)/s2*100
print('%.2f%%' % r)

## list,tupe,打印序列
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])


## 利用判断，根据bmi公试计算体重：
print('很多人以为直到失去你才知道拥有过什么，而事实上，你一直知道你拥有什么，只是你以为你永远不会失去\n'*2)

s1=input('输入你的身高（m）：')
s2=input('输入你的体重（kg）：')
height=float(s1)
weight=float(s2)
bmi=weight/(height**2)
if bmi<18.5:
    print ('过轻')
elif 18.5<=bmi<25:
    print('正常')
elif 25<=bmi<28:
    print('过重')
elif 28<=bmi<32:
    print('过胖')
else:
    print('严重肥胖')

## for 迭代练习

names = ['jack', 'zhudy', 'gavin']
for name in names:
    print(name

sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

l = list(range(5))
print(l)

sum = 0
for x in range(11):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

L = ['Bart', 'Lisa', 'Adam']

for name in L:
    print('Helo %s!' % name)

## for 迭代用户法
迭代：

>>> [x * x for x in range(1, 11)]
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

>>> [m + n for m in 'ABC' for n in 'XYZ']
['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

>>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
>>> for k, v in d.items():
...     print(k, '=', v)
...
y = B
x = A
z = C

## **kv 关键词参数：
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(person('Michael', 30))

print(person('Bob', 35, city='Beijing'))

## 函数的参数传递（需要深入的研究一下）：
## *args是可变参数，args接收的是一个tuple；
## **kw是关键字参数，kw接收的是一个dict。
## 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
