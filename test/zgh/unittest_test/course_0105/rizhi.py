# python有一个自带的日志系统  logging

import logging  # 所以不能以logging为文件名（自己的文件命名不能和引入的模块名冲突）

# root logger  收集日志的容器  若不定义一个logger,那么就默认使用root logger（最高级别的logger）
# 默认收集warning以上的级别信息
#handlers 渠道 （两种渠道）控制台--> console  文本--> file_handler  若handler不指定渠道，则会默认输出到控制台
#pre-defined format 按照提前设置好的格式进行输出 (默认格式-> 级别：日志收集器名：日志信息)

# logging.debug('这是个debug信息')  # 要传入一个msg
# logging.info('这是个info信息')
# logging.warning('这是个warning信息')
# logging.error('这是个error信息')
# logging.critical('这是个critical信息')



# 写一个自己的日志系统

# 收集器 -----创建一个日志收集器
my_logger = logging.getLogger('python13')
# getLogger 是个函数，必须传一个参数，作为自己的日志收集器的名字，否则还是会用root logger
my_logger.setLevel('DEBUG')  # 给日志收集器设置level   (相当于第一次过滤)

# 输出格式   Formatter 是个类  规定日志输出的格式
# formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
# 当前时间    日志级别     当前日志执行的（文件名）模块名     日志收集器名     日志信息
# 这些参数可以自己加减修改
# formatter = logging.Formatter('%(asctime)s-[%(levelname)s]-[日志信息]:%(message)s')
formatter = logging.Formatter('%(asctime)s-[%(levelname)s]-[%(lineno)d]-[日志信息]:%(message)s')

# 输出渠道 -----指定输出渠道
ch = logging.StreamHandler()  # 创建一个输出到控制台的渠道
ch.setLevel('ERROR')  # 给自己设置的渠道设置level  (相当于第二次过滤)
ch.setFormatter(formatter)

# 输出渠道 -----输出到指定文件  文件路径 绝对路径和相对路径都可以
fh = logging.FileHandler('huahua.log',encoding='utf-8')  # 指定参数，默认a模式。有文件，追加。没文件，新建
fh.setLevel('INFO')
fh.setFormatter(formatter)

# 对接  日志收集器和输出渠道进行对接
my_logger.addHandler(ch)
my_logger.addHandler(fh)

my_logger.debug('这是一个debug信息')   # 用自己的日志收集器去收集（logging调用的是root级别的）
my_logger.info('这是一个info信息')
my_logger.warning('这是一个warning信息')
my_logger.error('这是一个error信息')
my_logger.critical('这是一个critical信息')