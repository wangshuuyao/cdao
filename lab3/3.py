import re


def is_valid_id_card(id_card):
    pattern = r'^[1-9]\d{5}(19|20)\d{2}(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])\d{3}([0-9]|X)$'

    # 使用正则表达式进行匹配
    if re.match(pattern, id_card):
        return True
    else:
        return False


# 测试函数
id_card = input()

if is_valid_id_card(id_card):
    print(f"{id_card} 是合法的身份证号")
else:
    print(f"{id_card} 不是合法的身份证号")
