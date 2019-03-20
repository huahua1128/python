# n=5
# n=5
# for i in range(1,4):
#         for  j  in  range(i,i+1):
#             print((3-i)*' '+(2*i-1)*'*')
# for m  in range(1,3):
#         for  k in range(m,m+1):
#            print(m*' '+(n-2*m)*'*')
#
# #n=6
# n=6
# for i in range(1,int(n/2+1)):
#     for  j  in  range(i,i+1):
#         print((3-i)*' '+(2*i-1)*'*')
# print((int(n/2)-int(n/2))*' '+(2*int(n/2)-1)*'*')
# for m  in range(1,3):
#         for  k in range(m,m+1):
#             print(m*' '+(n-1-2*m)*'*')

#
def print_star(n):
    if n>1  and  n%2!=0:
        for i in range(1,(n//2+2)):
            for  j  in  range(i,i+1):
                print((n//2+1-i)*' '+(2*i-1)*'*')
        for m  in range(1,n//2+1):
            for  k in range(m,m+1):
                print(m*' '+(n-2*m)*'*')
    else:
        for i in range(1,(n//2+1)):
            for  j  in  range(i,i+1):
                print((n//2-i)*' '+(2*i-1)*'*')
        print((n//2-n//2)*' '+(2*(n//2)-1)*'*')   
        for m  in range(1,n//2):
                for  k in range(m,m+1):
                    print(m*' '+(n-1-2*m)*'*')
res=print_star(16)


