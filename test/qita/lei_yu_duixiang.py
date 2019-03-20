#enconding: utf-8
#name:  huahua

#
class Phone():
    '这是个手机类，有手机的属性和功能'
    def __init__(self, color, brand, size, price):  # 初始化函数
        self.color = color
        self.brand = brand
        self.size = size
        self.price = price

    def  call(self,name='huahua'):   #打电话
        print(self.price)
        print("可以给{}打电话".format(name))
        return  666666

    @staticmethod
    def send_msg(content):   #发短信
        print("可以发送短信",content)

    @classmethod
    def watch_video(cls,*args):  #看视频
        print("可以看",args)