from suds.client import Client
import unittest
from common import contants
from common.do_excel import DoExcel
from libext.ddt import ddt,data
from common import context
import json
from common.read_config import ReadConfig
from common.connect_mysql import MysqlUtil
from common.check import check_mobile
from common.logger import get_logger


@ddt
class TestSendCode(unittest.TestCase):

    case_dir = contants.case_dir
    do_excel = DoExcel(case_dir, 'sendMCode')
    cases = do_excel.get_data()
    read_config = ReadConfig()
    pre_url = read_config.get_value('url', 'pre_url')
    logger = get_logger("sendcode")

    @classmethod
    def setUpClass(cls):
        cls.mysql = MysqlUtil(return_dict= True)  # 生成一个数据库对象，返回的是数据字典

    def setUp(self):
        pass

    @data(*cases)
    def test_send_code(self,case):
        self.logger.info("开始执行{0}模块的第{1}条用例：{2}".format(case.module, case.case_id, case.title))
        data_new = context.replace(case.data)  # 正则表达式替换
        data_new = json.loads(data_new)   # 字符串转换为字典
        mobile = data_new["mobile"]    # str
        if case.title == "向未注册的手机号发送短信验证码":  # 未注册的手机号要在数据库里面去查询
            data_new["mobile"] = check_mobile()    # 最终生成的数据库里面没有的手机号放回data_new["mobile"]
        while True:   # 多次发送验证码手机号超过频率限制
            url = self.pre_url + case.url
            client = Client(url)
            try:
                result = client.service.sendMCode(data_new)
                msg = dict(result)["retInfo"]
            except Exception as e:
                result = e
                msg = str(e)
            finally:   # 跳出循环的条件
                if case.title != "向同一个号码发起多次验证码请求" or "手机号超过频率限制" in msg:
                    break

        try:
            case.expected= json.loads(case.expected)  # 预期结果将字符串转换为字典
            self.assertIn(case.expected["msg"], msg)  # 结果断言
            # 如果发送验证码成功，做数据校验
            if msg == "ok":
                sql = 'SELECT * FROM sms_db_{0}.t_mvcode_info_{1}  WHERE ' \
                      ' Fmobile_no={2}'.format(mobile[-2:], mobile[-3], mobile)
                results = self.mysql.fetch_all(sql)
                self.assertEqual(1, len(results))  # 是否有一条数据
                self.assertEqual(mobile, results[0]["Fmobile_no"])  # 加的一条数据是否是这个手机号的  results[0]["Fmobile_no"]是str

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


if __name__ == '__main__':
    unittest.main()