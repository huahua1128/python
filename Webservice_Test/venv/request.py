from suds.client import Client
from common.read_config import ReadConfig

config = ReadConfig()
pre_url = config.get_value('url', 'pre_url')

def request(case_url,api_name, data):
    url = pre_url + case_url
    client = Client(url)
    try:
        str = 'client.service.' + api_name
        result = eval(str)(data)
        msg = dict(result)["retInfo"]
    except Exception as e:
        result = e
        msg = str(e)
    return result


if __name__ == '__main__':
    data = {"client_ip": "12.34.78.99", "tmpl_id": "1", "mobile":"18800087878"}
    case_url = 'sms-service-war-1.0/ws/smsFacade.ws?wsdl'
    apiname =  'sendMCode'
    result = request(case_url, apiname, data)
    print(result)



    # client = Client(pre_url + case_url)
    # str = 'client.service.' + apiname
    # result = eval(str)(data)
    # print(result)