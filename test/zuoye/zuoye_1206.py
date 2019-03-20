#1
sum=0
for i in range(0,101,2):
    sum += i
print("0-100的所有偶数和为{0}".format(sum))

count=0
for i in range(1,101):
    if i%2 != 0:
        count += i
        i += 1
    else:
        i += 1
print("0-100的所有奇数和为{0}".format(count))

#2
member=0
for i in range(0,10):
    age=int(input("请问你的年龄是多少："))
    sex=input("请问您的性别是（男生请输入m,女生请输入f):")
    if  age>=10  and  age<=12 and sex== 'f':
        print("恭喜你，你可以加球队")
        member += 1
    else:
        print("抱歉，你不能加入球队")
print("符合条件的总人数是:%d" %member)

#3
for i in range(1,6):
    print(i*('* '))





