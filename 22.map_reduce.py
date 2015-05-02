#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
#map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，
# 并把结果作为新的list返回。
def fa(x):
	return x * x
L=map(fa,[1,2,3,4,5,6,7,8,9,10])
print(L)

M=map(str,[1,2,3,4,5,6,7,8,9,10])
print(M)

#reduce:
#reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，
# reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
def fb(x,y):
	return x+y

N=reduce(fb,[1,2,3,4,5])
print(N)