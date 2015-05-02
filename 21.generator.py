#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
#生成器即是在列表生成式中的[]，改为（）
L=(x * x for x in range(10))
#>>> L
#<generator object <genexpr> at 0x10c52aa50>
#>>> L.next()
#0
#>>> L.next()
#1
#>>> L.next()
#4
#通过next()函数调用下一个结果，不过这种方法太变态
#可以通过for循环来实现
for i in L:
	print i