#enconding: utf-8
#name:  huahua

from zgh.unittest_test.course_0103.test_math import TestMathClass
from zgh.unittest_test.course_0103.do_excel import DoExcel
import unittest
import HTMLTestRunnerNew

suite_1=unittest.TestSuite()

#测试数据
# #方法二：
# test_data = DoExcel('method_message.xlsx','add').get_data()  #列表
#
# for item in test_data:  # 根据key取值
#     suite_1.addTest(TestMathClass(item['a'], item['b'], item['expected'], 'test_add_method'))

# 测试数据
# 方法三：
cases = DoExcel('method_message.xlsx','add').get_data()  #装对象的列表

for case in cases:  # 每一个对象都有case_id  title  a  b  expected这些值
    suite_1.addTest(TestMathClass(case.case_id,case.title,case.a, case.b, case.expected, 'test_add_method'))  #再用对象去访问他的值


with open('add report.html','wb')  as  file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title="花花的关于测试数学类的报告",
                                            description='这是个数学类的测试报告',
                                            tester="花花")
    runner.run(suite_1)