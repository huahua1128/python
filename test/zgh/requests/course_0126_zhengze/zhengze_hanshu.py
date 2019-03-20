# s是目标字符串，d是替换的内容
# 找到目标字符串里面的标识符key，去d里面拿到值去替换
# 替换到s里面去，再返回
import re

def replace(s,d):
    p = "\$\{(.*?)}"
    while re.search(p,s):
        m = re.search(p,s)
        key = m.group(1)
        value = d[key]
        s = re.sub(p, value, s, count = 1)
    return  s


if __name__ == '__main__':
    s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'  # 字符串
    data = {"admin_user": '15873171553', "admin_pwd": "123456"}
    s = replace(s,data)
    print(s)