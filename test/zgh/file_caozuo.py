# file=open('python13.txt',encoding='UTF-8')  #中文要加编码utf-8
# print(file.read()) #读取所有内容
# print(file.read(5))   #读取不到，因为上面读完了，光标在最后
# print(file.readline())   #按行读取，每读一行
#
# for i  in range(10):
#     if 4<i<9:
#         print(file.readline())   #读取4-8行
#     else:
#         file.readline()  #读取不打印
# file.close()

# a=5
# file=open('python13.txt','a+',encoding='UTF-8')  #中文要加编码utf-8
# file.write("哈哈哈哈，今天天气真好")  #追加到后面
# file.seek(0,0)  #光标移到开头
# print(file.read())

