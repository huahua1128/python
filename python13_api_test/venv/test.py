import  requests
data_1 = {"mobilephone":"13539787045","pwd":"huahua123456"}
data = {"mobilephone":"13539787045","amount":"500000"}
data_2 ={'id':15696}
url =  'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
url_1 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/recharge'


res = requests.post(url, data = data_1)
res_1 = requests.post(url_1, data = data , cookies = res.cookies )
print('请求的结果是：', res_1.json())
