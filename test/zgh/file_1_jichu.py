'''print('nihao')
print("jiayou")

print('hello\
      python\
      66666')

str='nihao"小明"'
print(str)

#s=0.012
#print(type(s))

# b='hello world'
# print(b[-1])


#a='柠檬班'
#b='is best'
#print(a+b)

#c=1
#m='xiaowang'
#print(c,m)
#print(str(c)+m)


a='lemon'
res=a[1:]
print(res)

str_1='hello lemon class'
print(str_1[2::2])

name='花花'
age=22
score=86.236
print("%s今年%d岁,数学考了%d分"%(name,age,score))

name='花花'
age=22
score=86.236
print("{0}今年{1}岁,数学考了{0}分".format(name,age,score))

str_1='hello'
res=str_1.upper()
print('转换之后的结果为{}'.format(res))



str_1='hello'
res=str_1.find('el')
print('转换之后的结果为{}'.format(res))


tuple=(1,)
print(type(tuple))


a=[1,0.05,'lemonban',(1,2,3),[4,5,6]]
c=a[4]
print(c[2])
print(a[4][2])
print(a[-1][-1])


a={'name':'花花','age':18,'score':[99.99,100,80],'money':100}
print(a)
a.pop('score')
print(a)
print('字典中的姓名是:{}'.format(a['name']))


#print(a.items())
c={'name':'小明','mingt':'加油'}
a.update(c)
print(a)
print(c.values())

#print(5//2)


c={'name':'小明','mingt':'加油'}
print(c.popitem())

color='green'
if color=='red':
    print('红灯停')
elif color=='green':
    print('绿灯行')
else:
    print('请等一等')



a=input("请输入成绩：")
if a>=80:
    print("{0}分为优秀".format(a))
elif a>=60 and a<80:
    print("{}分为及格".format(a))
elif a>0 and a<60:
    print("{}分为不及格".format(a))
else:
    print("请输入一个数")


a=10
while True:
    a-=1
    if a>0:
        print("a的值为{0}".format(a))

    else:
        break



# sum=0
# for item in range(1,101):
#     sum+=item
# print("1到100的整数和为:{}".format(sum))
# a=tuple(range(2,8,2))
# print(a)

#
#
# def add(a=6,b=7):
#     c=a+b
#     print(c)
# add(4,6)




def greet(content="晚上好",*args):
    name=''
    for item in args:
        name+=item
        name+='.'
    print(name,content)
greet("花花","毛毛")

a=[1,0.05,'lemonban',(1,2,3),[4,5,6]]
a.extend('加油','花花')
print(a)


u = 'hello good boy'
print('.'.join(u))
x=1
print(eval('x+1'))

total=0
def sum(arg1,arg2):
    global total
    total=arg1+arg2
    print("函数内部的局部变量为:{0}".format(total))
    return total

sum(10,20)'''

# print("函数外部的全部变量为:{0}".format(total))


# a=1
# b=1
# print(id(a))
# print(id(b))

# a=20
# print(type(a))
# print(type(20.0))

# a="'''hello'''"
# print(a)
# b="'jiayou'"
# print(b)
# a=input("请输入一个数据：")
# print(a)


# a='hello world!'
# print(a[0:3:1])  #0 1 2
# print(a[0:4:2])  #0 2

# a='hello python1'
# print(a[-1::-1])   #a实现倒序输出所有元素
# print(a[12::-1])   #a实现倒序输出所有元素
# print(a[::-1])     #a实现倒序输出所有元素

# s_1="hello"
# s_2="加油"
# print(s_1+s_2)
# a=20
# print(s_1+s_2,a)   #不同数据类型的拼接
# print(s_1+s_2+str(a))    #不同数据类型的拼接

# age=18
# height=170.34
# hobby="打篮球"
# print("我的年龄是{2},身高是{0},业余爱好是{1}".format(height,hobby,age))
# a='1'
# # b=1
# # print(type(a))
# # print(type(b))

# a="hello python13y"
# print(a.upper())    #切换成大写
# b="HELLO PYTHON13Y"
# print(b.lower())     #切换成小写
# c="HELlO PyThOn13Y"
# print(c.swapcase())     #大小写互换

# a="hello python13y"
# print(a.find('l'))   #返回遇到的第一个l的索引值
# print(a.find('w'))    #若查找的元素不存在返回-1
# print(a.find('py'))   #查找子字符串，返回p的索引

# a="hello pytHon13y"
# print(a.capitalize())
# a="hello pytHon13y"
# print(a.count('h'))  #找h的个数，区分大小写
# print(a.index('py'))   #返回p的索引值

# b='12'
# print(b.isdigit())
# c='aas222'
# print(c.isdigit())
# print(c[1].islower())
# print(c[1].isupper())

# c='aas222'
# print('*'.join(c))

# a="helHlo pythonh13y"
# print(a.split(' '))  #以空格切分
# print(a.split('l'))   #以l切分
# print(a.split('h',2))   #以h切分,切分次数为2

# t_0=()          #空元组
# print(type(t_0))
# t_1=(1)          #不是元组
# print(type(t_1))
# t_2=('1')        #不是元组
# print(type(t_2))
# t_3=('1',)        #是元组
# print(type(t_3))
#
# t_1=(2,0.0089,'1',True,(1,2,3,'hello'))
# print(t_1[1])
# print(t_1[-1])
# print(t_1[-1][-1])  #嵌套取值  取hello
# print(t_1[-1][-1][1])  #嵌套取值  取e

# t_1=(2,0.0089,'1',True,(1,2,3,'hello'))
# print(t_1[:5:2])    #取索引为偶数的值
# print(t_1[::2])      #取索引为偶数的值

# t_1=(2,0.0089,'1',True,(1,2,3,'hello'),2,5)
# # #t_1[0]='加油'     #元组不可以修改
# # print(t_1.count(2))   #可以查询个数
# # print(t_1.index(2,1))  #查询第二个为2的索引

# t=[2,0.0089,'1',True,(1,2,3,'hello'),['python13','lemon','土豆','西红柿']]
# print(t[2])
# print(t[4][2])
# print(t[-1][-2][0])

# t=[2 ,'1',(1,2,3,'hello'),['python13','土豆']]
# a=['你是个大西瓜']
# t.append(a)
# print(t)

# t=[2,0.0089,'1',True,(1,2,3,'hello'),['python13','lemon','土豆','西红柿']]
# t.pop()
# print(t)
# t=[2,0.0089,'1',True,(1,2,3,'hello'),['python13','lemon','土豆','西红柿']]
# t.pop(2)
# print(t)

# t=[2,0.0089,'1',True,(1,2,3,'hello'),['python13','lemon','土豆','西红柿']]
# t.reverse()
# print(t)

# t_1=['a','f','r','h','k','l','k']
# t_2=[1,56,2,8,3,69,5]
# t_1.sort()
# t_2.sort()
# print(t_1)
# print(t_2)

# t=[2,0.0089,'1',True,(1,2,3,'hello'),['python13','lemon','土豆','西红柿']]
# t[-1][-1]='shadow'
# print(t)

# t=[2,0.0089,'1',True,(1,2,3,'hello'),['python13','lemon','土豆','西红柿']]
# t[4]='柠檬水'     #对整个元组可以修改，相当于列表的元素
# print(t)
# t=[2,0.0089,'1',True,(1,2,3,'hello'),['python13','lemon','土豆','西红柿']]
# t[4][1]='HELLO'  #这样相当于修改元组里面的值是不可以的
# print(t)

# a=(2,0.0089,'1',True,(1,2,3,'hello'),['python13','土豆','西红柿'])
# a[-1][-1]='*'   #对列表里面的元素修改
# print(a)
# a[-1]=9         #元组的元素不可以修改
# print(a)

# d={'name':'花花','age':18,'hobby':'学python',
#    'score':{'en':120,'math':99.99,'ch':'A'},
#    'friend':['baby','华华','小cc'],2:'hello',0.02:'python',
#    True:'这个value对应的key是布尔值'}
# print(d['friend'])
# print(d['friend'][0])
# print(d['score']['en'])
#
# d={'name':'花花','age':18,
#   'score':{'en':120,'math':99.99}}
# d['salary']='20k'  #新增元素
# print(d)
# d['name']='小可爱'   #修改
# print(d)
# d.pop('score')     #删除指定元素
# print(d)
# d.popitem()       #随机删除一个元素
# print(d)
#

# print(1+2)
# print(1*2)
# print(1-2)
# print(10%3)

# a=3
# a+=1   #相当于a=a+1
# print(a)

# print(3==4)   #判断两边是否相等
# print(3>4)
# print('get'=='GET')
# print('get'.upper()=='GET')  #区分大小写

# a=10
# b=-5
# c=0
# print(a>0 and b>0)   #左右两边同时成立
# print(a>0 or  b>0)   #左右两边有一边满足即可
# print(a>0 or b>0 and c>0)   #先and后or
# print(not 0)
#
# s='hello'
# print('e'not in s)
# t=[1,'hello',666,9.58]
# print('h' in t )
# print('hello' in t)
# d={'name':'huahua','age':18}
# print('age' in d)   #根据key ，不能根据value

# num=input("请输入一个1到100成绩:")
# # if num.isdigit():
# #     score=int(num)
# #     if 80 <= score <= 100:
# #         print("该成绩为优秀")
# #     elif 70 <= score < 80:
# #         print("该成绩为良好")
# #     elif 60 <= score < 70:
# #         print("该成绩为及格")
# #     else:
# #         print("该成绩为不及格")
# # else:
# #     print("该成绩格式不正确，请重新输入")

# pri=input("请输入您购买商品的总金额：")
# if pri.isdigit():
#     price=float(pri)
# else:
#     print("您输入的商品金额格式有误！")
#     price = float( input("请重新输入金额："))
# if  50<= price <=100:
#     final_price=price*0.9
#     zk_price=price*0.1
#     print("您的折扣价格为{1},您的最终购买价格为{0}".format(final_price,zk_price))
# elif  price>100:
#     final_price = price * 0.8
#     zk_price = price * 0.2
#     print("您的折扣价格为{1},您的最终购买价格为{0}".format(final_price, zk_price))
# else:
#     print("您的商品价格为{}".format(price))

# num=input("请输入一个1到100成绩:")
# if num.isdigit():
#     score=int(num)
#     if  100< score or  score<0:
#         print("数据范围应该在0-100之间")
#     elif  score > 80:
#         print("该成绩为优秀")
#     elif score> 70:
#         print("该成绩为良好")
#     elif score>=60:
#         print("该成绩为及格")
#     else:
#         print("该成绩为不及格")
# else:
#     print("输入的数据有误")
#
# s='python13'
# l=[1,0.23,'xiaohua','旅行者']
# d={'name':'花花','age':18,'money':'10w'}
# t=(1,5,6,'hi','how are you')
#
# d={'name':'花花','age':18,'money':'10w'}
# for item  in d:   #打印出字典中的value
#     print(d[item])
# for  i  in  d.values():  #打印出字典中的value
#     print(i)

# p=[[1,2,3],[4,5,6],[7,8,9]]
# for  i  in  p:
#     for  j  in  i:
#         print(j)

# res=range(1,10,3)
# print(list(res))  #强制转换为列表是为了方便观察
#range(101)

#0-100的偶数和
# sum=0
# for i in range(0,101,2):
#     sum+=i
# print("0-100的偶数和为{}".format(sum))
#0-100的奇数 偶数和
# sum_1=0
# sum_2=0
# for i in range(101):
#     if i%2!=0:
#         sum_1+=i
#     else:
#         sum_2+=i
# print("0-100的奇数和为{}".format(sum_1))
# print("0-100的偶数和为{}".format(sum_2))


# d={"admin":"lemon","huahua":"123456"}
# i=0
# username=input("请输入登录的用户名：")
# while not(username == "admin" or username == "huahua"):
#     print("用户名输入不正确")
#     username = input("请输入正确的用户名：")
# pswd = input("请输入登录的密码：")
# while i<3:
#     if (username == 'admin' and pswd == d['admin']) or (username == 'huahua' and pswd == d['huahua']):
#         print("恭喜您登陆成功")
#         break
#     if i==2:
#         break
#     print("密码错误,您还有{}次输入密码的机会".format(2 - i))
#     pswd = input("请重新输入登录的密码：")
#     i += 1

# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end='')
#     print()

# a=0
# # while a<3:  #0 1 2
# #     a+=1
# #     print("我是一个死循环")   #执行break后这一句不执行



