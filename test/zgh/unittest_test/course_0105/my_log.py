import logging  # 所以不能以logging为文件名（自己的文件命名不能和引入的模块名冲突）

class MyLog:
    '''自己写的日之类'''

    def my_log(self,level, msg):
        # 收集器 -----创建一个日志收集器
        my_logger = logging.getLogger('python13')
        # getLogger 是个函数，必须传一个参数，作为自己的日志收集器的名字，否则还是会用root logger
        my_logger.setLevel('DEBUG')  # 给日志收集器设置level   (相当于第一次过滤)

        # 输出格式   Formatter 是个类  规定日志输出的格式
        formatter = logging.Formatter('%(asctime)s-[%(levelname)s]-[%(lineno)d]-[日志信息]:%(message)s')

        # 输出渠道 -----指定输出渠道
        ch = logging.StreamHandler()  # 创建一个输出到控制台的渠道
        ch.setLevel('INFO')  # 给自己设置的渠道设置level  (相当于第二次过滤)
        ch.setFormatter(formatter)

        # 输出渠道 -----输出到指定文件  文件路径 绝对路径和相对路径都可以
        fh = logging.FileHandler('huahua.log',encoding='utf-8')  # 指定参数，默认a模式。有文件，追加。没文件，新建
        fh.setLevel('DEBUG')
        fh.setFormatter(formatter)

        # 对接  日志收集器和输出渠道进行对接
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if level == 'DEBUG':
            my_logger.debug(msg)  # 用自己的日志收集器去收集（logging调用的是root级别的）
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        # 删除收集器 ，防止信息重复输出
        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log('DEBUG', msg)

    def info(self, msg):
        self.my_log('INFO', msg)

    def warning(self, msg):
        self.my_log('WARNING', msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self, msg):
        self.my_log('CRITICAL', msg)

if  __name__ == '__main__':
    my_loger = MyLog()
    my_loger.error('99999999999999999')
    my_loger.info('6666666666666666666')