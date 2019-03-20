#enconding: utf-8
#name:  huahua
import random
from common import context

def first():
    # 随机给一些前六位的数的列表
    list = ['411623', '510100', '510107', '610100', '610112', '150602', '152922', '210600', '360102']
    num = random.choice(list)
    return num

def year():
    year = random.randint(1990,2015)
    return year

def month():
    month = random.randint(1, 12)
    if month < 10:
        month = '0' + str(month)
    return month

def day():
    day = random.randint(1, 29)
    if day < 10:
        day = '0' + str(day)
    return day

def random_num():
    '''生成身份证16-18位'''
    # 后面序号低于相应位数，前面加上0填充
    num = random.randint(400, 999)
    if num < 10:
        num = '00' + str(num)
    elif 10 < num < 100:
        num = '0' + str(num)
    return num

def get_cre_id():  # 生成身份证
    s_1 = first()
    print(s_1, type(s_1))
    num_1 = int(s_1[0]) * 7 + int(s_1[1]) * 9 + int(s_1[2]) * 10 + int(s_1[3]) * 5 + int(s_1[4]) * 8 + int(s_1[5]) * 4
    s_2 = str(year())
    print(s_2, type(s_2))
    num_2 = int(s_2[0]) * 2 + int(s_2[1]) * 1 + int(s_2[2]) * 6 + int(s_2[3]) * 3
    s_3 = str(month())
    print(s_3, type(s_3))
    num_3 = int(s_3[0]) * 7 + int(s_3[1]) * 9
    s_4 = str(day())
    print(s_4, type(s_4))
    num_4 = int(s_4[0]) * 10 + int(s_4[1]) * 5
    s_5 = str(random_num())
    print(s_5, type(s_5))
    num_5 = int(s_5[0]) * 8 + int(s_5[1]) * 4 + int(s_5[2]) * 2
    number = num_1 + num_2 + num_3 + num_4 + num_5
    print(number)
    res = number % 11
    print(res)
    if res == 0:
        last_num = 1
    elif res == 1:
        last_num = 0
    elif res == 2:
        last_num = 'X'
    elif res == 3:
        last_num = 9
    elif res == 4:
        last_num = 8
    elif res == 5:
        last_num = 7
    elif res == 6:
        last_num = 6
    elif res == 7:
        last_num = 5
    elif res == 8:
        last_num = 4
    elif res == 9:
        last_num = 3
    else:
        last_num = 2
    cre_id = s_1 + s_2 + s_3 + s_4 + s_5 + str(last_num)
    setattr(context.Context, "cre_id", cre_id)
    return cre_id

if __name__ == '__main__':
    print(get_cre_id())
    print(getattr(context.Context, "cre_id"))
