import uuid
import binascii

def ec():
    return uuid.uuid4().bytes

def ef(array):
    hex_digits = binascii.hexlify(array).decode("utf-8")
    # 格式化为标准UUID格式
    s = f"{hex_digits[:8]}-{hex_digits[8:12]}-{hex_digits[12:16]}-{hex_digits[16:20]}-{hex_digits[20:]}"
    return s

def ep(prefix=None):
    rnds = ec()
    uuid_hex = ef(rnds)
    if prefix is not None:
        # 如果提供了前缀，调整UUID以包含前缀
        # 注意，为了保持总长度不变，需要从UUID中移除等量的字符
        return prefix + uuid_hex[4:]
    else:
        # 如果没有提供前缀，直接返回正常的UUID
        return uuid_hex

# # 使用示例
# print(ep('aaa2'))  # 输出一个以"aaa1"开头的UUID
# print(ep('aaa1'))  # 输出一个以"aaa1"开头的UUID
# print(ep())        # 输出一个正常的UUID
