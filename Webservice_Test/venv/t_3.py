from suds.client import Client

# # 实名认证
url_2 = "http://120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
data = {"uid":"100006052","true_name":"你","cre_id":"370102200508205583"}
client_2 = Client(url_2)
# print(client_2)
result_2 = client_2.service.verifyUserAuth(data)
print(result_2)