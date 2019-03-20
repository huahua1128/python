# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 20:59
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_02_variable.py
#变量名：我们命名一个标识符 存储一个数据  变量名
#数字 字符串 列表 元组 字典 集合等各种类型的数据
# a=1
# b=1
# print(id(a))
# print(id(b))
# #
# a=1
# a=2
# print(a)

#数字：整型 浮点型
#整型 int
b=100
#安利一个  帮你判断数据类型的函数 type(数据)

# 浮点型 float
a=10.0
# print(type(a))

#字符串 str string
#成对的单引号 双引号 以及三引号括起来的内容都是字符串
c='10'
d="hello ai"
e="""10.0000"""
f='''66666
999
0000
0000
'''
# print(type(e))

#如果你的字符串里面必须包含单引号  最外层用双引号
#如果你的字符串里面必须包含双引号  最外层用单引号
x='"hello"'
print(x)
