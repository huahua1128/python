import requests

data_1 = {"mobilephone":"18629787846","pwd":"huahua123456"}  # 注册登陆的参数
data = {"mobilephone":"18629787844","pwd":"huahua123456",'regname':'xiaoxiao'}  # 注册
data_2 = {"mobilephone":"18629787846","amount":2}  # 充值的参数
data_3 = {"mobilephone":"18629787844","amount":2}  # 充值的参数
url =  'http://47.107.168.87:8080/futureloan/mvc/api/member/'

session = requests.session()   # 实例化一个session对象

resp_1 = session.request('post', url = url+'login', data = data_1)   # 登陆
res  = session.get(url+'register', params = data)  #注册

resp_2 = session.request('get', url = url+'recharge', params = data_2)  # 充值
resp_3 = session.request('get', url = url+'recharge', params = data_3)  # 充值
# 或者
# resp_1 = session.post( url = url+'login', data = data_1)  # 登陆
# resp_2 = session.get(url = url+'recharge', params = data_2)   # 充值


print('登陆请求的结果',resp_1.text)  # json字符串格式
print('登陆请求的cookies',resp_1.request._cookies)
print('登陆的响应cookies',resp_1.cookies)
print("*************************")
print('注册请求的结果',res.text)  # json字符串格式
print('注册请求的cookies',res.request._cookies)
print('注册的响应cookies',res.cookies)
print("*****************************************")
print('充值请求的cookies',resp_2.request._cookies)
print('充值请求的结果',resp_2.json())  # 字典
print('充值的响应cookies',resp_2.cookies)
print("*****************************************")
print('充值2请求的cookies',resp_3.request._cookies)
print('充值2请求的结果',resp_3.json())  # 字典
print('充值2的响应cookies',resp_3.cookies)