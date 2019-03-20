def student_info(class_name,name,offer):
    print("{}期的{}同学拿到了{}k的offer!恭喜恭喜".format(class_name,name,offer))

    eat("可乐",'花生','薯片')

def eat(*food_name):   #传进来是元组
    food_name_str=''   #存储传进来的食物列表
    for item in food_name:
        food_name_str+=item
        food_name_str+='、'
    food_name_str=food_name_str.strip('、')    #去掉最后的顿号，方法一，也可以用for
    print("最喜欢吃：{}".format(food_name_str))

#测试代码
if __name__=='__main__':  #代码执行的入口
    student_info('python13','小花花',20)

