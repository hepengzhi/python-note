#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
#列表生成器
#但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？
#>>> L = []
#>>> for x in range(1, 11):
#...    L.append(x * x)
#...
#>>> L
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
lista=[x * x for x in range(1,10)]
print(lista)

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
listb=[x * x for x in range(1, 11) if x % 2 == 0]
print(listb)

#还可以使用两层循环，可以生成全排列：
listc= [m + n for m in 'ABC' for n in 'XYZ']
print(listc)

#把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
LN=[s.lower() for s in L]
print(LN)