import  requests

class HttpRequest:
    '''接口请求类'''
    def  __init__(self,url,params):
        self.url = url
        self.params = params

    def http_request(self, method, cookies = None):
        if  method.upper == 'GET':
            try:
                res = requests.get(self.url, self.params, cookies=cookies)
            except Exception as e:
                print('执行get请求报错，错误是{}'.format(e))



