# f1=open('python13.txt',encoding='UTF-8') #相对路径
# print(f1.read())
#
# f2=open('E:\ZGH\\test\zgh\python13.txt',encoding='UTF-8') #绝对路径
# print(f2.read())

# f1=open('../apython13.txt',encoding='UTF-8')  #../返回上一层目录
# print(f1.read())
# f1.close()

import os

#获取当前文件的绝对路径  __file__表示当前文件
# real_path=os.path.realpath(__file__)
# print('绝对路径是',real_path)

# pwd_path=os.getcwd()  #具体到当前工作目录
# print('当前工作目录',pwd_path)
#
# file_list=os.listdir(pwd_path)  #pwd_path是当前工作目录
# print("当前目录的所有文件名：",file_list)
#
# for file in  file_list:
#     if os.path.isdir(file):  #判断是否是文件夹，返回值是布尔值
#         print("{},是一个文件夹".format(file))
#     if os.path.isfile(file): #判断是否是文件，返回值是布尔值
#         print("{},是一个文件".format(file))

# os.mkdir('world')  #新建文件夹在当前目录下
# os.mkdir('world/ai')  #新建ai时，必须保证world已经存在
# os.rmdir('world')   #删除当前目录下的文件夹
# os.rmdir('world/ai')   #删除ai,不能多级删除
# os.rmdir('world')   #删除world

#
# pwd_path=os.getcwd()  #具体到当前工作目录
# print('当前工作目录',pwd_path)
#
# # print(os.path.join(pwd_path,'那年夏天'))  #拼接路径（绝对路径）
# # os.mkdir(os.path.join(pwd_path,'那年夏天')) #在当前目录下新建文件
#
# print('2:',pwd_path+'\悠悠')
# os.mkdir(pwd_path+'\悠悠')   #在当前的目录下新建文件