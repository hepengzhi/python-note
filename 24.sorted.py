#!/usr/bin/env python
#-*- coding:utf-8 -*-
#
#排序也是在程序中经常用到的算法。无论使用冒泡排序还是快速排序，
# 排序的核心是比较两个元素的大小。如果是数字，我们可以直接比较，
# 但如果是字符串或者两个dict呢？直接比较数学上的大小是没有意义的，
# 因此，比较的过程必须通过函数抽象出来。通常规定，对于两个元素x和y，
# 如果认为x < y，则返回-1，如果认为x == y，则返回0，如果认为x > y，
# 则返回1，这样，排序算法就不用关心具体的比较过程，而是根据比较结果直接排序。
#数字排序：
L=[36, 5, 12, 9, 21]
M=sorted(L)
print(M)
#数字倒序排序，需重新定义比较条件
def reverse_cmp(x,y):
	if x<y:
		return 1
	if x>y:
		return -1
	return 0

N=sorted(L,reverse_cmp)
print(N)

#字符串排序：
S=sorted(['bob', 'about', 'Zoo', 'Credit'])
print(S)
def ignore_case(s1,s2):
	u1=s1.upper()
	u2=s2.upper()
	if u1>u2:
		return 1
	if u1<u2:
		return -1
	return 0

U=sorted(S,ignore_case)
print(U)