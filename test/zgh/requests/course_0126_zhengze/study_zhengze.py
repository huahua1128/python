import json
import  re    # 相当于正则的在线编辑器

# admin_user = '15873171553'
# admin_pwd = '123456'

data = {"admin_user":'15873171553',"admin_pwd":"123456"}
s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'  # 字符串

p = "\$\{admin_user}"   # 让他知道$符号死一个字符，需要转义\\

# # 查找替换
# m = re.search(p,s)   # 这种和多个if去判断是一样的
# # print(m)

# 正则表达式
p1 = "\$\{(.*?)}"  # 括号是一个组,\$\开始，}结束，?至少找一个，若不加？找出来的是一个match='${admin_user}","pwd":"${admin_pwd}"}'
    # .任意字符   * 查找多次   ？至少找到一遍就停止

m = re.search(p1, s)  # serach找到一个就停止
print(m)  # 返回值是一个match 对象    # <_sre.SRE_Match object; span=(16, 29), match='${admin_user}'>

# g = m.group()  # 返回的是整个匹配的字符串
# print(g)     # ${admin_user}

g1 = m.group(1)   # 根据组（取第一个组的匹配字符串）
print(g1)    # admin_user

value = data[g1]
s = re.sub(p1, value, s, count = 1)     # 查找且替换，count = 0 默认替换全部({"mobilephone":"15873171553","pwd":"15873171553"})，1表示一次
# sub 默认查找全部 findall
print(s)

# l = re.findall(p1, s)
# print(l)   # ['admin_user', 'admin_pwd']