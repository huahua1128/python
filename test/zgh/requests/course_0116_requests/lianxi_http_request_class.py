import requests

class  HttpRequest:
    """http请求类"""

    def __init__(self, url, params):
        self.url = url
        self.params = params

    def http_request(self, method, cookies = None):
        if method.upper() == 'GET':
            try:
                res = requests.get(self.url, params=self.params, cookies = cookies)
            except Exception as e:
                print("执行get请求出错，错误是：{}".format(e))
                res = 'Error:get请求报错{0}'.format(e)
        elif method.upper() == 'POST':
            try:
                res = requests.post(self.url, data=self.params, cookies = cookies)
            except Exception as e:
                print("执行post请求出错，错误是：{}".format(e))
                res = 'Error:post请求报错{0}'.format(e)
        else:
            print("你的请求方式不正确！")
            res = 'Error:请求方式不正确报错{0}'.format(method)
        return  res


if __name__ == '__main__':
    url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/register'
    params = {"mobilephone":"13539787041","pwd":"huahua123456","regname":"huahua"}
    res_1 = HttpRequest(url,params).http_request('get')
    res_2 = HttpRequest(url, params).http_request('post')
    print(res_1.json())
    print(res_2.json())