import pymysql
from common.read_config import ReadConfig

class MysqlUtil:

    def __init__(self, return_dict = False):
        read_config = ReadConfig()
        host = read_config.get_value('database','host')
        port = read_config.get_int('database', 'port')
        user = read_config.get_value('database', 'user')
        password = read_config.get_value('database', 'password')
        self.mysql = pymysql.connect(host = host, port = port, user = user, password = password) # 连接数据库
        if return_dict:
            self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)   # 指定每行数据以字典形式返回
        else:
            self.cursor = self.mysql.cursor()  # 连接游标  一个查询做完所有操作后再关闭。以元组返回

    def fetch_one(self,sql):  # 返回一条数据，是以元组的形式
        # cursor = self.mysql.cursor()   #查询一次关一次
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        # cursor.close()        # 关闭游标，查询一次关一次 (相当于建立一个查询，查询完一个就关闭)
        self.mysql.commit()
        return  result     # 返回的是个元组

    def fetch_all(self, sql):   # 默认返回的列表里面放元组的方式返回多条数据
        self.cursor.execute(sql)
        results = self.cursor.fetchall()   # [(),(),（）]
        self.mysql.commit()
        return  results

    def close(self):
        self.cursor.close()  #关闭游标
        self.mysql.close()   #关闭数据库

if  __name__ == '__main__':
    # mysql = MysqlUtil()
    # # results = connect.fetch_one("select mobilephone from member where  mobilephone=%s" % (20000000000))
    # results = mysql.fetch_one("select mobilephone from future.member where mobilephone=18999999999")  # future.member这样写上面就可以不写数据库名了
    # print(results)
    # print(results[0])
    # mysql.close()

    # mysql = MysqlUtil(return_dict=True)   # 以字典形式存放
    # sql = 'select *  from future.member limit 10'
    # results = mysql.fetch_all(sql)
    # print(results)
    # for result in results:
    #     print(type(result), result)   # int型
    # mysql.close()

    # mysql = MysqlUtil(return_dict=True)
    # sql = "select max(mobilephone) as max_phone  from future.member"
    # max = mysql.fetch_one(sql)
    # print(type(max['max_phone']), max['max_phone'])
    # mysql.close()

    # mysql = MysqlUtil(return_dict=True)
    # sql = 'SELECT * FROM sms_db_95.t_mvcode_info_3  WHERE ' \
    #       ' Fmobile_no={2}'.format(mobile[-2:], mobile[-3], mobile)
    # results = self.mysql.fetch_all(sql)

    # mysql = MysqlUtil()
    # sql = "SELECT Fverify_code FROM sms_db_95.t_mvcode_info_3  WHERE  Fmobile_no=13186248395"
    # results = mysql.fetch_one(sql)
    # print(type(results[0]),results[0])

    # 先向查找出来的手机发送验证码
    from suds.client import Client
    mysql = MysqlUtil(return_dict = True)
    mobile = str(13087253395)
    data = {"client_ip": "12.34.78.99", "tmpl_id": "1", "mobile": mobile}
    # client = Client(self.pre_url + 'sms-service-war-1.0/ws/smsFacade.ws?wsdl')
    client = Client("http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl")
    res_1 = client.service.sendMCode(data)
    print(res_1)
    # time.sleep(10)
    sql = "SELECT * FROM sms_db_{0}.t_mvcode_info_{1}  WHERE " \
          "  Fmobile_no={2}".format(mobile[-2:], mobile[-3], mobile)
    print(sql)
    print(mysql.fetch_all(sql), type(mysql.fetch_all(sql)))