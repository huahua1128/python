# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 20:21
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_变量的作用域.py
#局部变量
#全局变量
#湖南都是晴天 除了长沙是雨天
#全局变量：晴天
#局部变量：雨天

#全局变量生效的范围大于局部变量
#当局部变量存在的时候，优先取局部变量

# python里面的全局和局部
#函数外的是 全局变量
#函数内的是 局部变量
offer=1#全局变量

def student_info(class_name,name):#A
# 调用A 这一块代码的时候 才会涉及到去修改offer值
    global offer#声明全局变量
    offer=20#局部变量 在函数内部--->加了一个global 就变成了全局
    print('{}期的{}同学拿到了{}k的offer！！！恭喜恭喜!!'
          .format(class_name,name,offer))

def student_record():#记录最高薪资  B
    print('目前柠檬班要打破{}记录才能晋升为最高薪资offer'.format(offer))

student_record()#B
student_info('13','不忘初心')#A
print(offer)#C

#怎么去区分局部变量还是全局变量

#函数外的是 全局变量  哪里都可以用只要在当前的Python的文件内
#函数内的是 局部变量  他只能作用在函数里面
#当全局变量和局部变量同时存在的时候，优先取局部变量

# global 声明 函数内部的局部变量---变成全局变量

#使用场景：两个请求同时用了一个变量，
# 如果第二个请求用的是第一个请求改变过后的变量值