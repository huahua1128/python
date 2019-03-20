#enconding: utf-8
#name:  huahua

import unittest
from  zgh.unittest_test.zuoye_1129.math_class_method import MathMethod
class TestMathClass(unittest.TestCase):

    def  __init__(self,a,b,expected,testcase_name):
        super(TestMathClass,self).__init__(testcase_name)
        self.a = a
        self.b = b
        self.expected = expected

    def  setUp(self):
        print("——————开始执行本条用例————————")

    def  tearDown(self):
        print("——————本条用例执行完毕————————")

    def  test_add_method(self):
        result1=MathMethod().add(self.a,self.b)
        try:
            self.assertEqual(result1,self.expected)
        except  AssertionError  as  e:
            print("断言错误",e)
            print("本条用例不通过")
            raise e
        print("{0} + {1}的值是{2}".format(self.a, self.b, result1))

    def  test_subb_method(self):
        result2 = MathMethod().subb(self.a,self.b)
        try:
            self.assertEqual(result2,self.expected)
        except  AssertionError  as  e:
            print("断言错误",e)
            print("本条用例不通过")
            raise  e
        print("{0} - {1}的值是{2}".format(self.a, self.b, result2))