from suds.client import Client
from common.connect_mysql import MysqlUtil
from common.get_ip import get_ip
from common import context

def get_code(mobilephone):
    # 先向查找出来的手机发送验证码
    mysql = MysqlUtil()
    ip = get_ip()
    data = {"client_ip":ip, "tmpl_id": "1", "mobile": mobilephone}
    # client = Client(self.pre_url + 'sms-service-war-1.0/ws/smsFacade.ws?wsdl')
    client = Client("http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl")
    res_1 = client.service.sendMCode(data)
    # print(res_1)
    sql = "SELECT Fverify_code FROM sms_db_{0}.t_mvcode_info_{1}  WHERE " \
          "  Fmobile_no={2}".format(mobilephone[-2:], mobilephone[-3], mobilephone)
    # print(sql)
    # ww = mysql.fetch_all(sql)
    # print(ww, type(ww))

    verify_code = (mysql.fetch_one(sql))[0]
    # print(verify_code)
    setattr(context.Context, 'verify_code', verify_code)
    return verify_code