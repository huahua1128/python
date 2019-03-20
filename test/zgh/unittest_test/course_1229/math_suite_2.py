#enconding: utf-8
#name:  huahua

#起py文件名的时候不要suite.py
import unittest
from zgh.unittest_test.course_1229.test_math_method import TestAdd #模块加载用例
import HTMLTestRunnerNew
suite=unittest.TestSuite()  #对象
#多组测试数据加载用例
loader=unittest.TestLoader()
test_data = [[0, 0, 0], [1, 4, 5], [-5, 4, -1]]  #a b  expcted
for item in test_data:
    suite.addTest(TestAdd(item[0],item[1],item[2],'test_add'))

#执行用例   将用例写到html文件中
with open('course_1229.html','wb')  as  file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title="花花的第一份报告",
                                            description='这是个数学类的测试报告',
                                            tester="花花")
    runner.run(suite)