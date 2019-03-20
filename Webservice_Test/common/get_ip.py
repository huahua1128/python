#enconding: utf-8
#name:  huahua
import random
from common import context

def get_ip():
    a = str(random.randint(1,255))
    b = str(random.randint(1, 255))
    c = str(random.randint(1, 255))
    d = str(random.randint(1, 255))
    ip = a +'.' + b +'.'+ c +'.'+d
    setattr(context.Context, "ip", ip)
    return ip

if __name__ == '__main__':
    get_ip()
    print(getattr(context.Context,"ip"))