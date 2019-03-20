# file=open("apython13.txt","w",encoding='utf-8')
# try:
#     print("读操作之前")
#     res=file.read()  #读操作  -----异常出现在这里
#     print("读操作之后")
#     print("读操作获取的结果：{}".format(res))
# except:
#     file.write("读操作报错啦")
#     print("读操作报错啦")
#
# print("13期的同学们晚上好！")

# L = [1, 2, 3]
# try:
#     file = open("apython13.txt", "w", encoding='utf-8')
#     try:
#         print("获取列表数据",L[4])  #索引取值异常-----中断
#     except  IndexError  as  e:
#         print("列表数据读取错误{}".format(e))
#         file.write("列表数据读取错误{}".format(e))# 把e写到file中
#
#     print("读操作之前")
#     res=file.read()  #读操作异常  -----中断
#     print("读操作之后")
#     print("读操作获取的结果：{}".format(res))
# except IOError  as e:
#     file.write("读操作报错啦{}".format(e))#把e写到file中
#     print("读操作报错啦{}".format(e))
#
# print("13期的同学们晚上好！")

#
# try:
#     file = open("apython13.txt", "w", encoding='utf-8')
#     print("读操作之前")
#     res=file.read()  #读操作异常  -----中断
#     print("读操作之后")
#     print("读操作获取的结果：{}".format(res))
#     TestResult='Pass'
# except IOError  as e:
#     TestResult='Failed'
#     file.write("读操作报错啦{}".format(e))#把e写到file中
#     print("读操作报错啦{}".format(e))
# finally:
#     file.write(TestResult) #必须要保证这个变量在try和except中都存在
#     file.write("我执行完毕了，我是finally")
#
# print("13期的同学们晚上好！")


#
# try:
#     file = open("apython13.txt", "w+", encoding='utf-8')
#     print("读操作之前")
#     res=file.read()  #读操作正常，不中断
#     print("读操作之后")
#     print("读操作获取的结果：{}".format(res))
#     TestResult='Pass'
# except IOError  as e:
#     TestResult='Failed'
#     print(TestResult)
#     file.write("读操作报错啦{}".format(e))
#     print("读操作报错啦{}".format(e))
# else:
#     print(TestResult)
#     file.write("我执行完毕了，我是finally")
#
# print("13期的同学们晚上好！")

#上下文管理器
file=open("apython13.txt",'w+',encoding='utf-8')
file.write("今天天气很好")
print(file.closed)  #判断文件是否关闭
file.close()
print(file.closed)  #判断文件是否关闭

with open("apython13.txt",'w+',encoding='utf-8')  as  file:
    file.write("明天也要加油呀")
print("2.",file.closed)   #判断文件是否关闭