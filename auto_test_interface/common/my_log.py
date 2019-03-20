import logging  # 所以不能以logging为文件名（自己的文件命名不能和引入的模块名冲突）
from common.peizhi_file import ReadConfig

class MyLog:
    '''自己写的日之类'''

    def __init__(self):
        self.in_level = ReadConfig('conf/math_method.conf').get_value('LOG', 'in_level')
        self.out_level = ReadConfig('conf/math_method.conf').get_value('LOG', 'out_level')
        self.file_level = ReadConfig('conf/math_method.conf').get_value('LOG', 'file_level')
        self.file_path = ReadConfig('conf/math_method.conf').get_value('LOG', 'file_path')
        self.format = ReadConfig('conf/math_method.conf').get_value('LOG', 'formatter')
        # 收集器 -----创建一个日志收集器
        self.my_logger = logging.getLogger('python13')  # getLogger 是个函数，必须传一个参数，作为自己的日志收集器的名字，否则还是会用root logger
        self.my_logger.setLevel(self.in_level)  # 给日志收集器设置level   (相当于第一次过滤)

        # 输出格式   Formatter 是个类  规定日志输出的格式
        self.formatter = logging.Formatter(self.format)

        # 输出渠道 -----指定输出渠道
        self.ch = logging.StreamHandler()  # 创建一个输出到控制台的渠道
        self.ch.setLevel(self.out_level)  # 给自己设置的渠道设置level  (相当于第二次过滤)
        self.ch.setFormatter(self.formatter)

        # 输出渠道 -----输出到指定文件  文件路径 绝对路径和相对路径都可以
        self.fh = logging.FileHandler(self.file_path,encoding='utf-8')  # 指定参数，默认a模式。有文件，追加。没文件，新建
        self.fh.setLevel(self.file_level)
        self.fh.setFormatter(self.formatter)

    def add_handler(self):
        # 对接  日志收集器和输出渠道进行对接
        self.my_logger.addHandler(self.ch)
        self.my_logger.addHandler(self.fh)

    def remove_handler(self):
        # 删除收集器 ，防止信息重复输出
        self.my_logger.removeHandler(self.ch)
        self.my_logger.removeHandler(self.fh)

    def debug(self, msg):
        self.add_handler()
        self.my_logger.debug(msg)
        self.remove_handler()

    def info(self, msg):
        self.add_handler()
        self.my_logger.info(msg)
        self.remove_handler()

    def warning(self, msg):
        self.add_handler()
        self.my_logger.warning(msg)
        self.remove_handler()

    def error(self, msg):
        self.add_handler()
        self.my_logger.error(msg)
        self.remove_handler()

    def critical(self, msg):
        self.add_handler()
        self.my_logger.critical(msg)
        self.remove_handler()


if  __name__ == '__main__':
    my_loger = MyLog()
    my_loger.error('999999999999999995555555')
    my_loger.info('666666666666666666655555555')