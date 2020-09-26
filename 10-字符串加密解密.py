# Python编程：对字符串加密的5种方式
from urllib.parse import quote, unquote

name = "王大锤"

# 1. url编码
# ---------------------------------------------------
# 编码
utf8_name = quote(name)  # utf-8
print(utf8_name)
# %E7%8E%8B%E5%A4%A7%E9%94%A4   长度是 9

gbk_name = quote(name, encoding="gbk")
print(gbk_name)
# %CD%F5%B4%F3%B4%B8    长度是 6

# 解码
print(unquote(utf8_name))
print(unquote(gbk_name, encoding="gbk"))
# 王大锤


# 2. Base64编码
# ---------------------------------------------------
# base64编码是将二进制字节流编码为可打印的64个字符
# 以6位分割 bit位都是0，base64约定以‘=’代替
# z -> b'eg=='

import base64

name = "王大锤"

# 编码： 字符串 -> 二进制 -> base64编码
b64_name = base64.b64encode(name.encode())
print(b64_name)
# b'546L5aSn6ZSk'

# 解码：base64编码 -> 二进制 -> 字符串
print(base64.b64decode(b64_name).decode())
# 王大锤


# 3. 字符串转换ascii
# ---------------------------------------------------
name = "王大锤"

# 编码
ascii_name = list(map(ord, name))
print(ascii_name)
# [29579, 22823, 38180]

# 解码
print("".join(map(chr, ascii_name)))
# 王大锤


# 4. md5不可逆
# ---------------------------------------------------
import hashlib

name = "王大锤"

# 编码
print(hashlib.md5(name.encode()).hexdigest())
# 59c22c7bb43b8561cfd3b52f507171cb


# 5. Unicode转中文
# ---------------------------------------------------
name = "王大锤"

# 编码
unicode_name = name.encode("unicode_escape")
utf8_name = name.encode("utf-8")
gbk_name = name.encode("gbk")
gbk2312_name = name.encode("gb2312")

print(unicode_name)
# b'\\u738b\\u5927\\u9524'

print(utf8_name)
# b'\xe7\x8e\x8b\xe5\xa4\xa7\xe9\x94\xa4'

print(gbk_name)
# b'\xcd\xf5\xb4\xf3\xb4\xb8'

print(gbk2312_name)
# b'\xcd\xf5\xb4\xf3\xb4\xb8'

# 解码

print(unicode_name.decode())
# \u738b\u5927\u9524

print(unicode_name.decode("unicode_escape"))
# 王大锤

print(utf8_name.decode())  # 默认utf-8
# 王大锤

print(gbk_name.decode("gbk"))
# 王大锤