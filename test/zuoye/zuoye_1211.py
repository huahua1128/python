#enconding: utf-8
#name:  huahua

# 练习题
#1
def make_shirt(size,typeface):
    print("这个t-shirt的尺码为:{0}，印刷的字样为:{1}".format(size,typeface))

make_shirt("L","number one")

#2
def  describe_city(cityname,country='China'):
    print("{0} is  in  {1}".format(cityname,country))

describe_city("Tokyo","Janpan")
describe_city("London","England")
describe_city('shanghai',"China")
describe_city("tianjin")

#3
def city_country(cityname,country):
   print("{0}"",""{1}".format(cityname,country))

city_country("天津","中国")
city_country("伦敦","英国")
city_country('上海',"中国")

#4
def make_album(name,album):
    d={name:album}
    return d

res_1=make_album("张杰","逆战")
res_2=make_album("易烊千玺","舒适圈")
res_3=make_album("何炅","栀子花开")
print("歌手和专辑名分别为：",res_1)
print("歌手和专辑名分别为：",res_2)
print("歌手和专辑名分别为：",res_3)

#5
def food_print(*args):
    print("您点的三明治中添加的食材有：{}".format(args))

food_print("鸡肉","苹果","面包","火腿")
food_print("芝士","鸡蛋")
food_print("午餐肉","生菜")

# 初级题型
# 1
def score_print():
    score = input("请输入你的成绩：\n")
    if score.isdigit()  and  0 <= int(score) <= 100:
        score=int(score)
        if  80<score:
            print("成绩优秀！")
        elif  60<= score <=80:
            print("成绩良好！")
        else:
            print("成绩不及格！")
    else:
        print("你的成绩输入错误！！！")
        score_print()

score_print()

# 2
def price_count():
    price=input("请输入当月利润：\n")
    if  price.replace('.','') .isdigit():
        price = eval(price)
        if  0<= price <=100000:
            price=price*0.1
        elif  100000< price <=200000:
            price=(price-100000)*0.075+100000*0.1
        elif  200000< price <=400000:
            price=(price-200000)*0.05+(200000-100000)*0.075+100000*0.1
        elif  400000< price <=600000:
            price=(price-400000)*0.03+(400000-200000)*0.05+(200000-100000)*0.075+100000*0.1
        elif 600000 < price <= 1000000:
            price = (price - 600000) * 0.015+(600000-400000)*0.03+(400000-200000)*0.05+(200000-100000)*0.075+100000*0.1
        else:
            price = (price - 1000000) * 0.01+(1000000 - 600000) * 0.015+(600000-400000)*0.03+(400000-200000)*0.05+(200000-100000)*0.075+100000*0.1
        print("您当月应发奖金总数为:%.2f"%price)
    else:
            print("您输入的数据有误，请重新输入！")
            price_count()

price_count()

# 3
import random
num=random.randint(1,10)
print(num)
def guess_num():
    count=input("猜猜我现在心里想的是0-10的数字几：\n")
    if count.isdigit()and 0<=int(count)<=10:
        count=int(count)
        if count<num:
            print("你猜的太小了，请重新猜")
            guess_num()
        elif count>num:
            print("你猜的太大了，请重新猜")
            guess_num()
        else:
            print("恭喜你猜对了！！")
    else:
        print("你输入错误，请输入0-10的整数")
        guess_num()

guess_num()

# 4
def  len_judge(*args):
    if len(args)>5:
        print("传入的参数长度大于5")
    else:
        print("传入的参数长度小于5")

len_judge(*("helloworld !"))
len_judge(*(1,"花花",[1,2,"lemon"]))
len_judge(*["hh",25,"加油",666,0,"明天"])

# 5
def people_msg(name,city,sex='f'):
    if city=="长沙"  and  sex=='f':
        print("姓名为:{0}，性别为:{1}   ".format(name,sex),end='')
        res="True"
    else:
        res="False"
    return  res

print(people_msg('花花','长沙','m'))
print(people_msg('小明','长沙'))

# 6
def check_ele(a):
    s=[]
    if len(a)>2:
        s.append(a[0])
        s.append(a[1])
        return s
    else:
        return "长度不大于2"

print(check_ele([1,2,3,4,5]))
print(check_ele([1,3]))

# 7.
def str_dict(str,**kwargs):
    if str  not in kwargs:
        kwargs[str]=' '
        return kwargs
    else:
        return  "字符串在字典中"

d={"name":"花花","age":18}
print(str_dict("happy",name="花花",age=18))
print(str_dict("name",name="花花",age=18))

# 中级题型
# 1
def  num_count(i,j,k,m):
    count=0
    for i in range(1,5):
         for  j  in  range(1,5):
             for k  in  range(1,5):
                 if i != j and i != k and j != k:
                     print(i*100+j*10+k)
                     count+=1
    return count

print(num_count(1,2,3,4))

# 2
def ask_msg(m,n,sex,k):
    count=0
    while count < k:
        age_1 = input("请输入你的年龄：\n")
        if age_1.isdigit():
            age=int(age_1)
            if  m<= age<=n:
                sex_1=input("请问你的性别是(男生请输入m,女生请输入f)：\n")
                if   sex_1=='f' or  sex_1=='m':
                    if  sex_1==sex:
                        print("恭喜你可以加入足球队")
                        count+=1
                    else:
                        print("抱歉你不能加入球队")
                        count += 1
                else:
                    print("你的性别输入有误，请重新输入")
            else:
                print("抱歉你不能加入球队")
                count += 1
        else:
                print("你的年龄输入有误，请重新输入")

ask_msg(12,20,"m",3)
