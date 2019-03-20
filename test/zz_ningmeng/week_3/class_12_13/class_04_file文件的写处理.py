# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 21:29
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_04_file文件的写处理.py

# open()函数
# 文件打开的模式
#只读模式的情况下 去进行写操作  io.UnsupportedOperation: not writable
#r  只读   r+   读写
# file=open('python13.txt','r+',encoding='UTF-8')
# print(file.readline())
# file.write('胡萝卜好好吃')
# # 先读在写 写在最后面
# # 先写  覆盖写


#w 只写    w+   读写  只写的模式下去进行操作 就会报错 io.UnsupportedOperation: not readable
# file=open('python13.txt','w+',encoding='UTF-8')#如果文件名存在 先清空文件 再做其他操作
# file.write('好呀零食，纪念我美好的时光！')
# file.seek(6,0)#重新改变光标的位置 移动的量  相对位置 0开头  【1当前位置  2尾巴】--二进制文件
# print(file.read())
# file=open('python13.txt','r',encoding='UTF-8')
# print(file.read())
file=open('yu.txt','w')#如果文件不存在的话 可以新建文件
# file.close()#记得关闭文件


#ASCII编码 1个英文1个字节
#GBK编码 支持中文
#UTF-8编码  1个字符要占3个字节

#ASCII-GBK
#ascii-->decode -->UTF-8-->encode--> gbk

#a 只能追加写  a+  读写
file=open('python13-8.txt','a+',encoding='utf-8')
# file.write('isnns 的名字好长啊！')
# file.seek(0,0)
print(file.read())

#什么时候才会用到这玩意？
#写日志 生成html报告的时候的会用到