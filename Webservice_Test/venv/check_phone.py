#enconding: utf-8
#name:  huahua

# 判断是否为正确的手机号

def check_phone(str):
    if len(str) != 11:
        return False
    elif str[0:2] != "13":
        return False
    elif str[2] < "0" or str[2] > "9":
        return False
    for i in range(3,11):
        if str[i] < "0" or str[i] > "9":
            return False
    return True

if __name__ == '__main__':
    print(check_phone(str(13109090902)))