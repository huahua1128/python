# # fp = open('test.txt','r')
# # content=fp.read(5)
# # print(content)
# # fp.close()
#
# # fp = open('test.txt','r')
# # lines=fp.readlines()
# # print(lines)
# # fp.close()
# #
# # fp = open('test_1.txt','w')
# # list_1=['666','nihao','111']
# # fp.writelines(list_1)
# # fp.close()
#
# # fp = open('test_1.txt','w')
# # po=fp.tell()
# # print("位置1为:{0}".format(po))
# # list_1=['666','nihao','111']
# # fp.writelines(list_1)
# # po=fp.tell()
# # print("位置为2:{0}".format(po))
# # fp.close()
# #
# # fp = open('test_1.txt','w+')
# # list_1=['666','nihao','111']
# # fp.writelines(list_1)
# # fp.close()
#
# #
# # import os
# # os.rename('test.txt','huahua.txt')
# # path =os.getcwd()
# # print(path)
#
# # print(os.getcwd())
#
# # print(os.listdir('.'))
#
#
# # import os
# # path=os.getcwd()
# # test_path =os.path.join(path,"huahua")
# # # print(test_path)
# # all_files=os.listdir(test_path)
# # print(all_files)
#
#
# # a = 'pythyon'
# # i = 2
# # for element in a:
# #     if element == 'y':
# #         pass
# #     else:
# #         print(element+str(i))
#
# # import  os
# # print(os.getcwd())
# # os.chdir("E:\\ZGH\\test\\zgh_2")
# # f=open('test_1.txt','a+')
# # f.write('jin tian yao jia you')
# # f.close()
# # print(os.getcwd())
# #
# # os.chdir("E:\\ZGH\\test\\zgh")
# # print(os.getcwd())
#
# # f=open("test_99.txt",'a+')
# # f.close()
#
#
# # os.mkdir("xhh")
#
#
# # import  os
#
# # os.rmdir("E:\\ZGH\\test\\test")
# import shutil
# shutil.rmtree("E:\\ZGH\\test\\as")
# # os.chdir("E:\\ZGH\\test\\test")
# # os.remove("txt")
#
#
# # import zgh.leijia
# # leijia.ladd(100)



# f=open("E:\\ZGH\\test\\zgh\\jiayou.txt","r+")
# print(f.read())
# f.write("3333"
#         "hhhh"
#         "en")
# print(f)
# f.close()
#
# f=open("jiayou.txt","r+")
# # f.write("12378")
# print(f.read())
# # # f=open("jiayou.txt","w+")
# # # f.write("456")
# # # content=f.read()
# # print(content)
# f.close()


# f=open("test_1.txt","w+")
# print(f.read())
# f.close()

# f=open("E:\\ZGH\\test\\zgh\\jiayou.txt","w+")
#
# f.write("6669998887")
# lenth=len(f.read())
# print(lenth)
# print(f.tell())
# f.seek(8)
# print(f.read())
# f.close()


# f=open("E:\\ZGH\\test\\zgh\\jiayou.txt","r+")
# print(f.read())
# f.close()


# f=open("test_1.txt","r+")
# f.write("232323dfdfd"
#         "eennen333"
#         "45ddf")
# f.seek(5,0)
# print(f.read())
# f.close()


# f=open("test_1.txt","r+")
# str=f.read()
# print(str.split(','))
# f.close()


# def readList(filename):
#     f = open(filename, "r+")
#     lines=f.readlines()
#     list=[]
#     for item in lines:
#             str=item.replace('\n', '')
#             list.append(str)
#     return list
#
# list_2=readList("zzz.txt")
#
# print(list_2)



# def add(*args):
#     print(args)
#     count=0
#     for item in args:
#         count+=item
#     return count
#
# # print("求和为{0}".format(add(1,5,2,3)))
# a=['nihao','加油']
# t=['wulei','huahua','hhhhh']
# a.append(t)
# print(a)

import os
# path=os.getcwd()    #得到1010文件的路径
# test_path =os.path.join(path,'test')    #test目录的路径
# all_files=os.listdir(test_path)    #打印出test目录下的文件
#
# for file in all_files:
#     file_com=os.path.splitext(file)   #分别将文件名和后缀分开
#     filename=file_com[0]    #分别存入文件名
#     extention=file_com[1]    #存入后缀名
#
#     new_file=filename+'_知了课堂'+extention     #新的文件名
#     old_file_path=os.path.join(test_path,file)     #
#     new_file_path= os.path.join(test_path,new_file) #
#     print(old_file_path)
#     print(new_file_path)
#     os.rename(old_file_path,new_file_path)     #
#
# os.mkdir("dhh")

# f=open("E:\\ZGH\\test\\zgh\\test_1.txt","r+")
# f.write("232323dfdgdgdfd哈哈哈哈哈"
#         "eennen3dgd33"
#         "45ddfgdgf")
# f.seek(5,0)
# print(f.read())
# f.close()


