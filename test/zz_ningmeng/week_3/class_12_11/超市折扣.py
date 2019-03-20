# -*- coding: utf-8 -*-
# @Time    : 2018/12/11 21:22
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : 超市折扣.py

# 1：一家商场在降价促销。
# 如果购买金额50-100元(包含50元和100元)之间，会给10%的折扣，
# 如果购买金额大于100元会给20%折扣。
# 编写一程序，询问购买价格，再显示出折扣（%10或20%）和最终价格
#只考虑整数

#写成一个函数  最大化的复用
def discount(min,max,discount_1,discount_2):
    while True:
        total=input('请输入你的购买总价：')
        if total.isdigit():
            total=int(total)#强转一下
            if min<=total<=max:
                print('你购买的总价是：{}，可以享受{}%的折扣，优惠后价格为：{}'
                      .format(total,discount_1,total*(1-discount_1/100)))
            elif total>max:
                 print('你购买的总价是：{}，可以享受{}%的折扣，优惠后价格为：{}'
                      .format(total,discount_2,total*(1-discount_2/100)))
            else:
                print('你购买的总价是：{}，不享受任何折扣!'.format(total))
            break#结束循环
        else:
            print('请输入数字')
discount(100,200,50,80)

#浮点数怎么办?