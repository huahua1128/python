#enconding: utf-8
#name:  huahua

import  unittest
from zgh.unittest_test.jd_zuoye import test_jd_method
import HTMLTestRunnerNew

suite111=unittest.TestSuite()

#方法二  通过模块加载测试用例
loader111 = unittest.TestLoader()
suite111.addTest(loader111.loadTestsFromModule(test_jd_method))  #执行时要手动输入支付方式


#生成html测试报告
with open("test report.html",'wb')  as  file666:
    runner111 = HTMLTestRunnerNew.HTMLTestRunner(stream=file666,
                                            verbosity=2,
                                            title="huahua's test report of Jingdong class",
                                            description="This report is about the test report of Jingdong class",
                                            tester="花花—13133")
    runner111.run(suite111)