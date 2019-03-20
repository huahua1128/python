# def  radio_machine():
#     print("我是一个复读机，只会说你好！")
#     return   [111,222],[333,666]
# res=radio_machine()
# print("函数的返回值为: {}".format(res))
#
# def add():
#     result=8+8
#     print(result)
#     return  result
# res=add()+20  #拿到返回值再做下一步处理
# print(res)
#
# t=[1,2,3]
# t.pop()

# n=1
# print(eval("n+1"))
# m=2.036
# print(eval("m+1"))


# def count_number(a,c,b=101): #默认参数顺序必须在位置参数后面
#     count=0
#     for i  in range(a,b,c):
#         count+=i
#     print("计算结果是：{}".format(count))
#     return  count
#
# count_number(0,2)  #有默认参数的可以不用赋值，位置参数必须赋值
# count_number(0,2,50) #有值就用实参的值，就不用默认参数值了

# def robot_cat(*args):
#     print(args)   #到函数内部就成了元组
#     for  item  in   args:
#         print("我是叮当猫，我可以变出很多东西，比如：{}".format(item))
#
# a=["money",'钱钱钱']
# b=[["money",'钱钱钱'],[1,"hello"]]
# robot_cat(a)  #传入列表
# print('----------------')
# robot_cat(*a)  #传入的是列表的元素
# print('----------------')
# robot_cat(*b)   #（脱外套，但只脱一层）并且只能加一个星号

# def robot_cat(*args):
#     print(args)   #到函数内部就成了元组
#     for  item  in   args:
#         print("我是叮当猫，我可以变出很多东西，比如：{}".format(item))
#
# b={"name":"花花","年龄":18}
# robot_cat(b)   #传入后就一个参数（一个字典整体是一个元素）
# print('----------------')
# robot_cat(*b)   #传入后只传入了字典的key
# robot_cat(*b.values())   #传入后传了字典的value

# def anyway(**kwargs):
#     print(kwargs)
#
# anyway(color='blue',y=3,name=18)  #必须为变量名=值（key不能为字符串）

# list=['1:2','12:2','5','3','6']
# for  i  in  list:
#     print(i)
#     m=i.split(',')
#     print(m)

# def student_info(class_name,name,offer):
#     print("{}期的{}同学拿到了{}k的offer!恭喜恭喜".format(class_name,name,offer))
#
#     eat("可乐",'花生','薯片')
#
# student_info('python13','小花花',20)  #这个函数调用放在这里会报错，还未定义eat函数
# #
# def eat(*food_name):   #传进来是元组
#     food_name_str=''   #存储传进来的食物列表
#     for item in food_name:
#         food_name_str+=item
#         food_name_str+='、'
#     food_name_str=food_name_str.strip('、')    #去掉最后的顿号，方法一，也可以用for
#     print("最喜欢吃：{}".format(food_name_str))
#
# student_info('python13','小花花',20) #这个函数调用放在这里不会报错，按顺序向下执行，eat已定义
# eat("煎饼",'小鱼干','火锅','玉米')



offer=1   #全局变量（局部里面申明了全局，这个值就被修改了）
def student_info(class_name,name):
    global offer   #申明全局变量
    offer=20   #申明后就成了全局变量
    print("{}期的{}同学拿到了{}k的offer!恭喜恭喜".format(class_name,name,offer))
    offer+=2   #全局变量（offer=22）

def student_record():  #记录最高薪资
    print("目前要打破{}k记录才能晋升为最高薪资".format(offer))   #申明后的全局变量的值


print(offer)
print(offer+3)
student_record()   #1  因为还没调用student_info,所以还没有修改offer的值
student_info('13','不忘初心')  #20
print(offer)     #22
student_record()    #22  已经调用student_info,所以已修改了offer的值（这个调用可以不写全局offer=1）


