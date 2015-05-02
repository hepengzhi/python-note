#!/usr/bin/env python
#-*- coding:utf-8 -*-
#calcultate n*n or n*n*n...
#def power(x):
#	return(x*x)
import math
#默认参数，power(10),power(10,2)
def power(x,n=2):
	sum=1
	for i in range(n):
		sum=sum*x
	return(sum)
import math
#默认参数不能是可变的对象，如list等
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L

#可变参数,计算a^2+b^2+c^2...(只需要在原函数的基础上加一个*),通过calc(1,2,3)直接调用，而不用[]或()
def calc(*numbers):
	sum=0
	for i in numbers:
		sum=sum+i*i
	return(sum)

#关键字参数，关键字参数作为dic传入,关键字参数可以省略
def person(name,age,**kw):
	print 'name:',name,'age:',age,'other:',kw

#>>> kw = {'city': 'Beijing', 'job': 'Engineer'}
#>>> person('Jack', 24, **kw)
#name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}

#如果包含4中参数,参数的位置应该为：必选参数，默认参数，可变参数，关键字参数
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
