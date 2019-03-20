#enconding: utf-8
#name:  huahua
#enconding: utf-8
#name:  huahua

import   random
class  Online_Retailers:   #父类
    '这是个电商类，有它的属性以及对应的功能'
    def  __init__(self,name1='京东',feature1='Electronic product',boss1='刘强东'): #初始化函数
        self.name1 = name1  #平台名称
        self.feature1 = feature1   #平台特征
        self.boss1 = boss1   #创始人


    def  login_in(self,username000,pwd000):    #登录功能   静态方法
        #用户名：huahua   密码：123456
        if username000 == 'huahua' and  pwd000 == '123456':
            print("Congratulations on your successful login！")
            res123=True
        else:
            print("Sorry for the incorrect account or password you entered.，Login failed")
            res123 = False
        return   res123

    def pay_method(self,paymethod0):  #支付
        try:
            if  paymethod0 == '微信':
                print("WeChat payment")   # 微信支付
            elif  paymethod0 == '支付宝':
                print("Alipay payment")     #支付宝支付
            elif  paymethod0 == '银联':
                print("UnionPay payment")    # 银联支付
        except Exception  as  e:
            print("The data you entered is incorrect.")

        return  paymethod0

    def  discount(self):   #优惠券
        money=random.randint(10, 50)
        return money


class  JingDong123(Online_Retailers):  #京东类继承电商类
    '这个是京东类，有它的的属性和功能'

    def  settlement(self,price,zhanghao,mima):   #结算功能   拓展
        print("Welcome to Jingdong Mall！！！")
        var=JingDong123().login_in(zhanghao,mima)
        if  var:
            while True:
                my_paymethod=input("Please choose your payment method.（微信，银联，支付宝）：")
                pay_res = JingDong123().pay_method(my_paymethod)
                if  pay_res=='微信':
                    discount = JingDong123().discount()
                    if price > discount:
                        print("Congratulations on the {} yuan discount，final payment amount is: {}".format(discount,price-discount))
                        return  discount
                    else:
                        print("There is no discount on your purchase amount，final payment amount is ：{}",price)
                        return  discount
                    break
                elif pay_res=='银联' :
                        print("There is no discount on your purchase amount，final payment amount is :{}".format(price))
                        return  0
                        break
                elif pay_res=='支付宝':
                    print("Sorry.This payment method is not supported，please re-select the mode of payment")
        else:
            return  False



if  __name__=='__main__':
    JingDong123().settlement(240,'huahua','123456')  #调用京东类实现功能


