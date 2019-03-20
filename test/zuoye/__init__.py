# print (False  and True and False)
#
# print ((False and True) and (False))
# age=20
# for a in age:
#     print(a)


member=0
for i in range(0,10):
    ag=input("请问你的年龄是多少：")
    if  ag.isdigit():
        age=int(ag)
        sex=input("请问您的性别是（男生请输入m,女生请输入f):")
        if sex!='m' or sex!='f':
            print("您输入的性别有误，请重新输入（男生请输入m,女生请输入f)：")
            if  age>=10  and  age<=12 and sex== 'f':
                print("恭喜你，你可以加球队")
                member += 1
            else:
                print("抱歉，你不能加入球队")
    else:
        print("您输入的年龄有误")
        input("请输入一个整数：")
        sex = input("请问您的性别是（男生请输入m,女生请输入f):")
        if sex!='m' or sex!='f':
            print("您输入的性别有误")
            input("请重新输入性别（男生请输入m,女生请输入f)：")
            if ag.isdigit():
                age = int(ag)
                if age >= 10 and age <= 12 and sex == 'f':
                    print("恭喜你，你可以加球队")
                    member += 1
                else:
                    print("抱歉，你不能加入球队")

print("符合条件的总人数是:%d" %member)