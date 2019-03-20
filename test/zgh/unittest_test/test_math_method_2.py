#enconding: utf-8
#name:  huahua
import  unittest
from zgh.unittest_test.math_method import MathMethod
class TestSub(unittest.TestCase):   #测试减法类

    def  test_two_positive_sub(self):
        result=MathMethod(3,2).subb()
        expected=11
        try:
            self.assertEqual(expected,result)
        except AssertionError  as  e:
            print("这是个断言错误{}".format(e))
            raise   e
        print("两个正数相减的值是{}，预期结果是{}".format(result,expected))

    def test_two_negtive_sub(self):
        result=MathMethod(-2,-5).subb()
        expected = 3
        try:
            self.assertEqual(expected, result)
        except AssertionError  as  e:
            print("这是个断言错误{}".format(e))
            raise e
        print("两个负数相减的值是{}，预期结果是{}".format(result, expected))

    def test_positive_negtive_sub(self):
        result=MathMethod(2,-4).subb()
        expected = 6
        try:
            self.assertEqual(expected, result)
        except AssertionError  as  e:
            print("这是个断言错误{}".format(e))
            raise e
        print("一正一负相减的值是{}，预期结果是{}".format(result, expected))



class  TestAbs(unittest.TestCase):   #测试绝对值类

    def test_abs_two_positive(self):  #第三条执行的用例
        result=MathMethod(2,3).a_b_s()
        expected=1
        try:
            TestAbs().assertEqual(result,expected)
        except AssertionError  as  e:
            print("出现断言错误",e)
            raise e
        print("两个正数相减的绝对值是：{}".format(result))

    def  test_abs_positive_negitve(self):   #第一条执行的用例
        result=MathMethod(2,-5).a_b_s()
        excepted=7
        try:
            self.assertEqual(result,excepted)
        except AssertionError  as  e:
            print("出现断言错误",e)
            raise e
        print("一正一负两个数相减的绝对值是：{}".format(result))

    def  test_abs_two_negtive(self):   #第二条执行的用例
        result=MathMethod(-2,-5).a_b_s()
        expected=3
        try:
            self.assertEqual(result,expected)
        except AssertionError  as  e:
            print("出现断言错误",e)
            raise   e
        print("两个负数相减的绝对值是：{}".format(result))

# if  __name__=='__main__':
#     unittest.main()

