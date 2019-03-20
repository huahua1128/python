#enconding: utf-8
#name:  huahua
class  MathMethod:
    '数学方法类'
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def  add(self):
        return  self.a+self.b

    def subb(self):
        return  self.a-self.b

    def a_b_s(self):
        return   abs(self.a-self.b)
