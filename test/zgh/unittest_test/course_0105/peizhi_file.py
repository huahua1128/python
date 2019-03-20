# import configparser #configparser模块下的ConfigParser类是配置类，专门读取配置文件的
# 上面那样导入，新建对象时，cf = configparser.ConfigParser()

# from  configparser import ConfigParser  #若这样传，下面的对象cf = ConfigParser()直接调用类

# #配置文件的使用
# cf = ConfigParser()
# cf.read('case.conf',encoding='utf-8')  # 相当于open，是以对象的方式调用里面的方法
#
# # 读值方法一
# # value_1 = cf.get('StudentInfo','class_name') # 一次get只能一个片段一个option,获取多个值就多次调用get
# # # get里面传值[片段名，option],先定位片段，再定位option(相当于字典中的key),value(相当于字典中的value)
# # value_2 = cf.get('TeacherInfo','t3')
# # print(value_1)
# # print(value_2)
#
# #读值方法二
# # value = cf['TeacherInfo']['t1']   #一层一层的去定位
# # print(value)
#
# value = cf.get('TeacherInfo','avg_age')
# print(value)
# print(type(value))
#
# #转换类型方法一  eval  字典 元组 列表
# value = eval(cf.get('TeacherInfo', 't_name'))
# print(value)
# print(type(value))
#
# #转换类型方法二  整数  浮点数 布尔值
# value_1 = cf.getint('StudentInfo','student_num')
# value_2 = cf.getfloat('TeacherInfo','gride')
# value_3 = cf.getboolean('TeacherInfo','age')
# print(type(value_1))
# print(type(value_2))
# print(type(value_3))



#写一个类
from configparser import ConfigParser
class  ReadConfig:
    ''' 读配置文件的类 '''
    def __init__(self, file):  # file是你要读取的配置文件名
        self.cf = ConfigParser()
        self.cf.read(file, encoding = 'utf-8')

    def get_value(self, section, option):
        return self.cf.get(section, option)

    def get_int(self, section, option):
        return self.cf.getint(section, option)

    def get_float(self, section, option):
        return self.cf.getfloat(section, option)

    def get_boolean(self, section, option):
        return self.cf.getboolean(section, option)

    def get_value_2(self, section, option):
        return eval(self.cf.get(section, option))


if  __name__ == '__main__':
   res= ReadConfig('case.conf').get_boolean('TeacherInfo', 'age')
   print(res)
   print(ReadConfig('case.conf').get_float('TeacherInfo', 'gride'))
   print(type(ReadConfig('case.conf').get_value('StudentInfo', 'class_name')))
   print(type(ReadConfig('case.conf').get_value_2('TeacherInfo', 't_name')))