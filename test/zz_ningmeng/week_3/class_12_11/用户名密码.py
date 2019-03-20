# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 22:09
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_用户名密码.py

# 4：用户的登录信息存在在字典里面，例如{"admin":"lemon","huahua":"123456"}，
# 用户名：admin 对应密码：lemon
# 用户名：huahua对应密码：123456
# 根据上述信息以及下列条件写出符合题目的程序代码：
# 1）设计1个登陆的程序， 不输同的用户名和对成密码存在个字典里面，入正确的用户名和密码去登陆，
# 2）首先输入用户名，如果用户名不存在或者为空，则一直提示输入正确的用户名
# 3）当用户名正确的时候，提示去输入密码，如果密码跟用户名不对应， 则提示密码错误请重新输入。
# 4）如果密码输入错误超过三次，中断程序运行。
# 5）当输入密码错误时，提示还有几次机会
# 6）用户名和密码都输入正确的时候，提示登陆成功!'''

user_info={"admin":"lemon","huahua":"123456"}
while True:
    name=input('请输入用户名:')
    if name in user_info.keys():
        count=0
        while count<3:
            pwd=input('请输入密码:')
            if pwd==user_info[name]:
                print('登录成功！！！')
                break
            else:
                count+=1
                print('密码输入错误，请重新输入,还有{}次输入机会'.format(3-count))
    else:
        print('请输入正确的用户名')
        continue
    break