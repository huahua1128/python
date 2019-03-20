#enconding: utf-8
#name:  huahua
#3个坏人，5个平民 ，2个警察，分别编号为：N0,N1,N2,N3,N4,N5,N6,N7,N8,N9

class Police:
    '警察类，有警察的属性以及他的方法'
    def __init__(self,code_name,name,age):   #初始化函数
        self.code_name = code_name
        self.name = name
        self.age = age
        self.res=0

    @staticmethod
    def shoot(kill_name):  #开枪   静态方法
        print("我要对你开枪了！！！{} {},你死了".format(kill_name,eval(kill_name).name))

    def input_people(self):  #指认   对象方法
        print("请警察选择你要指认的人：", badegg+people)
        res = input()
        self.res = res

    def  catch_badboy(self):  #抓人   对象方法
        print("我抓到你了")

    def  run(self):   #跑的快   对象方法
        print("跑的很快")

class  BadEgg:
    '坏人类，有坏人的属性以及他的方法'
    def __init__(self,nick_name,name,age):   #初始化函数
        self.nick_name = nick_name
        self.name = name
        self.age = age
        self.res=0

    def choose(self):  #选择做什么  对象方法
        res_1 = input("请坏人选择数字你要做什么(1：抢银行，2：偷东西，3:杀人):")
        if res_1=='1':
            self.bank_robbery(self.name)
        elif  res_1=='2':
            self.scrounge(self.name)
        else :
            print("请选择你要杀的人,：",people+police)
            res = input()
            self.res = res

    @staticmethod
    def shoot(kill_name):   #杀人   静态方法
        print("{} {} 这局死掉".format(kill_name,eval(kill_name).name))

    def  run(self):   #跑的快   对象方法
        print("跑的很快")

    def  scrounge(self,name):   #偷东西  对象方法
        print("{} 去偷东西了".format(name))

    def  bank_robbery(self,name):    #抢银行   对象方法
        print("{} 去抢银行了".format(name))

class  People:
    '平民类，有平民的属性以及方法'
    def __init__(self,pet_name, name, age):  #初始化函数
        self.pet_name = pet_name
        self.name = name
        self.age = age
        self.res=0

    def  run(self):   #跑的快  对象方法
        print("跑的很快")

    def input_people(self):    #选择指认的目标    对象方法
        print("请平民选择你要指认的人：", badegg+police)
        res = input()
        self.res = res

    @staticmethod
    def  identify_pepole(kill_name):    #指认技能   静态方法
        print("指认技能生效,{}  {}死掉".format(kill_name,eval(kill_name).name))

# 创建对象：
N0 = BadEgg("N0", "pitt", 30)
N1 = BadEgg("N1", "河畔", 22)
N2 = BadEgg("N2", "海绵", 31)

N3 = People("N3", "花花", 18)
N4 = People("N4", "七月", 24)
N5 = People("N5", "晴天", 26)
N6 = People("N6", "简爱", 28)
N7 = People("N7", "阿牛", 20)

N8 = Police("N8", "挖矿", 40)
N9 = Police("N9", "月亮", 35)

# 创建不同类游戏角色列表
badegg = ['N0', 'N1', 'N2']
people = ['N3', 'N4', 'N5', 'N6', 'N7']
police = ['N8', 'N9']

count=1
def panduan():
# 4  判断
    if len(police) == 0 or len(people) == 0:
        print("非常遗憾，本局坏人获胜！！！")
        return 0
    if len(badegg) == 0:
        print("恭喜，本局平民和警察获胜！！！")
        return  0


while True:
    print("***********这是第{}轮************".format(count))
    # 1 坏蛋出击
    list=[]
    for  item   in  badegg:
        var=eval(item)
        var.choose()
        if  var.res != 0:
            list.append(var.res)

    person_out=''
    if  len(list)==3:
        if list[0]==list[1]:
            person_out=list[0]
            BadEgg.shoot(person_out)
        elif list[1]==list[2]:
            person_out=list[1]
            BadEgg.shoot(person_out)
        elif list[0]==list[2]:
            person_out=list[2]
            BadEgg.shoot(person_out)
    elif len(list)==2:
        if list[0]==list[1]:
            person_out=list[0]
            BadEgg.shoot(person_out)
    elif   len(list)==1:
        person_out=list[0]
        BadEgg.shoot(person_out)

    if person_out in police:
        police.remove(person_out)
    if person_out in people:
        people.remove(person_out)

    if panduan()==0:
        break

    #2  平民出击
    list_1=[]
    for  item   in  people:
        var_1=eval(item)
        var_1.input_people()
        if  var_1.res != 0:
            list_1.append(var_1.res)

    person_out_1=''
    if len(list_1)==5:
        if  ((list_1[0]==list_1[1]) and (list_1[2]!=list_1[3]  and  list_1[3]!=list_1[4]))  or ((list_1[0]==list_1[2]) and (list_1[1]!=list_1[3]  and  list_1[3]!=list_1[4]))  or ((list_1[0]==list_1[3]) and (list_1[1]!=list_1[2]  and  list_1[2]!=list_1[4])) or ((list_1[0] == list_1[4]) and (list_1[1] != list_1[2] and list_1[2] != list_1[3]))  or (list_1[0] == list_1[1]== list_1[2] and (list_1[3] != list_1[4])) or (list_1[0] == list_1[1]== list_1[3] and (list_1[2] != list_1[4])) or (list_1[0] == list_1[1]== list_1[4] and (list_1[2] != list_1[3])) or (list_1[0] == list_1[2]== list_1[3] and (list_1[1] != list_1[4])) or (list_1[0] == list_1[2]== list_1[4] and (list_1[1] != list_1[3])) or (list_1[0] == list_1[3]== list_1[4] and (list_1[1] != list_1[2])) or(list_1[0] == list_1[1]== list_1[2]==list_1[3]) or (list_1[0] == list_1[1]== list_1[2]==list_1[4]) or (list_1[0] == list_1[1]== list_1[2]==list_1[3]==list_1[4]):
            person_out_1=list_1[0]
            People.identify_pepole(person_out_1)
        elif ((list_1[1]==list_1[2]) and (list_1[0]!=list_1[3]  and  list_1[3]!=list_1[4])) or ((list_1[1]==list_1[3]) and (list_1[0]!=list_1[2]  and  list_1[2]!=list_1[4])) or ((list_1[1]==list_1[4]) and (list_1[0]!=list_1[2]  and  list_1[2]!=list_1[3])) or (list_1[1]==list_1[2]==list_1[3]  and  list_1[0]!=list_1[4]) or (list_1[1]==list_1[2]==list_1[4]  and  list_1[0]!=list_1[3]) or (list_1[1] == list_1[3]== list_1[4] and (list_1[0] != list_1[2])):
            person_out_1 = list_1[1]
            People.identify_pepole(person_out_1)
        elif ((list_1[2]==list_1[3]) and (list_1[0]!=list_1[1]  and  list_1[1]!=list_1[4])) or ((list_1[2]==list_1[4]) and (list_1[0]!=list_1[1]  and  list_1[1]!=list_1[3])) or (list_1[2]==list_1[3]==list_1[4]  and  list_1[0]!=list_1[1]):
            person_out_1 = list_1[2]
            People.identify_pepole(person_out_1)
        elif ((list_1[3]==list_1[4]) and (list_1[0]!=list_1[1]  and  list_1[1]!=list_1[2])):
            person_out_1 = list_1[4]
            People.identify_pepole(person_out_1)

    if len(list_1)==4:
        if (list_1[0]==list_1[1] and list_1[2] != list_1[3]) or (list_1[0]==list_1[2] and list_1[1] != list_1[3]) or (list_1[0]==list_1[3] and list_1[1] != list_1[2]) or (list_1[0]==list_1[1]== list_1[2]) or (list_1[0]==list_1[1]== list_1[3]) or (list_1[0]==list_1[2]== list_1[3]) or (list_1[0]==list_1[1]== list_1[2]==list_1[3]):
            person_out_1 = list_1[0]
            People.identify_pepole(person_out_1)
        elif (list_1[1]==list_1[2] and list_1[0] != list_1[3]) or (list_1[1]==list_1[3] and list_1[0] != list_1[2]) or (list_1[1]==list_1[2]== list_1[3]):
            person_out_1 = list_1[1]
            People.identify_pepole(person_out_1)
        elif (list_1[2]==list_1[3] and list_1[1] != list_1[0]):
            person_out_1 = list_1[2]
            People.identify_pepole(person_out_1)

    if len(list_1)==3:
        if list_1[0]==list_1[1] or list_1[0]==list_1[2] or list_1[0]==list_1[1]==list_1[2]:
            person_out_1 = list_1[0]
            People.identify_pepole(person_out_1)
        elif list_1[1]==list_1[2]:
            person_out_1=list_1[1]
            People.identify_pepole(person_out_1)

    if len(list_1)==2:
        if list_1[0]==list_1[1]:
            person_out_1=list_1[0]
            People.identify_pepole(person_out_1)

    if len(list_1)==1:
        person_out_1=list_1[0]
        People.identify_pepole(person_out_1)

    if person_out_1 in police:
        police.remove(person_out_1)
    if person_out_1  in badegg:
        badegg.remove(person_out_1)

    if panduan() == 0:
        break

    #3 警察出击
    list_2=[]
    for  item   in  police:
        var_2=eval(item)
        var_2.input_people()
        if  var_2.res != 0:
            list_2.append(var_2.res)

    person_out_2=''
    if len(list_2)==2:
        if list_2[0]==list_2[1]:
            person_out_2=list_2[0]
            if person_out_2 in people:
                print("不好意思，指认的人为平民，本局游戏结束！！！")
                count += 1
                continue
            if  person_out_2  in  badegg:
                Police.shoot(person_out_2)
    if len(list_2)==1:
        person_out_2=list_2[0]
        if person_out_2 in people:
            print("不好意思，指认的人为平民，本局游戏结束！！！")
            count += 1
            continue
        if person_out_2 in badegg:
            Police.shoot(person_out_2)
            badegg.remove(person_out_2)

        if panduan() == 0:
            break










