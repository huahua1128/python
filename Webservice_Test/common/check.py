#enconding: utf-8
#name:  huahua
from common import context
from common.connect_mysql import MysqlUtil

mysql = MysqlUtil()

def check_mobile():
    while True:
        mobile = getattr(context.Context, 'mobile')
        # print("每次取到的mobile",mobile)
        sql_1 = "select * from sms_db_{0}.t_mvcode_info_{1}  WHERE " \
                "  Fmobile_no={2}".format(mobile[-2:], mobile[-3], mobile)
        if mysql.fetch_one(sql_1):
            pre_mobile = mobile[:8]
            end_mobile = mobile[-3:]
            mobile = str(int(pre_mobile) + 1) + end_mobile
            setattr(context.Context, 'mobile', mobile)
            # print(getattr(context.Context, 'mobile'))
        else:  # 最终的手机号还是mobile
            # print("最新从数据库查询出来的手机号：", mobile)
            setattr(context.Context, 'mobile', mobile)  # 用最新的手机号覆盖Context类属性的mobile值
            # print("****************",getattr(context.Context, 'mobile'))
            break
    return mobile

def check_user_id():
    # 每次将user_id 最后一位加1
    while True:
        user_id = getattr(context.Context, 'user_id')
        sql_1 = "SELECT * FROM user_db.t_user_info WHERE Fuser_id=\'{0}\'".format(user_id)
        if mysql.fetch_one(sql_1):
            user_id_1 = int(user_id[-1]) + 1
            user_id = user_id[:-1]+str(user_id_1)
            setattr(context.Context, 'user_id', user_id)
            # print("****************",getattr(context.Context, 'user_id'))
        else:    # 最终的手机号还是mobile
            setattr(context.Context, 'user_id', user_id)   # 用最新的手机号覆盖Context类属性的mobile值
            # print("++++++++++++++++++++++++",getattr(context.Context, 'user_id'))
            # print("最新从数据库查询出来的用户名：", user_id)
            break
    return user_id


if __name__ == '__main__':
    check_mobile()
    check_user_id()