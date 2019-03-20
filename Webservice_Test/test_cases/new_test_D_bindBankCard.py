#enconding: utf-8
#name:  huahua
#enconding: utf-8
#name:  huahua

from suds.client import Client
import unittest
from common import contants
from common.do_excel import DoExcel
from libext.ddt import ddt,data
import json
from common.read_config import ReadConfig
from common.connect_mysql import MysqlUtil
from common.get_cre_id import *

# 这个接口未完成

read_config = ReadConfig()
pre_url = read_config.get_value('url', 'pre_url')
count = 0

@ddt
class TestBindBankCard(unittest.TestCase):

    case_dir = contants.case_dir
    do_excel = DoExcel(case_dir, 'bindBankCard')
    cases = do_excel.get_data()

    @classmethod
    def setUpClass(cls):
        pass
        cls.mysql = MysqlUtil(return_dict= True)  # 生成一个数据库对象，返回的是数据字典
        try:
            with open(contants.uid_list_dir, 'r') as file:
                cls.uid_list = file.readlines()
        except FileNotFoundError as e:
            print("该文件不存在！！")

    def setUp(self):
        pass

    @data(*cases)
    def test_bind_bank_card(self,case):
        print("开始执行{0}模块的第{1}条用例：{2}".format(case.module, case.case_id, case.title))

        global count
        print(count)
        print(self.uid_list)
        self.uid = str(self.uid_list[count])[:-1]

        data_new = context.replace(case.data)  # 正则表达式替换
        data_new = json.loads(data_new)  # 字符串转换为字典

        url = pre_url + case.url
        client = Client(url)
        try:
            result = client.service.bindBankCard()
            msg = dict(result)["retInfo"]
        except Exception as e:
            result = e
            msg = str(e)

        try:
            case.expected = json.loads(case.expected)  # 预期结果将字符串转换为字典
            self.assertIn(case.expected["msg"], msg)  # 结果断言
            self.do_excel.write_back(case.case_id + 1, msg, "PASS")
            print("第{}条测试用例执行的结果是：PASS".format(case.case_id))

        except AssertionError as e:
            self.do_excel.write_back(case.case_id + 1, msg, 'FAIL')
            print("第{}条测试用例执行的结果是：FAIL".format(case.case_id))
            print("执行失败！期望结果是：{0}，实际结果是：{1}".format(case.expected, result))
            raise e

    def tearDown(self):
        print('用例执行完毕')
        print("******************************************************")

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close()  # 关闭数据库


if __name__ == '__main__':
    unittest.main()