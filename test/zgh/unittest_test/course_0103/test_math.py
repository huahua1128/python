#enconding: utf-8
#name:  huahua

import unittest
from  zgh.unittest_test.course_0103.math_class_method import MathMethod
from  zgh.unittest_test.course_0103.do_excel import DoExcel
class TestMathClass(unittest.TestCase):

    def  __init__(self,case_id,title,a,b,expected,testcase_name):
        super(TestMathClass,self).__init__(testcase_name)  #超继承
        self.case_id = case_id   # 用例id
        self.title = title   # 用例标题
        self.a = a
        self.b = b
        self.expected = expected
        # self.t = DoExcel('method_message.xlsx','add')   #创建对象（方便后面写回）

    def  setUp(self):
        self.t = DoExcel('method_message.xlsx', 'add')
        print("——————开始执行第{0}条用例：{1}————————".format(self.case_id,self.title))

    def  tearDown(self):
        print("——————本条用例执行完毕————————")

    def  test_add_method(self):
# 这里不能直接右键运行，是先创建一个对象去运行，因为现在超继承有很多参数，要传参。case_id,title,a,b,expected,testcase_name
# 原来可以运行是因为原来的参数有默认值，运行时自己就新建对象了。 methodName有默认值
        result=MathMethod().add(self.a,self.b)
        try:
            self.assertEqual(result,self.expected)
            test_result = 'Pass'
        except  AssertionError  as  e:
            print("断言错误",e)
            print("本条用例不通过")
            test_result = 'Failed'
            raise e
        finally:  # 写回结果
            self.t.write_back(self.case_id+1,6,result)     # 写回实际的结果
            self.t.write_back(self.case_id+1,7,test_result)  # 写回测试结论
            print("{0} + {1}的值是{2}".format(self.a, self.b, result))

    def  test_subb_method(self):
        result = MathMethod().subb(self.a,self.b)
        try:
            self.assertEqual(result,self.expected)
        except  AssertionError  as  e:
            print("断言错误",e)
            print("本条用例不通过")
            raise  e
        print("{0} - {1}的值是{2}".format(self.a, self.b, result))

if __name__ == '__main__':
    unittest.main()   #自动执行以test_开头的用例