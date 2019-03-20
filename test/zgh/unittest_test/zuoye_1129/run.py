#enconding: utf-8
#name:  huahua

from zgh.unittest_test.zuoye_1129.choose_excel import ChooseExcel

if  __name__=="__main__":
    ChooseExcel("method_message.xlsx", 'add', 'test_add_method').choose_excel()
    ChooseExcel("method_message.xlsx", 'sub', 'test_subb_method').choose_excel()