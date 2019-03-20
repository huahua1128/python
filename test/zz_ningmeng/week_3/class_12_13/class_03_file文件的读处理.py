# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 21:02
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_03_file你文件的处理.py

#file：txt 日志 不包括mp4 excel html
#处理：读、写
#什么时候用呢 ：想用就用

#存储数据的操作  #有中文的时候 注意设置编码为 utf-8
#第一步：打开文件 open() file
file=open('python13.txt',encoding='UTF-8')#我打开的这个文件存在file变量里面
# print(file.read())#默认是读取文件中的所有内容，保持格式
# print('***********************')
# print(file.read(5))#读取指定长度的内容
# print('***********************')
# print(file.readline())#按行读取,每次只能读一行的内容
# print('***********************')
# print(file.readline())

# print(file.readlines())#按行读取,读完所有行--返回列表 每一行是列表的一个元素
# \n 换行符
# for item in file.readlines():
#     print(item)

#小练习：读出前10行诗句 怎么读？
# for i in range(10):
#     print(file.readline())

# count=0
# while count<10:
#     print(file.readline())
#     count+=1

#小练习：读出前5-8行诗句 怎么读？
# for i in range(10):# 5 6 7 8
#     if 5<=i<=8:
#         print(file.readline())
#     else:
#         file.readline()

file.write('差不多先生就是这66666')