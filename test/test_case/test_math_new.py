#enconding: utf-8
#name:  huahua

import unittest
from ddt import ddt, data  # pip install  ddt
from  common.math_class_method import MathMethod
from  common.do_excel import DoExcel
from common.my_log import MyLog
from common.peizhi_file import ReadConfig

my_logger = MyLog()
file_path = ReadConfig('conf/math_method.conf').get_value('EXCEL', 'file_path')
#测试数据  方法三
cases = DoExcel(file_path,'add').get_data()  #装对象的列表
# t = DoExcel('method_message.xlsx', 'add')    (这样也可以)

@ddt  #装饰器 （装饰的是测试类。测试类是继承过TestCase）  （ddt, data两个要同时使用）
class TestMathClass(unittest.TestCase):  #继承TestCase

    def  setUp(self):
        self.t = DoExcel(file_path, 'add')  #这行也可以放到类外面，不用self.调用时也不需要self.

    def  tearDown(self):
       my_logger.info("——————本条用例执行完毕————————")

    @data(*cases)     # 装饰器，是装饰unittest.TestCase里面的子类的测试方法的  （相当于在调用data函数）
    # @data(cases)  data（*values）里面的*values参数是动态参数，传进来是以元组的形式  一个  值 （[对象值 ,对象值,...]）
    # data里面有几条数据执行几条用例，@data(cases)这样传只有一条数据（一个元组），就只会执行一条用例
    #@data(*cases) 这样传参数的时候脱外套，就可以把里面的值分别取出来（对象值 ,对象值,...）有几个对象值就会执行几条用例
    def  test_add_method(self,case):  # case相当于接收了把cases拆分的多个元素（对象）
        my_logger.info("——————开始执行第{0}条用例：{1}————————".format(case.case_id, case.title))
        # print('a: ',case.a)
        # print('b: ', case.b)
        # print('expected: ', case.expected)
        result = MathMethod().add(case.a,case.b)
        try:
            self.assertEqual(result,case.expected)
            test_result = 'Pass'
        except  AssertionError  as  e:
            my_logger.error("断言错误{}".format(e))
            my_logger.info("本条用例不通过")
            test_result = 'Failed'
            raise e
        finally:  # 写回结果
            self.t.write_back(case.case_id+1,6,result)     # 写回实际的结果
            self.t.write_back(case.case_id+1,7,test_result)  # 写回测试结论
            # t.write_back(case.case_id + 1, 6, result)  # 写回实际的结果
            # t.write_back(case.case_id + 1, 7, test_result)  # 写回测试结论
            my_logger.info("{0} + {1}的值是{2}".format(case.a, case.b, result))




# #测试数据  方法一   利用列表索引值获取
# test_data = DoExcel('method_message.xlsx','add').get_data()  #嵌套列表
#
# @ddt  #装饰器 （装饰的是测试类。测试类是继承过TestCase）  （ddt, data两个要同时使用）
# class TestMathClass(unittest.TestCase):  #继承TestCase
#
#     def  setUp(self):
#         self.t = DoExcel('method_message.xlsx', 'add')
#
#     def  tearDown(self):
#         print("——————本条用例执行完毕————————")
#
#     @data(*test_data)     # 装饰器，是装饰unittest.TestCase里面的子类的测试方法的  （相当于在调用data函数）
#     def  test_add_method(self,item):  # item相当于接收了把test_data拆分成的多个小列表
#         print("——————开始执行第{0}条用例：{1}————————".format(item[0],item[1]))
#         result = MathMethod().add(item[2],item[3])
#         try:
#             self.assertEqual(result,item[4])
#             test_result = 'Pass'
#         except  AssertionError  as  e:
#             print("断言错误",e)
#             print("本条用例不通过")
#             test_result = 'Failed'
#             raise e
#         finally:  # 写回结果
#             self.t.write_back(item[0]+1,6,result)     # 写回实际的结果
#             self.t.write_back(item[0]+1,7,test_result)  # 写回测试结论
#             print("{0} + {1}的值是{2}".format(item[2], item[2], result))



#
# #测试数据  方法一    利用unpack解包获取  （先导入unpack）
# test_data = DoExcel('method_message.xlsx','add').get_data()  #嵌套列表
#
# @ddt  #装饰器 （装饰的是测试类。测试类是继承过TestCase）  （ddt, data两个要同时使用）
# class TestMathClass(unittest.TestCase):  #继承TestCase
#     def  setUp(self):
#         self.t = DoExcel('method_message.xlsx', 'add')
#
#     def  tearDown(self):
#         print("——————本条用例执行完毕————————")
#
#     @data(*test_data) # 装饰器  解包后为[ ], [ ] ,[ ],[ ]...  解包后有几个执行几个用例。
#     @unpack   #把上面的数据再次拆分，根据逗号拆分，一个元素一个元素去拆分eg:每次拆分一个[1, '两个零相加', 0, 0, 1]
#     #unpack拆分成几个，下面就要用几个参数去接收。  case_id, title, a, b, excepted 解包后为5个参数
#     def  test_add_method(self, case_id, title, a, b, excepted):
#         print("——————开始执行第{0}条用例：{1}————————".format(case_id, title))
#         result = MathMethod().add(a,b)
#         try:
#             self.assertEqual(result,excepted)
#             test_result = 'Pass'
#         except  AssertionError  as  e:
#             print("断言错误",e)
#             print("本条用例不通过")
#             test_result = 'Failed'
#             raise e
#         finally:  # 写回结果
#             self.t.write_back(case_id+1, 6, result)     # 写回实际的结果
#             self.t.write_back(case_id+1, 7, test_result)  # 写回测试结论
#             print("{0} + {1}的值是{2}".format(a, b, result))




# # #测试数据  方法二   利用字典获取数据
# test_data = DoExcel('method_message.xlsx','add').get_data()  #列表，每个元素是一个字典
# @ddt  #装饰器 （装饰的是测试类。测试类是继承过TestCase）  （ddt, data两个要同时使用）
# class TestMathClass(unittest.TestCase):  #继承TestCase
#
#     def  setUp(self):
#         self.t = DoExcel('method_message.xlsx', 'add')
#
#     def  tearDown(self):
#         print("——————本条用例执行完毕————————")
#
#     @data(*test_data)     # 装饰器，是装饰unittest.TestCase里面的子类的测试方法的  （相当于在调用data函数）
#     #解包后是多个字典。{ }，{ }，{ }...
#     def  test_add_method(self,item):  # item相当于接收了把test_data这个列表拆分成的多个小字典
#         print("————开始执行第{0}条用例：{1}—————".format(item['case_id'],item['title']))
#         result = MathMethod().add(item['a'],item['b'])
#         try:
#             self.assertEqual(result,item['expected'])
#             test_result = 'Pass'
#         except  AssertionError  as  e:
#             print("断言错误",e)
#             print("本条用例不通过")
#             test_result = 'Failed'
#             raise e
#         finally:  # 写回结果
#             self.t.write_back(item['case_id']+1, 6, result)     # 写回实际的结果
#             self.t.write_back(item['case_id']+1, 7, test_result)  # 写回测试结论
#             print("{0} + {1}的值是{2}".format(item['a'], item['b'], result))



if __name__ == '__main__':
    unittest.main()   #自动执行以test_开头的用例