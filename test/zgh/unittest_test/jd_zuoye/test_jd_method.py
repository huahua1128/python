#enconding: utf-8
#name:  huahua

import unittest
from zgh.unittest_test.jd_zuoye.jd import JingDong123
class TestJingDong(unittest.TestCase):

    def  setUp(self):
       print("----------test case start execution-----------")

    def  tearDown(self):
        print("----------execution of test cases is complete-----------")

    def  test_jd_method_01(self):  #第一条用例，账号密码错误
        res_666=JingDong123().settlement(136,'huahua','123321')
        try:
            self.assertFalse(res_666)
        except  AssertionError  as  e:
            print("Assertion  error",e)
            print("This test case does not pass")
            raise e
        else:
            print("This test case  passes")

    def  test_jd_method_02(self):   #第二条用例，账号密码正确的情况下，支付方式为微信
        print("本条用例请选择微信支付")
        res_777=JingDong123().settlement(136,'huahua','123456')
        try:
            self.assertIn(res_777,range(10,51))
        except  Exception  as  e:
            print("Assertion  error",e)
            print("This test case does not pass")
            raise e
        else:
            print("This test case  passes")

    def test_jd_method_03(self):   #第三条用例，账号密码正确的情况下，金额改变，支付方式为微信
        print("本条用例请选择微信支付")
        res_888=JingDong123().settlement(12,'huahua','123456')
        try:
            self.assertIn(res_888,range(10, 51))
        except  AssertionError  as  e:
            print("Assertion  error",e)
            print("This test case does not pass")
            raise  e
        else:
            print("This test case  passes")

    def  test_jd_method_04(self):   #第三条用例，账号密码正确的情况下，金额改变，支付方式为银联
        print("本条用例请选择银联支付")
        res_999=JingDong123().settlement(12,'huahua','123456')
        try:
            self.assertEqual(res_999,0)
        except  Exception  as  e:
            print("Assertion  error", e)
            print("This test case does not pass")
            raise e
        else:
            print("This test case  passes")
