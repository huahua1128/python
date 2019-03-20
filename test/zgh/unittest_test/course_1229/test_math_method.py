#enconding: utf-8
#name:  huahua

#unittest
#TestCase类   专门写用例的  （这个类的一个实例/对象 就是一条用例）
#TestCase 里面的初始化函数的methodname是每一条用例方法名。有默认值，可以不传。
import unittest   #导入unittest
from zgh.unittest_test.course_1229.math_method_2 import MathMethod    #导入测试的模块和类
class TestAdd(unittest.TestCase):  #继承TestCase类

    def __init__(self, a, b, expected, MethodName):  #重写 MethodName要传进来是因为下面的函数要用到
        # 超继承 既有子类的方法，也会执行父类
        super(TestAdd, self).__init__(MethodName)
        # MethodName是因为父类TestCase初始化函数里面有参数，这样写可以测试其他的用例
        # def __init__(self, a, b, expected):  #上面不传MethodName
        #     super(TestAdd, self).__init__('test_add')  #这里面直接写入需要测试的用例名，局限性
        self.a = a
        self.b = b
        self.expected = expected

    def setUp(self):  #重写，父类里面有
        print("---------开始执行用例-----------")

    def  tearDown(self):
        print("---------执行用例完毕-----------")

    def test_add(self):  # 多组数据测试  加法
        result = MathMethod(self.a,self.b).add()
        try:
            self.assertEqual(self.expected, result)  # 断言
        except AssertionError as e:
            print("断言出错{}".format(e))
            raise e
        print("a +  b的结果是：{}".format(result))


if  __name__=='__main__':
    unittest.main()     #会自动的在当前文件里面加载以 test_ 开头的用例


