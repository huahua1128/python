#enconding: utf-8
#name:  huahua

user_id = "花花花Arno1"
user_id_1 = int(user_id[-1])+1
print(user_id[-1])
user_id = user_id[:-2]+str(user_id_1)
print(type(user_id),user_id)
#enconding: utf-8
#name:  huahua

user_id = "花花花Arno1"
user_id_1 = int(user_id[-1])+1
print(user_id[-1])
user_id = user_id[:-2]+str(user_id_1)
print(type(user_id),user_id)

from common import context
from common.connect_mysql import MysqlUtil
from suds.client import Client
from common.get_code import get_code

mysql = MysqlUtil()

mobile_new = '13100233395'
def check_mobile():
    global mobile_new
    for i in range(1, 6):
        while True:
            print("每次取到的mobile", mobile_new)
            sql_1 = "select * from sms_db_{0}.t_mvcode_info_{1}  WHERE " \
                    "  Fmobile_no={2}".format(mobile_new[-2:], mobile_new[-3], mobile_new)
            print(sql_1)
            print(mysql.fetch_one(sql_1))
            if mysql.fetch_one(sql_1):
                print('-------------------',mobile_new)
                pre_mobile = mobile_new[:8]
                end_mobile = mobile_new[-3:]
                mobile_new = str(int(pre_mobile) + 1) + end_mobile
                setattr(context.Context, 'mobile', mobile_new)
                print('+++++++++++++++++++',mobile_new)
            else:  # 最终的手机号还是mobile
                print("###############最新从数据库查询出来的手机号：", mobile_new)
                break


        get_code(mobile_new)

        verify_code = getattr(context.Context, 'verify_code')

        uer_id = str(1234445 + i)
        url_2 = "http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
        data = {"verify_code":verify_code , "user_id": user_id, "mobile": mobile_new, "channel_id": "2",
                "pwd": "123@wee", "ip": "34.90.78.1"}
        client_2 = Client(url_2)
        try:
            result_2 = client_2.service.userRegister(data)
            print(result_2)
        except Exception as e:
            print(type(str(e)), e)

if __name__ == '__main__':
    # from common import context
    # print(getattr(context.Context, "uid_list"))

    # uid_list = [1,2]
    # for i in range(1,4):
    #     uid_list.append(i)
    #     print(uid_list)
    # print(uid_list)

    uid_list = ['100006277\n', '100006278\n', '100006279\n', '10000628\n', '100006281\n']
    with open("wwww.txt", 'w') as file:
        file.writelines(uid_list)










