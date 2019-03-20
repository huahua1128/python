from suds.client import Client



# 发送验证码
url = "http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"   #这里是你的webservice访问地址
data = {"client_ip":"1234.34.78.999","tmpl_id":"1","mobile":"13012344395"}
client = Client(url)    #Client里面直接放访问的URL，可以生成一个webservice对象
print(client)
try:
    result = client.service.sendMCode(data)
    print(dict(result)["retInfo"])
except Exception as e:
    print(type(str(e)),e)
    if 'Unmarshalling Error' in str(e):
        print(666666666666)
print(type(dict(result)),dict(result)['retCode'])
print(type(dict(result)),dict(result)['retInfo'])

