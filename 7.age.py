#!/usr/bin/env python
#if >18 print adult else print teenager
#
age=input("please input your age: ")
if isinstance(age,int):
    if age>=18:
        print("Adult!")
    else:
        print("teenager.")
else:
    print("Age is not integer")