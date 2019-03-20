#enconding: utf-8
#name:  huahua

#unittest
#TestCase类   专门写用例的  （这个类的一个实例/对象 就是一条用例）
#TestCase 里面的初始化函数的methodname是每一条用例方法名。有默认值，可以不传。
import unittest   #导入unittest
from zgh.unittest_test.math_method import MathMethod    #导入测试的模块和类
class TestAdd(unittest.TestCase):  #继承TestCase类

    def setUp(self):  #重写，父类里面有
        print("---------开始执行用例-----------")

    def  tearDown(self):
        print("---------执行用例完毕-----------")

    # def test_add(self):  # 多组数据测试(这个方法不可以)
    #     test_data = [[0, 0, 0], [1, 4, 5], [-5, 4, -1]]
    #     for item in test_data:
    #         result = MathMethod(item[0], item[1]).add()
    #     try:
    #         self.assertEqual(item[2], result)  # 断言
    #     except AssertionError as  e:
    #         print("断言出错{}".format(e))
    #         raise e
    #     print("a +  b的结果是：{}".format(result)

    def test_add_two_zero(self):  #必须以test开头，不能传参
        result=MathMethod(0,0).add()   #两个0相加
        expected=0  #(期望结果)
        try:
            # self.assertTrue(result)
            self.assertEqual(expected,result)   #断言
            # self.assertFalse(result)
        except AssertionError as  e:
            print("断言出错{}".format(e))   #处理
            raise  e    #抛出异常，否则不抛出直接执行，有异常时已经处理了就显示通过了
        print("两个0相加的结果是：{}".format(result))

    def test_add_two_negtive(self):    #两个负数相加
        result=MathMethod(-1,-3).add()
        # expected = 1
        try:
            self.assertIsNotNone(result)
            # self.assertEqual(expected,result)   #断言
        except AssertionError as  e:
            print("断言出错{}".format(e))
            raise e
        print("两个负数相加的结果是：{}".format(result))

    def  test_add_negtive_positive(self):   #一正一负相加
        result=MathMethod(-1,3).add()
        expected = 2
        try:
            self.assertEqual(expected,result)   #断言
        except AssertionError as  e:
            print("断言出错{}".format(e))
            raise  e
        print("一正一负相加的结果是：{}".format(result))



if  __name__=='__main__':
    unittest.main()     #会自动的在当前文件里面加载以 test_ 开头的用例


