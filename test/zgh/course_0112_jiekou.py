import json  # 导入json模块  处理字典和json之间的转换

# python中的字典  单双引号都可以

# python--->None
# json----->null

d_1={'status':1, 'code':"10001", "data":None, "msg":"登陆成功"}
print(type(json.dumps(d_1)))
print(json.dumps(d_1))

# 数据格式json
d_2 = '''{"status":1, "code":"10001", "data":null, "msg":"登陆成功"}'''
d_2 = '{"status":1, "code":"10001", "data":null, "msg":"登陆成功"}'
# print(type(json.loads(d_2)))
# print(json.loads(d_2))

# print(type(d_1))
# print(d_1)
# print(type(d_2))
# print(d_2)