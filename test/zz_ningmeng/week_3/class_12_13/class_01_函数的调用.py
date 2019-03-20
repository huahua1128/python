# -*- coding: utf-8 -*-
# @Time    : 2018/12/13 19:47
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_函数的调用.py

def student_info(class_name,name,offer):
    print('{}期的{}同学拿到了{}k的offer！！！恭喜恭喜!!'
          .format(class_name,name,offer))

    eat('玉米','可乐','必胜客','周黑鸭')#函数的相互调用


def eat(*food_name):#动态参数
    food_name_str=''#存储我放进来的食物列表
    for item in food_name:
        food_name_str+=item
        food_name_str+='、'
    food_name_str=food_name_str.strip('、')
    print('最喜欢吃：{}'.format(food_name_str))


if __name__ == '__main__':
    student_info('13','w.','22')
