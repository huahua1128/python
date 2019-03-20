#-------- 方法一

# def print_star(Num) :
#     start = int(-Num/2)
#     end = -start + 1
#     for i in range(start, end):
#         tempStr = ""
#         if Num % 2 == 0 and i == 0: #偶数特殊处理
#             continue
#         for j in range(start, end):
#             if abs(i) + abs(j) == end-1 :
#                 tempStr += "*"
#             else:
#                 tempStr += " "
#         print(tempStr)
#
# while True:
#     intNum = input("please input a num data:\n")
#     print_star(int(intNum))


#-------- 方法二

def print_star(Num) :
    for i in range(1, Num+1, 2):            #上半部分
        t = (Num-i)//2
        print(' '*t + '*'*i + ' '*t)
    for i in reversed(range(1, Num, 2)):    #下半部分
        t = (Num-i)//2
        print(' '*t +'*'*i + ' '*t)
    
while True:
    intNum = input("please input a num data:\n")
    print_star(int(intNum))


#-------- 方法三
# def print_star(Num) :
    # s = '*'
    # for i in range(1, Num+1, 2):
        # print((s*i).center(Num))
    # for i in reversed(range(1, Num, 2)):
        # print((s*i).center(Num))
        
# while True:
    # intNum = input("please input a num data:\n")
    # print_star(int(intNum))
