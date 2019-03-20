# #rnconding: utf-8
# #name:  huahua
# #编写机器人类:智能机器人属性和功能
# #颜色  品牌  大小  移动速度  价格
# # 人脸识别    #语音对讲  #紧急呼叫   #语音播报   #播放歌曲
#
# class IntelligentRobot:
#     '这是个智能机器人类，有机器人的属性和功能'
#     def __init__(self,color,brand,size,speed,price): #初始化函数
#         self.color=color
#         self.brand=brand
#         self.size=size
#         self.speed=speed
#         self.price=price
#
#     def  msg(self):
#         print("我的品牌是：{}，价格是{}，大小是{}，移动速度是{}".format(self.brand,self.price,self.size,robot_2.speed))
#
#     def  face_recognition(self):  # 人脸识别  对象方法 (只能通过对象访问)
#         print("你好呀，我可以做人脸识别！")
#
#     @staticmethod
#     def  voice_intercom(name):  #语音对讲   静态方法 (类和对象来访问)
#         print("你好呀，我可以语音对讲，你可以和{}进行通话对讲".format(name))
#
#     def  emergency_call(self,phone_number=110):    #紧急呼叫   对象方法
#         print("你好呀，我可以进行紧急呼叫，当前呼叫的号码为:",phone_number)
#
#     @classmethod
#     def  voice_announcements(cls,*args):   #语音播报   类方法 (类和对象来访问)
#         print("你好呀，我可以进行语音播报，当前播报的内容是:",args)
#
#     @classmethod
#     def   sing_song(cls,song):    #播放歌曲    类方法
#         print("你好呀，我可以播放歌曲，即将播放的歌曲是:",song)
#
#
# robot_2=IntelligentRobot('1111','2222','33333','44444',5555)
# # robot=IntelligentRobot('blue','优必选','1243*925*1110mm','0-1m/s',6599)   #创建对象
# # robot_2=IntelligentRobot('1111','2222','33333','44444',5555)
# # print("机器人价格是:",robot.price)   #对象调用属性
# # print("机器人品牌是:",IntelligentRobot.brand)   #类调用属性
# # print("机器人颜色是:",robot.color)    #对象调用属性
# # print("机器人移动速度是:",IntelligentRobot.speed)   #类调用属性
#
# # robot.face_recognition()
#
# # robot.voice_intercom('花花')
# # IntelligentRobot.voice_intercom("小明")
# #
# # robot.emergency_call()
# # robot.emergency_call(119)
# #
# # robot.voice_announcements('今天可能会有雨','提醒大家出门带雨伞','别忘记啦！')
# # IntelligentRobot.voice_announcements('下午三点要开会','请大家不要迟到了')
# #
# # robot.sing_song('传奇')
# # IntelligentRobot.sing_song('沙漠骆驼')
# # robot_2.msg()
#
#

# class Phone():
#     '这是个手机类，有手机的属性和功能'
#     def __init__(self, color, brand, size, price):  # 初始化函数
#         self.color = color
#         self.brand = brand
#         self.size = size
#         self.price = price
#
#     def  call(self,name='huahua'):   #打电话
#         print(self.price)
#         print("可以给{}打电话".format(name))
#         return  666666
#
#     @staticmethod
#     def send_msg(content):   #发短信
#         print("可以发送短信{}",content)
#
#     @classmethod
#     def watch_video(cls,*args):  #看视频
#         print("可以看{}",args)


from qita.lei_yu_duixiang import Phone  #导入父类模块

class  ApplePhone(Phone):  #ApplePhone继承Phone类
    '这是个苹果类'

    def  measure(self):   #拓展
        print("可以测量身高或者是距离")

    def  watch_video(cls):   #重写
        print("可以看电视")

ApplePhone('red','iphone','6.0','8800').measure()

# ApplePhone.send_msg('今天有雨啊，带伞')   #发短信为静态方法
# ApplePhone('red','iphone','6.0','8800').call()  #打电话为对象方法
# ApplePhone.watch_video("甄嬛传",'海王','毒液')   #看电视为类方法

