#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
#filter()也接收一个函数和一个序列。和map()不同的时，
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
#
#过滤出列表中的奇数
def is_odd(n):
    return n % 2 == 1

L=filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])
print(L)
# 结果: [1, 5, 9, 15]

#过滤空字符
def not_empty(s):
    return s and s.strip()

M=filter(not_empty, ['A', '', 'B', None, 'C', '  '])
print(M)
# 结果: ['A', 'B', 'C']