#enconding: utf-8
#name:  huahua

setPayPwd
from suds.client import Client

# # ## 设置
url_2 = "http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
data = {"uid":"100005421","pay_pwd":"123456wer","mobile":"18777770098","cre_id":"110101199003077635","user_name":"宋大辉","bank_type":"1001","cardid":"6227001253210804602","bank_name":"中国建设银行","bank_area":"江苏省","bank_city":"徐州市"}
client_2 = Client(url_2)
print(client_2)
try:
    result_2 = client_2.service.setPayPwd(data)
    print(result_2)
except Exception as e:
    print(type(str(e)),e)