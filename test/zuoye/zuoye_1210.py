#1
pri=input("请输入您购买商品的总金额：")
if pri.isdigit():
    price=float(pri)
else:
    print("您输入的商品金额格式有误！")
    price = float( input("请重新输入金额："))
if  50<= price <=100:
    final_price=price*0.9
    zk_price=price*0.1
    print("您的折扣价格为{1},您的最终购买价格为{0}".format(final_price,zk_price))
elif  price>100:
    final_price = price * 0.8
    zk_price = price * 0.2
    print("您的折扣价格为{1},您的最终购买价格为{0}".format(final_price, zk_price))
else:
    print("您的商品价格为{}".format(price))

#2
for i  in  range(1,10):
    for  j  in  range(1,i+1):
        print('{} * {} = {}  '.format(j,i,i*j),end='')
    print()

#3
num_1=''
num_2=''
member=input("请输入一个四位整数：")
if member.isdigit():
    num=member
else:
    print("您输入的数字格式有误！")
    num = input("请重新输入一个四位整数：")
for i in num:
    a=int(i)+5
    b=a%10
    num_1=num_1+str(b)
print(num_1)
new_num_2=num_2+num[3]+num[2]+num[1]+num[0]
print(new_num_2)
print("合作后加密的整数为：{}".format(num_1+new_num_2))


#4
d={"admin":"lemon","huahua":"123456"}
i=0
count=2
username=input("请输入登录的用户名：")
while True:
    if username == "admin" or username == "huahua":
        break
    print("用户名输入不正确")
    username = input("请输入正确的用户名：")
pswd = input("请输入登录的密码：")
if (username=='admin'and pswd!=d['admin'] )or  (username=='huahua'and pswd!=d['huahua']):
    while i<2:
        print("密码错误,您还有{}次输入密码的机会".format(count))
        count-=1
        pswd = input("请重新输入登录的密码：")
        i += 1
        if (username == 'admin' and pswd == d['admin']) or (username == 'huahua' and pswd == d['huahua']):
            print("恭喜您登陆成功")
            break
else:
    (print("恭喜您登陆成功"))

 #4  第二种方法
d={"admin":"lemon","huahua":"123456"}
i=0
count=2
username=input("请输入登录的用户名：")
while not(username == "admin" or username == "huahua"):
    print("用户名输入不正确")
    username = input("请输入正确的用户名：")
pswd = input("请输入登录的密码：")
if (username=='admin'and pswd!=d['admin'] )or  (username=='huahua'and pswd!=d['huahua']):
    while i<2:
        print("密码错误,您还有{}次输入密码的机会".format(2-i))
        pswd = input("请重新输入登录的密码：")
        i += 1
        if (username == 'admin' and pswd == d['admin']) or (username == 'huahua' and pswd == d['huahua']):
            print("恭喜您登陆成功")
            break
else:
    (print("恭喜您登陆成功"))




