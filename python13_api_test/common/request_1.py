import requests
import json
# 充值的第二种方式
class Request:

    def request(self, method, url, data = None, cookies = None):
        if data is not None and type(data) == str:
            data = json.loads(data)   # 如果是字符串就转成字典
        try:
            if method.upper() == 'GET':
                return requests.get(url = url, params = data, cookies = cookies)
            elif method.upper() == 'POST':
                return requests.post( url=url, data=data, cookies=cookies)
            else:
                print("不支持该请求方式")
        except Exception as e:
            print('执行请求报错',e)
