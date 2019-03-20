import requests

# 参数
data_1 = {"mobilephone":"13539787045","pwd":"huahua123456","regname":"huahua"}  # 注册登陆的参数
data_2 = {'mobilephone':'18929787846','amount':2}  # 充值的参数
url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/'

# 注册接口   用get请求，url传参，用params
res_1 = requests.get(url+'register', params = data_1)
print('请求的url',res_1.url)          # 获取请求的url
print('请求头',res_1.request.headers)      # 获取请求头
print('请求参数',res_1.request.body)      # 获取请求参数  get获取的请求参数都是none,get的参数是和url一起传的。post获取的是参数，
print('请求cookies',res_1.request._cookies)    # 请求cookies

print('响应头',res_1.headers)      # 获取响应头
print('响应状态码',res_1.status_code)      # 获取响应状态码
print('响应信息类型', type(res_1.text))   # 获取响应信息类型
print('响应信息', res_1.text)        # 获取响应信息  json格式的字符串
print('响应信息字典类型', type(res_1.json()))   # 获取响应信息类型
print('响应信息字典', res_1.json())  # 获取响应信息    json()直接将json字符串转为字典
print('响应cookies', res_1.cookies)   # 获取响应cookies

print('注册请求的结果是：', res_1.json())


# 登陆接口   用post请求，表单传参，用data
url_2 = 'http://47.107.168.87:8080/futureloan/mvc/api/member/login'
res_2 = requests.post(url_2, data = data_1)
print('请求参数',res_2.request.body)

# 充值接口   用post请求，表单传参，用data
# #充值需要用到登陆返回的cookies
res_3 = requests.post(url+'recharge', data = data_2, cookies = res_2.cookies)
# res_3.encoding = 'utf-8'
print('注册请求的结果是：', res_3.json())
print('regname：', res_3.json()['data']['regname'])    # regname
print('注册请求的结果是：', res_3.text)


# 可以将这个充值的响应信息写入html
with open('html1_report.html', 'wb') as file:
    file.write(res_3.content)

with open('html2_report.html', 'w+', encoding = 'utf-8') as file:
    file.write(res_3.text)