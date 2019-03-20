# 解决用例之间的依赖，比如注册成功后的手机号用来登陆或者是充值
# 如何解决多个module，或者不同数据类之间的数据传递---》
# 同一个类或者module里面，不同的方法之间的数据的传递 ---》 同一个类，不同方法，使用self或者全局变量 或者global

# 反射
# 静态-运行前，如果要调用类的属性或者方法，需要实例化他的对象
# 动态-运行时，就获取类的属性或者方法，甚至更改他的属性或者方法

class Girls:

    single =  False # 类属性

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sing(self):
        print(self.name + '会唱歌')

if __name__ == '__main__':
    g = Girls('mongo', 18)
    # print(g.name)
    # g.sing()
    # # print(g.hub)  # 在设置之前是没有这个属性的
    #
    # # 给类或者实例对象动态的添加属性或者方法
    # setattr(g, 'hub', 'swimming')   # 给类或者实例对象动态的添加属性或者方法（对象属性），swimming是添加的对象属性，只有g这个属性才有
    # print(g.hub)   # 设置了之后这个 g 实例才有这个属性
    # # print(Girls.hub)   # swimming是添加的对象属性，只有g这个属性才有
    # # print(Girls('mongo', 20).hub)    # swimming是添加的对象属性，只有g这个属性才有
    #
    # setattr(Girls, 'hub', 'swimming')  # 类属性（给类添加），swimming是添加的类属性，所有的对象都有这个属性
    # # print(g.hub)  # 类属性可以用对象调用
    # # print(Girls.hub)    # 类属性可以用类调用
    #
    # # 获取类或者对象的属性值
    # print(getattr(Girls, 'hub'))   # 不实例化，直接取类的属性
    # # print(getattr(Girls, 'male'))   # 获取的属性不存在时，AttributeError: type object 'Girls' has no attribute 'male'
    # print(getattr(g,'hub'))
    #
    # # 判断类或者对象是否有这个属性值  有--True   没有---False
    # print(hasattr(Girls, 'male'))  # 返回的是布尔值
    # print(hasattr(g, 'name'))   # 判断对象是否有这个属性
    # print(hasattr(Girls, 'name'))    # name在初始化函数里，实例化的时候才会有对应的属性，但这里并没有实例化，所以没有
    # print(hasattr(Girls, 'single'))
    #
    # # 删除类或者对象的属性值
    # print(delattr(g, 'name'))   # 删除对象属性    ---->None
    # # print(getattr(g, 'name'))  # 看是否删除了该对象属性  ---->AttributeError: 'Girls' object has no attribute 'name'
    # delattr(Girls, 'single')  # 删除类属性
    # print(hasattr(Girls, 'single'))   # 判断是否删除了该类属性  --->False

    ## 动态的添加方法  (不会)
    # def dance(self):
    #     #     print(self.name + '会跳舞')
    #     #
    #     # setattr(Girls, dance, )
    #     # print(g.dance)
