from  configparser import ConfigParser

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


if  __name__ == '__main__':
   res= ReadConfig('conf/math_method.conf').get_value('Case', 'button')
   print(res)
   t=eval(res)
   print(type(t))
