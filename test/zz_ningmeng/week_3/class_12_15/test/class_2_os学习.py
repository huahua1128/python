# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 10:21
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_2_os学习.py

#绝对路径 相对路径的区别
# f1=open('../python13.txt',encoding='utf-8')#相对路径
# print(f1.read())
#
# print('*'*50)
#
# #绝对路径
# f2=open(r'D:\2018Python自动化课件&代码\code\python_13\week_3\class_12_15\python13.txt',encoding='utf-8')
# print(f2.read())

import os

# #可以获取到文件的绝对路径  __file__表示当前模块文件  具体到文件名（模块名）
# real_path=os.path.realpath(__file__)
# print('绝对路径    :',real_path)
#
# pwd_path=os.getcwd()#具体到当前工作目录
# print('当前工作目录:',pwd_path)
#
# file_list=os.listdir(pwd_path)#返回值是列表
# print('当前目录的所有文件名：',file_list)
#
# for file in file_list:
#     if os.path.isdir(file):#判断文件是否是文件夹  返回值是布尔值
#         print('{},是一个文件夹'.format(file))
#     elif os.path.isfile(file):#判断文件是否是文件 返回值是布尔值
#         print('{},是一个文件'.format(file))
#

#新建 删除 mkdir rmdir
# os.mkdir('whereas')#make directory
# os.rmdir('whereas')#remove directory

#多级新建  不能跨级创建文件夹 必须一级一级，
# 如果一定要跨级新建的时候  要注意前面的路径已经存在，否则报错
# 删除的时候 要注意 是否没有子目录 为空 ---问题：非空目录是否支持强制删除--自己去拓展
# os.mkdir('whereas/AI')#make directory
# os.rmdir('whereas')#remove directory

pwd_path=os.getcwd()#具体到当前工作目录
print(pwd_path)

# print(os.path.join(pwd_path,'那年夏天'))#拼接路径 os.path.join(prefix,suffix)
# os.mkdir(os.path.join(pwd_path,'那年夏天'))

print("拼接后的路径",pwd_path+'\幽幽')
os.mkdir(pwd_path+'\幽幽')