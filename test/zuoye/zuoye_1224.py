#enconding: utf-8
#name:  huahua

import   random
class  Online_Retailers:   #父类
    '这是个电商类，有它的属性以及对应的功能'
    def  __init__(self,name='京东',feature='电子产品',boss='刘强东'): #初始化函数
        self.name=name  #平台名称
        self.feature=feature   #平台特征
        self.boss=boss   #创始人

    @staticmethod
    def  login_in(username,pwd):    #登录功能   静态方法
        #用户名：huahua   密码：123456
        if username == 'huahua' and  pwd == '123456':
            print("恭喜您登录成功！")
            res=True
        else:
            print("抱歉您输入的账号或者密码有误，登录失败")
            res=False
        return   res

    def pay_method(self):  #支付
        try:
            method=int(input("请您选择支付方式：（1：微信支付，2：支付宝支付，3：银联支付）"))
            if  method==1:
                print("微信支付")   # 微信支付
            elif  method==2:
                print("支付宝支付")     #支付宝支付
            elif  method==3:
                print("银联支付")    # 银联支付
        except Exception  as  e:
            print("您输入的数据有误，请重新输入")
            Online_Retailers().pay_method()
        return  method

    @classmethod
    def  discount(cls):   #优惠券
        print("支付成功。恭喜您获得了一张金额为{}的优惠券".format(random.randint(10,50)))



class  JingDong(Online_Retailers):  #京东类继承电商类
    '这个是京东类，有它的的属性和功能'

    @staticmethod
    def  settlement():   #结算功能   拓展
        print("欢迎来到京东商城！！！")
        username = input("请输入您登录的用户名：")
        pwd = input("请输入您的登录密码：")
        result=JingDong.login_in(username,pwd)
        if  result:
            input("请您输入的购买金额：")
            while True:
                pay_res = JingDong().pay_method()
                if  pay_res==1:
                    JingDong.discount()
                    break
                elif pay_res==3:
                    print("结算成功。您的支付方式没有优惠")
                    break
                elif pay_res==2:
                    print("很抱歉，我们暂时不支持该支付方式，请重新支付")




class  TaoBao(Online_Retailers):   #淘宝类继承电商类
    '这个是淘宝类，有它的的属性和功能'

    @staticmethod
    def settlement():  # 结算功能   拓展
        print("欢迎来到淘宝！！！")
        username = input("请输入您登录的用户名：")
        pwd = input("请输入您的登录密码：")
        result = TaoBao.login_in(username,pwd)
        if result:
            input("请您输入的购买金额：")
            while True:
                pay_res = TaoBao().pay_method()
                if pay_res == 2:
                    TaoBao.discount()
                    break
                elif pay_res == 3:
                    print("结算成功。您的支付方式没有优惠")
                    break
                elif pay_res == 1:
                    print("很抱歉，我们暂时不支持该支付方式，请重新支付")



if  __name__=='__main__':
    JingDong.settlement()   #调用京东类实现功能
    TaoBao().settlement()  # 调用淘宝类实现功能

