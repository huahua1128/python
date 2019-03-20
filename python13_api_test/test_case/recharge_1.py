import unittest
import json
from libext.ddt import ddt,data
from common.do_excel import DoExcel
from common.request_1 import Request
from common import contants
from common.read_config import ReadConfig

# 第二种方法，不用session传递，用get post然后直接传递cookies。request里面也不同
@ddt
class TestRecharge(unittest.TestCase):  # 继承TestCase类
    do_excel = DoExcel(contants.case_dir, 'recharge1')
    cases = do_excel.get_data()
    path_url = ReadConfig().get_value('url', 'path_url')  # 这些放到类里面也可以，用self调用
    request = Request()
    # 以上都是类属性   request = Request() 实例化为了传递cookies,Request初始化的时候有session的对象

    def setUp(self):  # 每个用例执行前执行一次
        self.res = self.request.request('post', url=self.path_url + 'member/login', data= {"mobilephone":"13539787043","pwd":"huahua123456"})

    @data(*cases)
    def test_recharge(self, case):
        print("开始执行{0}模块的第{1}条用例：{2}".format(case.module, case.case_id, case.title))
        resp = self.request.request('post', url= self.path_url+case.url, data = case.data,cookies = self.res.cookies)  #request.path_url都是类属性
        case.expected = json.loads(case.expected)
        print(resp.json())
        try:
            self.assertEqual(case.expected['code'], resp.json()['code'], 'recharge error')  # recharge error是提示
            self.do_excel.write_back(case.case_id + 1, resp.text, 'PASS')
            print("第{}条测试用例执行的结果是：PASS".format(case.case_id))
        except AssertionError as e:
            self.do_excel.write_back(case.case_id + 1, resp.text, 'FAIL')
            print("第{}条测试用例执行的结果是：FAIL".format(case.case_id))
            print("期望结果是：{0}，实际结果是：{1}".format(case.expected, resp.json()))
            raise e

    def tearDown(self):
        print('用例执行完毕')
        print("******************************************************")




if __name__ == '__main__':
    unittest.main()