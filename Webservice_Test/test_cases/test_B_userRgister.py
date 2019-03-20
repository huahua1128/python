#enconding: utf-8
#name:  huahua
from suds.client import Client
import unittest
from common import contants
from common.do_excel import DoExcel
from libext.ddt import ddt,data
import json
from common.read_config import ReadConfig
from common.get_code import get_code
from common.check import *
from common.get_ip import get_ip
import time
from common import context
from common.logger import get_logger

read_config = ReadConfig()
pre_url = read_config.get_value('url', 'pre_url')


@ddt
class TestUserRegister(unittest.TestCase):

    case_dir = contants.case_dir
    do_excel = DoExcel(case_dir, 'userRegister')
    cases = do_excel.get_data()
    logger = get_logger("register")

    @classmethod
    def setUpClass(cls):
        pass
        cls.mysql = MysqlUtil(return_dict= True)  # 生成一个数据库对象，返回的是数据字典
        cls.uid_list = []

    def setUp(self):
        pass

    @data(*cases)
    def test_user_register(self,case):
        self.logger.info("开始执行{0}模块的第{1}条用例：{2}".format(case.module, case.case_id, case.title))
        if json.loads(case.data)["ip"] == "${ip}":
            get_ip()
        if json.loads(case.data)["mobile"] == "${mobile}":
            check_mobile()
            if json.loads(case.data)["verify_code"] == "${verify_code}":
                get_code(getattr(context.Context, 'mobile'))  # 调用发送验证码的函数，发送验证码并将验证码设置为Context类的一个属性
        # 先向查找出来的手机发送验证码
        elif json.loads(case.data)["mobile"] != None and len(json.loads(case.data)["mobile"]) == 11:
            get_code(json.loads(case.data)["mobile"])
        if json.loads(case.data)["user_id"] == "${user_id}":
            check_user_id()    # 覆盖Context的user_id的属性值

        data_new = context.replace(case.data)  # 正则表达式替换
        data_new = json.loads(data_new)  # 字符串转换为字典
        # print(data_new)
        if case.title == "验证码超过一分钟注册":
            time.sleep(65)
        url = pre_url + case.url
        client = Client(url)
        try:
            result = client.service.userRegister(data_new)
            msg = dict(result)["retInfo"]
        except Exception as e:
            result = e
            msg = str(e)

        try:
            case.expected = json.loads(case.expected)  # 预期结果将字符串转换为字典
            self.assertIn(case.expected["msg"], msg)  # 结果断言
            if msg == "ok":  # 数据库校验
                sql = 'SELECT * FROM user_db.t_user_info WHERE Fuser_id=\'{0}\''.format(getattr(context.Context, 'user_id'))
                result_1 = self.mysql.fetch_all(sql)
                self.assertEqual(1, len(result_1))
                self.assertEqual(data_new["channel_id"], result_1[0]["Fchannel_id"])
                self.assertEqual(data_new["ip"], result_1[0]["Fip"])
                self.assertNotEqual(data_new["mobile"], result_1[0]["Fmobile"])
                self.assertNotEqual(data_new["pwd"], result_1[0]["Fpwd"])
                self.uid_list.append(str(result_1[0]["Fuid"])+'\n')
                # setattr(context.Context, "uid_list", self.uid_list)


            self.do_excel.write_back(case.case_id + 1, msg, "PASS")
            self.logger.info("第{}条测试用例执行的结果是：PASS".format(case.case_id))

        except AssertionError as e:
            self.do_excel.write_back(case.case_id + 1, msg, 'FAIL')
            self.logger.error("第{}条测试用例执行的结果是：FAIL".format(case.case_id))
            self.logger.error("执行失败！期望结果是：{0}，实际结果是：{1}".format(case.expected, result))
            raise e

    def tearDown(self):
        self.logger.info('用例执行完毕')
        self.logger.info("******************************************************")

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close()  # 关闭数据库
        with open(contants.uid_list_dir, 'w+') as file:
            file.writelines(cls.uid_list)


if __name__ == '__main__':
    unittest.main()