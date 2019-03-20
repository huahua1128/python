# # a=int(input("请输入你的成绩："))
# # if a>=80:
# #     print("{0}分为优秀".format(a))
# # elif a>=60 and a<80:
# #     print("{}分为及格".format(a))
# # else:
# #     print("{}分为不及格".format(a))
# #
# # #print(type(a))
# #
# #
# # s=input("请输入一个整数:")
# # n=int(s)
# # if n%3==0 and n%5==0:
# #     print('{0}可以被3和5同时整除'.format(n))
# # else:
# #     print('{0}不可以被3和5同时整除'.format(n))
# #
# #
# #
# # s=input("请输入一个年份:")
# # year=int(s)
# # if (year%4==0 and year%100!=0) or year%400==0:
# #     print("{}是闰年".format(year))
# # else:
# #     print("{0}不是闰年".format(year))
# #
# # def ladd(a):
# #     sum=0
# #     for i in range(a+1):
# #         sum += i
# #     print("累加和为:{0}".format(sum))
# #     return sum
# # ladd(10)
#
# #1
# # def print_info():
# #     print("本章学习了python 的基础语法！")
# #
# # print_info()
#
# #2
# # def favorite_book(bookname):
# #     print("我最喜欢的书是"+bookname)
# #
# # favorite_book("平凡的世界")
#
# #3
# # def favorite_book(bookname="柠檬班python自动化教科书"):
# #    print("我最喜欢的书是"+bookname)
# #
# # favorite_book("平凡的世界")
#
# #4
# # def make_shirt(size,typeface):
# # #     print("这个t-shirt的尺码为:{0}，印刷的字样为:{1}".format(size,typeface))
# # #
# # # make_shirt("L","我是第一")
#
# #5
# # def  describe_city(cityname='chengdu',country='China'):
# #     print("{0} is  in  {1}".format(cityname,country))
# #
# # describe_city(country="China666")
# # describe_city("London","England")
# # describe_city('shanghai',"China")
# # describe_city("tianjin")
#
# #6
# # def city_country(cityname,country):
# #     return cityname,country
# #
# # res1=city_country("tianjin","China")
# # res2=city_country("London","England")
# # res3=city_country('shanghai',"China")
# # print(res1)
# # print(res2)
# # print(res3)
#
# #7
# # def make_album(name,album):
# #     d={name:album}
# #     return d
# #
# # res_1=make_album("张杰","逆战")
# # res_2=make_album("易烊千玺","舒适圈")
# # print(res_1)
# # print(res_2)
#
# #8
# # def make_album(name,album):
# #     d={name:album}
# #     return d
# # i=0
# # while  i<5:
# #     name=input("请输入歌手名：")
# #     album=input("请输入这个歌手的专辑名：")
# #     res=make_album(name,album)
# #     print(res)
# #     i+=1
#
# # #9
# # def food_print(*args):
# #     print("您添加的食材有：{}".format(args))
# #     print(type(args))
# # food_print('香蕉',"苹果","面包","火腿")
# # food_print("芝士","鸡蛋")
# # food_print("午餐肉")
#
#
# #10
# # def  make_car(maker,model,**kwdargs):
# #     print(maker,model,kwdargs)
# #
# # # car=make_car("subaru","outback","color"="blue","tow_package"="True")
# # make_car("subaru","outback",color="blue",tow_package="True")
#
# # t=("hello","nihao")
# # print('@'.join(t))
# # L=["123","45","hello"]
# # print('*'.join(L))
# # lk="hellowejh,ki"
# # print('6'.join(lk))
#
# # T=12
# # def add():
# #     global T
# #     T=10
# #     print(T)
# #
# # add()
# # print(T)
# #
# # T=12
# # def add():
# #     T=10
# #     print(T)
# #
# # add()
# # print(T)
#
# # list_1=["nihao",1,"加油",25]
# # def  add():
# #     list_1[0]="明天"
# #     list_1.pop(2)
# #     print(list_1)
# #
# # add()
# # print(list_1)
#
# # list_1 = {"nihao":1,"加油":25}
# # list_1.update([('s33even',12)])
# # list_1.update(name=123,ss="hhh")
# # print(list_1)
#
# # str='dsfdf'
# # str=str.strip()
# # print(str)
# # print(222)
# # print("\r")
# # print(666)
#
#
# # def file_1(file):
# #     f=open(file,"r+")
# #     s=[]
# #     for i  in f.readlines():
# #         d={}
# #         print(i)
# #         print(i.strip('\n').split(','))
# #         for j  in  i.strip('\n').split(','):
# #             d[j.split(':',1)[0]]=j.split(':',1)[1]
# #         s.append(d)
# #     f.close()
# #     return  s
# #
# # print(file_1("file.txt"))
#
# # def student_info(class_name,name,offer):
# #     print("{}期的{}同学拿到了{}k的offer!恭喜恭喜".format(class_name,name,offer))
# #
# #     eat("可乐",'花生','薯片')
# #
# # student_info('python13','小花花',20)  #这个函数调用放在这里会报错，还未定义eat函数
# #
# # def eat(*food_name):   #传进来是元组
# #     food_name_str=''   #存储传进来的食物列表
# #     for item in food_name:
# #         food_name_str+=item
# #         food_name_str+='、'
# #     food_name_str=food_name_str.strip('、')    #去掉最后的顿号，方法一，也可以用for
# #     print("最喜欢吃：{}".format(food_name_str))
# #
# # student_info('python13','小花花',20) #这个函数调用放在这里不会报错，按顺序向下执行，eat已定义
# # # eat("煎饼",'小鱼干','火锅','玉米')
# #
# # def student_info(class_name,name,offer):
# #     print("{}期的{}同学拿到了{}k的offer!恭喜恭喜".format(class_name,name,offer))
# #
# #
# # def student_record(offer):  #记录最高薪资
# #     print("目前的最高薪资是{}".format(offer))
#
# # try:
# #     print(a)
# #     print(b)
# #
# # except:
# #     print("****")
# #     print(666)
#
# # try:
# #     # a=222
# #     print(a)
# # except  Exception as e:
# #     print("错误:%s"%e)
# #     raise e
#
# # def redPackage(money=input("请输入红包金额：")):
# #     try:
# #         f=float(money)
# #
# #         if f>=0.01 and f<=200:
# #             print("红包即将成功发送！")
# #         else:
# #             redPackage(input("输入有误，请重新输入0.01-200的金额:"))
# #
# #     except Exception as e:
# #         print("格式出错啦，%s" % e)
# #         redPackage(input("输入有误，请重新输入0.01-200的金额:"))
# #
# # redPackage()
#
#
# # def divide(x, y):
# #     try:
# #         result = x / y
# #     except ZeroDivisionError:
# #         print("division by zero!")
# #     else:
# #         print("result is", result)
# #     finally:
# #         print("executing finally clause")
# #
# # if __name__=='__main__':
# #     divide(10,5)
#
#
# # def price_count():
# #    price=input("请输入当月利润：\n")
# #    try:
# #         price = float(price)
# #         if  0<= price <=100000:
# #             price=price*0.1
# #         elif  100000< price <=200000:
# #             price=(price-100000)*0.075+100000*0.1
# #         elif  200000< price <=400000:
# #             price=(price-200000)*0.05+(200000-100000)*0.075+100000*0.1
# #         elif  400000< price <=600000:
# #             price=(price-400000)*0.03+(400000-200000)*0.05+(200000-100000)*0.075+100000*0.1
# #         elif 600000 < price <= 1000000:
# #             price = (price - 600000) * 0.015+(600000-400000)*0.03+(400000-200000)*0.05+(200000-100000)*0.075+100000*0.1
# #         else:
# #             price = (price - 1000000) * 0.01+(1000000 - 600000) * 0.015+(600000-400000)*0.03+(400000-200000)*0.05+(200000-100000)*0.075+100000*0.1
# #         print("您当月应发奖金总数为:%.2f"%price)
# #    except Exception as e:
# #         print("错误: %s"%e)
# #         print("您输入的数据有误，请重新输入！")
# #         price_count()
# #
# # price_count()
#
# #
# # with open('E:/ZGH/test\zgh/file.txt','r',encoding='utf-8') as file:
# #     print(file.read())
# # #
# # def addd():
# #     try:
# #         a = input("请输入第一个数：")
# #         b = input("请输入第二个数：")
# #         sum=int(a)+int(b)
# #         print("两个数的和是：{}".format(sum))
# #     except ValueError  as  e:
# #         print("格式错误:%s"%e,"\n请重新输入数据")
# #
# # addd()
#
#
# # while True:
# #     try:
# #         a = input("请输入第一个数：")
# #         b = input("请输入第二个数：")
# #         sum=int(a)+int(b)
# #         print("两个数的和是：{}".format(sum))
# #         break
# #     except ValueError  as  e:
# #         print("格式错误:%s"%e,"\n请重新输入数据")
#
#
# # a="hello"
# # # print("你好"+a)
# #
# # class SuperMan:
# #     age = 30
# #     sex = 'male'
# #     name = 'nick'
# #
# #     def protect_people(self,name='毛毛'):
# #         print("我是超人，我会保护人民，我的名字叫：",name)
# #         self.age = 40
# #
# #     def fly_to_sky(self,name_2):
# #         self.protect_people(name_2)
# #         print(self.age)
# #         print("我是超人，我会飞")
# # person=SuperMan()
# # print(person.age)
# # person.fly_to_sky("ahuahua")
# # print(person.age)
#
# #
# # class SuperMan:
# #     def __init__(self,age,sex,name):
# #         self.age = age
# #         self.sex =sex
# #         self.name = name
# #
# #     def protect_people(self,name='毛毛'):
# #         print("我是超人，我会保护人民，我的名字叫：",name)
# #         self.age = 40
# #
# #     def fly_to_sky(self,name_2='huahua'):
# #         self.protect_people(name_2)
# #         print(self.age)
# #         print("我是超人，我会飞")
# #
# # person=SuperMan(20,'f','nick')
# # print('1',person.age)
# # person.fly_to_sky('华华')
# # print('2',person.age)
#
#
# #
# # class SoftTestEnginner:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age
# #     def basic_skill(self):
# #         print("{}今年{}岁，可以做点点点功能测试".format(self.name,self.age))
# #     def salary(self,salary):
# #         print("可以拿到的薪资大概是%s"%salary)
# #
# # SoftTestEnginner('小毛',21).basic_skill()
# # SoftTestEnginner("小毛",21).salary(5000)
# #
# #
# # class JuniorSoftTestEnginner(SoftTestEnginner):
# #     def basic_skill(self):
# #         print("{}今年{}岁，可以做接口自动化测试".format(self.name,self.age))
# #
# # JuniorSoftTestEnginner('华华',30).basic_skill()
# # JuniorSoftTestEnginner('华华',30).salary(120000)
#
#
# # #子类调用父类
# # class A:
# #     def __init__(self):
# #         self.namea = "aaa"
# #     def funca(self):
# #         print("function a : %s" % self.namea)
# #
# # class B(A):
# #     def __init__(self):
# #         self.nameb = "bbb"
# #         A.__init__(self)
# #     def funcb(self):
# #         print("function b : %s" % self.nameb)
# #
# # b = B()
# # print(b.nameb)
# # b.funcb()
# # b.funca()
#
#
# #单元测试
# # import  unittest
# # class TestMathMethod(unittest.TestCase):
#
#
# #enconding: utf-8
# #name:  huahua
#
# #编写机器人类:智能机器人属性和功能
# #颜色  品牌  大小  移动速度  价格
# # 人脸识别    #语音对讲  #紧急呼叫   #语音播报   #播放歌曲
#
# class IntelligentRobot:
#     '这是个智能机器人类，有机器人的属性和功能'
#     color='blue'
#     brand='优必选'
#     size='1243*925*1110mm'
#     speed='0-1m/s'
#     price=6599
#
#     def  face_recognition(self):  # 人脸识别  对象方法 (只能通过对象访问)
#         print("你好呀，我可以做人脸识别！")
#
#     @staticmethod
#     def  voice_intercom(name):  #语音对讲   静态方法 (类和对象来访问)
#         print("你好呀，我可以语音对讲，你可以和{}进行通话对讲".format(name))
#         IntelligentRobot().face_recognition()
#         # IntelligentRobot.face_recognition()
#
#
#     def  emergency_call(self,phone_number=110):    #紧急呼叫   对象方法
#         print("你好呀，我可以进行紧急呼叫，当前呼叫的号码为:",phone_number)
#         self.face_recognition()
#         # IntelligentRobot.face_recognition()
#         IntelligentRobot().face_recognition()
#
#
#     @classmethod
#     def  voice_announcements(cls,*args):   #语音播报   类方法 (类和对象来访问)
#         print("你好呀，我可以进行语音播报，当期播报的内容是:",args)
#         cls().sing_song(999)
#         IntelligentRobot.sing_song(111)
#         IntelligentRobot().sing_song(222)
#
#     @classmethod
#     def   sing_song(cls,song):    #播放歌曲    类方法
#         print("你好呀，我可以播放歌曲，即将播放的歌曲是:",song)
#
# robot=IntelligentRobot()   #创建对象
#
# # print("机器人价格是:",robot.price)   #对象调用属性
# # print("机器人品牌是:",IntelligentRobot.brand)   #类调用属性
# # print("机器人颜色是:",robot.color)
# # print("机器人移动速度是:",IntelligentRobot.speed)
# #
# # robot.face_recognition()
# #
# robot.voice_intercom('花花')
# # IntelligentRobot.voice_intercom("小明")
# #
# # robot.emergency_call()
# # robot.emergency_call(119)
# #
# # robot.voice_announcements('今天可能会有雨','提醒大家出门带雨伞','别忘记啦！')
# # IntelligentRobot.voice_announcements('下午三点要开会','请大家不要迟到了')
# #
# # robot.sing_song('传奇')
# # IntelligentRobot.sing_song('沙漠骆驼')
#
#
#
#
#
#
# #enconding: utf-8
# #name:  huahua
# #
# # import random
# # class  FingerGuessing:
# #     juese=0
# #     finger=0
# #     pc_finger=0
# #     num_1=0
# #     num_2=0
# #     num_3=0
# #
# #     @staticmethod
# #     def  choose_player():   #选角色
# #         try:
# #             player=int(input("请选择角色，输入1-3的任意一个数字（1.曹操，2.张飞，3.刘备）:"))
# #             if  player==1  or player==2  or  player==3:
# #                if player==1:
# #                    FingerGuessing.juese='曹操'
# #                elif player==2:
# #                    FingerGuessing.juese = '张飞'
# #                else:
# #                    FingerGuessing.juese = '刘备'
# #             else:
# #                 print("你输入的数据不在范围内，请重新输入")
# #                 FingerGuessing().choose_player()
# #             print(FingerGuessing.juese)
# #         except  Exception  as  e:
# #             print("你输入的数据类型有误，请重新输入")
# #             FingerGuessing().choose_player()
# #
# #
# #     def  guessing_finger(self):   #角色出拳
# #         print(self.juese)
# #         try:
# #             self.finger=int(input("请你出拳，输入1-3的任意一个数字（1.剪刀，2.石头，3.布）:"))
# #             if  self.finger==1  or self.finger==2  or  self.finger==3:
# #                 pass
# #             else:
# #                 print("你输入的数据不在范围内，请重新输入")
# #                 FingerGuessing().guessing_finger()
# #         except  Exception  as  e:
# #             print("你输入的数据类型有误，请重新输入")
# #             FingerGuessing().guessing_finger()
# #
# #     @classmethod
# #     def  pc_guessing(cls):  #电脑出拳
# #         cls.pc_finger=random.randint(1,3)
# #         print("电脑出拳：",cls.pc_finger)
# #
# #     def  fight_against(self):
# #         if self.finger==self.pc_finger:
# #             print("本局平局")
# #             self.num_1+=1
# #         elif (self.finger==1 and self.pc_finger==3)  or (self.finger==2 and self.pc_finger==1) or (self.finger==3 and self.pc_finger==2):
# #             print("恭喜{}，本局你获胜".format(self.juese))
# #             self.num_2+=1
# #         else:
# #             print("不好意思，本局电脑获胜")
# #             self.num_3+=1
# #         res=input("请问是否继续猜拳,若继续玩游戏，请输入字母y,若想结束，请输入字母n：")
# #         if  res=='y':
# #             FingerGuessing().guessing_finger()
# #             FingerGuessing.pc_finger()
# #         else:
# #             FingerGuessing().res_print()
# #
# #     def  res_print(self):
# #         print("最终的结果为：{}赢了{}局，电脑赢了{}局，平局{}次".format(self.juese,self.num_2,self.num_3,self.num_1))
# #         print("游戏结束")
# #
# # fg=FingerGuessing()
# #
# # fg.choose_player()
# # fg.guessing_finger()
# # fg.pc_guessing()
# # fg.fight_against()
# # fg.res_print()
#
# # a=[1,2,3,"hello"]
# # a.remove('hello')
# # print(a)
#
#
# # num_1=0
# # for  item  in  b:
# #     item.choose()
# #     if item.res_2!=0:
# #         num_1+=1
# # if  num_1 == 3 or  num_1 == 2:
# #     if b[0].res_2 ==b[1].res_2:
# #         b[0].shoot()
# #
# #     elif  b[0].res_2==b[2].res_2:
# #         b[0].shoot()
# #
# #     elif  b[1].res_2==b[2].res_2:
# #         b[1].shoot()
# #
# # elif num_1 == 1:
# #     for item  in  b:
# #         if  item.res_2 != 0:
# #             item.shoot()
# #

#
# numb_1=0
# numb_2=0
# numb_3=0
# numpo_1=0
# numpo_2=0
# person_1.input_people()
# if person_1.res==b[0]:
#     numb_1+=1
# if person_1.res==b[1]:
#     numb_2 += 1
# if person_1.res==b[2]:
#     numb_3 += 1
# if person_1.res==b[3]:
#     numpo_1 += 1
# if person_1.res==b[4]:
#     numpo_2 += 1
#
# person_2.input_people()
# if person_1.res==b[0]:
#     numb_1+=1
# if person_1.res==b[1]:
#     numb_2 += 1
# if person_1.res==b[2]:
#     numb_3 += 1
# if person_1.res==b[3]:
#     numpo_1 += 1
# if person_1.res==b[4]:
#     numpo_2 += 1
#
# person_3.input_people()
# if person_1.res==b[0]:
#     numb_1+=1
# if person_1.res==b[1]:
#     numb_2 += 1
# if person_1.res==b[2]:
#     numb_3 += 1
# if person_1.res==b[3]:
#     numpo_1 += 1
# if person_1.res==b[4]:
#     numpo_2 += 1
#
# person_4.input_people()
# if person_1.res==b[0]:
#     numb_1+=1
# if person_1.res==b[1]:
#     numb_2 += 1
# if person_1.res==b[2]:
#     numb_3 += 1
# if person_1.res==b[3]:
#     numpo_1 += 1
# if person_1.res==b[4]:
#     numpo_2 += 1
#
# person_5.input_people()
# if person_1.res==b[0]:
#     numb_1+=1
# if person_1.res==b[1]:
#     numb_2 += 1
# if person_1.res==b[2]:
#     numb_3 += 1
# if person_1.res==b[3]:
#     numpo_1 += 1
# if person_1.res==b[4]:
#     numpo_2 += 1
#
# list_1=[numb_1,numb_2,numb_3,numpo_1,numpo_2]
# list_1.sort()
# if  list_1[4]==5:
#     person_1.identify_pepole()
# # if
# #
# #
# # people = ['N3', 'N4', 'N5', 'N6', 'N7']
# # a= "N3"
# # people.remove(a)
# # print(people[0])


# a=1
# while True:
#     if a==1:
#         print(666)
#         break
#     else:
#         print(999)
# print(8888)
#
# from  zgh.lianxi_2 import Police
# class Oo(Police):
#     pass
#
#
# Oo(1,2,3).catch_badboy()
#
#
# import   random
# class  Online_Retailers:   #父类
#     '这是个电商类，有它的属性以及对应的功能'
#     def  __init__(self,name='京东',feature='电子产品',boss='刘强东'): #初始化函数
#         self.name=name  #平台名称
#         self.feature=feature   #平台特征
#         self.boss=boss   #创始人
#
#     @staticmethod
#     def  login_in(username,pwd):    #登录功能   静态方法
#         #用户名：huahua   密码：123456
#         if username == 'huahua' and  pwd == '123456':
#             print("恭喜您登录成功！")
#             res=True
#         else:
#             print("抱歉您输入的账号或者密码有误，登录失败")
#             res=False
#         return   res
#
#     def pay_method(self):  #支付
#         try:
#             method=int(input("请您选择支付方式：（1：微信支付，2：支付宝支付，3：银联支付）"))
#             if  method==1:
#                 print("微信支付")   # 微信支付
#             elif  method==2:
#                 print("支付宝支付")     #支付宝支付
#             elif  method==3:
#                 print("银联支付")    # 银联支付
#         except Exception  as  e:
#             print("您输入的数据有误，请重新输入")
#             Online_Retailers().pay_method()
#         return  method
#
#     def  discount(self):   #优惠券
#         print("支付成功。恭喜您获得了一张金额为{}的优惠券".format(random.randint(10,50)))
#
#
#
# class  JingDong(Online_Retailers):  #京东类继承电商类
#     '这个是京东类，有它的的属性和功能'
#
#     @staticmethod
#     def  settlement():   #结算功能   拓展
#         print("欢迎来到京东商城！！！")
#         username = input("请输入您登录的用户名：")
#         pwd = input("请输入您的登录密码：")
#         result=JingDong.login_in(username,pwd)
#         if  result:
#             input("请您输入的购买金额：")
#             while True:
#                 pay_res = JingDong().pay_method()
#                 if  pay_res==1:
#                     JingDong().discount()
#                     break
#                 elif pay_res==3:
#                     print("结算成功。您的支付方式没有优惠")
#                     break
#                 elif pay_res==2:
#                     print("很抱歉，我们暂时不支持该支付方式，请重新支付")
#
#
#
#
# class  TaoBao(Online_Retailers):   #淘宝类继承电商类
#     '这个是淘宝类，有它的的属性和功能'
#
#     def settlement(self):  # 结算功能   拓展
#         print("欢迎来到淘宝！！！")
#         username = input("请输入您登录的用户名：")
#         pwd = input("请输入您的登录密码：")
#         result = TaoBao.login_in(username,pwd)
#         if result:
#             input("请您输入的购买金额：")
#             while True:
#                 pay_res = TaoBao().pay_method()
#                 if pay_res == 2:
#                     self.discount()
#                     break
#                 elif pay_res == 3:
#                     print("结算成功。您的支付方式没有优惠")
#                     break
#                 elif pay_res == 1:
#                     print("很抱歉，我们暂时不支持该支付方式，请重新支付")
#
#
#
# if  __name__=='__main__':
#     JingDong.settlement()   #调用京东类实现功能
#     TaoBao().settlement()  # 调用淘宝类实现功能
#

# class TB(ElectronicPlatform):
#     def __init__(self):
#         super().__init__('淘宝', '服装类', '马云')
#     def login(self):
#         user_name = input('请输入用户名：')
#         pwd = input('请输入密码：')
#         while True:
#             if user_name == 'huahua' and pwd == '123456':
#                 print('登录成功\n登录的用户名为{}'.format(user_name))
#                 user_money=int(input('请输入付款金额：'))
#                 money=self.pay_method()     #'1':'alipay','2':'wechatpay','3':'unionpay'
#                 if money=='1':
#                     mon=self.discount()
#                     print('可以享受优惠，此次的付款金额为：{}'.format(user_money-mon))
#                     break
#                 elif money=='3':
#                     print('不享受任何优惠，此次的付款金额为：{}'.format(user_money))
#                     break
#                 elif money=='2':
#                     print('没有此类支付方式，请重新选择')
#                     continue
#             else:
#                 result='failed'
#                 print('登录失败：{}'.format(result))
#                 continue
#             #return result
#             break
#



