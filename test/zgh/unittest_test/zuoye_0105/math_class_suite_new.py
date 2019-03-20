#enconding: utf-8
#name:  huahua

from zgh.unittest_test.zuoye_0105.test_math_new import TestMathClass
import unittest
import HTMLTestRunnerNew

suite=unittest.TestSuite()

#测试数据
# 利用ddt
# #loader加载方式  ddt里面  @data（*x）里能拆分几个数据就运行几条用例，所以加载用例时可以加载整个类（类里面只有加法）
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(TestMathClass))

with open('add  new report.html', 'wb')  as  file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title="花花的关于测试数学类的报告",
                                            description='这是个数学类的测试报告',
                                            tester="花花")
    runner.run(suite)