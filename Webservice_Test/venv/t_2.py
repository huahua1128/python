from suds.client import Client

# # # 注册
url_2 = "http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
data_1 = {'channel_id': '2', 'mobile': '13010057395', 'ip': '172.28.78.9', 'pwd': 'huahua123456', 'verify_code': 'yy44ff#', 'user_id': '大小66600u'}
data = {"verify_code":"358123","user_id":"大e宝999","mobile":"13012344395","channel_id":"ydhfhe##","pwd":"123@wee","ip":"34.90.78.1"}
client_2 = Client(url_2)
# print(client_2)
try:
    result_2 = client_2.service.userRegister(data_1)
    print(result_2)
except Exception as e:
    print(type(str(e)),e)
    if 'Unmarshalling Error' in str(e):
        print(666666666666)