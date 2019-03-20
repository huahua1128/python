#enconding: utf-8
#name:  huahua

import random
class  FingerGuessing:
    '这是个石头剪刀布游戏类'
    juese=0
    finger=0
    pc_finger=0
    num_1=0
    num_2=0
    num_3=0

    @staticmethod
    def  choose_player():   #选角色
        try:
            player=int(input("请选择角色，输入1-3的任意一个数字（1.曹操，2.张飞，3.刘备）:"))
            if  player==1  or player==2  or  player==3:
               if player==1:
                   FingerGuessing.juese='曹操'
               elif player==2:
                   FingerGuessing.juese = '张飞'
               else:
                   FingerGuessing.juese = '刘备'
            else:
                print("你输入的数据不在范围内，请重新输入")
                FingerGuessing().choose_player()
        except  Exception  as  e:
            print("你输入的数据类型有误，请重新输入")
            FingerGuessing().choose_player()

    def  guessing_finger(self):   #角色出拳
        try:
            self.finger=int(input("请你出拳，输入1-3的任意一个数字（1.剪刀，2.石头，3.布）:"))
            if  self.finger==1  or  self.finger==2  or self.finger==3:
                pass
            else:
                print("你输入的数据不在范围内，请重新输入")
                self.guessing_finger()
        except  Exception  as  e:
            print("你输入的数据类型有误，请重新输入")
            self.guessing_finger()

    @classmethod
    def  pc_guessing(cls):  #电脑出拳
        cls.pc_finger=random.randint(1,3)
        print("电脑出拳：",cls.pc_finger)

    def  fight_against(self):   #判断输赢
        if self.finger==self.pc_finger:
            print("本局平局")
            self.num_1+=1
        elif (self.finger==1 and self.pc_finger==3)  or (self.finger==2 and self.pc_finger==1) or (self.finger==3 and self.pc_finger==2):
            print("恭喜{}，本局你获胜".format(self.juese))
            self.num_2+=1
        else:
            print("不好意思，本局电脑获胜")
            self.num_3+=1
        while True:
            res=input("请问是否继续猜拳,若继续玩游戏，请输入字母y,若想结束，请输入字母n：")
            if  res=='y':
                self.guessing_finger()
                FingerGuessing.pc_guessing()
                self.fight_against()
                break
            elif res=='n':
                self.res_print()
                break
            else:
                print("输入有误，请重新输入")

    def  res_print(self):   #最终结果
        print("最终的结果为：{}赢了{}局，电脑赢了{}局，平局{}次".format(self.juese,self.num_2,self.num_3,self.num_1))
        print("游戏结束！！！")

fg=FingerGuessing()

fg.choose_player()
fg.guessing_finger()
fg.pc_guessing()
fg.fight_against()

