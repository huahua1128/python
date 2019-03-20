#enconding: utf-8
#name:  huahua
#起py文件名的时候不要suite.py

import unittest
from  zgh.unittest_test import test_math_method_2
from   zgh.unittest_test import test_math_method_1
import HTMLTestRunnerNew

# from  zgh.unittest_test.test_math_method_1 import TestAdd  #导入放用例的模块的TestAdd 类
# from  zgh.unittest_test.test_math_method_2  import TestSub  #导入放用例的模块的TestSub类
# from  zgh.unittest_test.test_math_method_2  import  *   #导入放用例的模块的所有类
# suite  集合套件  TestSuite 测试套件  存储加载用例

suite=unittest.TestSuite()  #对象

#方法一：    #加载用例
# suite.addTest(TestAdd('test_add_two_zero'))   #必须以字符串加入
# suite.addTest(TestSub('test_two_positive_sub'))

#方法二：通过测试类来加载测试用例
# loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromTestCase(test_math_method_2.TestAdd))

# 方法三：通过模块去加载用例
# loader=unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_math_method_2))   #直接导入到模块

#多组测试数据加载用例
loader=unittest.TestLoader()
suite.addTest(loader.loadTestsFromTestCase(test_math_method_1.TestAdd))



#执行用例
#将测试报告写在txt中
# with open('py13.txt','w',encoding='utf-8')  as  file:
# # 执行用例
#     runner=unittest.TextTestRunner(stream=file,  #写入的到哪
#                                descriptions=True,  #描述
#                                verbosity=1)   #
#     runner.run(suite)    #执行测试集里面的用例

#执行用例
#将用例写到html文件中
with open('190101.html','wb')  as  file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title="花花的第一份报告",
                                            description='这是个数学类的测试报告',
                                            tester="花花")
    runner.run(suite)