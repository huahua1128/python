import unittest
from  zgh.unittest_test.course_0103.math_class_method import MathMethod
from  zgh.unittest_test.course_0103.do_excel import DoExcel

class TestSub(unittest.TestCase):  #继承TestCase

    def  setUp(self):
        self.t = DoExcel('method_message.xlsx', 'subb')

    def  tearDown(self):
        print("——————本条用例执行完毕————————")


def  test_subb_method(self):
    result = MathMethod().subb(self.a,self.b)
    try:
        self.assertEqual(result,self.expected)
    except  AssertionError  as  e:
        print("断言错误",e)
        print("本条用例不通过")
        raise  e
    print("{0} - {1}的值是{2}".format(self.a, self.b, result))