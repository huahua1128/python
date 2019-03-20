# -*- coding: utf-8 -*-
# @Time    : 2018/12/15 9:33
# @Author  : lemon_huahua
# @Email   : 204893985@qq.com
# @File    : class_1_模块的导入.py

#安装完了之后？？用！--怎么用？
#导入到当前模块文件中来

#import、import....as

#除了顶级目录，导入你要引用的文件时，需要一层一层的剥开
#import week_3.class_12_13.class_01_函数的调用
# import week_3.class_12_13.class_01_函数的调用 as hello
#调用eat 函数
# hello.eat('胡萝卜','老坛酸菜','螺蛳粉')
#什么时候适合用
#当你导入的文件路径超长的时候
#当你导入的模块名名字很长的时候

#from...import...  import可以具体到函数名以及类名，但是至少要到模块名
# from week_3.class_12_13.class_01_函数的调用 import eat#推荐使用
# eat('胡萝卜','老坛酸菜','螺蛳粉','铁板烧')

#from...import *
# from week_3.class_12_13.class_01_函数的调用 import *
# eat('娃哈哈','优乐美')
# student_info('444','七月','18')

#from...import...as
# from week_3.class_12_13.class_01_函数的调用 import student_info as AI
# AI('444','七月','18')
