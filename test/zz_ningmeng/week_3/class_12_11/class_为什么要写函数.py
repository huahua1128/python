# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 20:09
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_为什么要写函数.py

def count_number():
    count=0
    for i in range(1,100):#i=1
        count+=i#count=count+i
    print('计算结果是：{}'.format(count))
    return count#隐式的添加

print(count_number()+666)

#1:return后面的代码不再执行，所以我们的有效代码要放在return前面
#2：return表示函数的结束

#什么时候用return？
#想用就用

#函数里面 return的表达式个数 支持0个或多个
# 如果你的函数里面没有写return  就会隐式的添加一个return 返回None
#==1 返回你指定的数据类型
#>1  返回的是元组类型，用逗号区分
#==0 返回None
