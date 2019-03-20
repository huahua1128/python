from  zgh.unittest_test.zuoye_1129.excel_operation import Excel_Operation
from  zgh.unittest_test.zuoye_1129.test_math import TestMathClass
import  unittest
import HTMLTestRunnerNew

class  ChooseExcel():

    def  __init__(self,excel_name,sheet_name,test_case_name):
        self.excel_name = excel_name
        self.sheet_name = sheet_name
        self.test_case_name = test_case_name

    def choose_excel(self):
        suite_1 = unittest.TestSuite()
        list_data=Excel_Operation(self.excel_name,self.sheet_name).read_data()
        count = 1
        for  i  in  list_data:
            count += 1
            a=i['a']
            b=i['b']
            expected=i['expected']
            suite_1.addTest(TestMathClass(a,b,expected, self.test_case_name))
            if 'add' in self.test_case_name:
                result = a + b
            else:
                result = a - b
            Excel_Operation(self.excel_name,self.sheet_name).write_data(count,4,result)
            if  result == expected:
                Excel_Operation(self.excel_name,self.sheet_name).write_data(count, 5, 'Pass')
            else:
                Excel_Operation(self.excel_name,self.sheet_name).write_data(count, 5, 'Failed')

        with open(self.test_case_name+'.html', 'wb')  as  file:
            runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                          verbosity=2,
                                                          title="花花的关于测试数学类的报告",
                                                          description='这是个数学类的测试报告',
                                                          tester="花花")
            runner.run(suite_1)