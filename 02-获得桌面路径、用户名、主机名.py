#! /usr/bin/python
# -*- coding: utf-8 -*-

import os

# print(os.environ['HOME'])
# print(os.path.expandvars('$HOME'))
print(os.path.expanduser('~'))

def get_desk_p():
    return os.path.join(os.path.expanduser('~'),"Desktop")

print('你的桌面路径是：',get_desk_p())



import socket
import getpass

user_name = getpass.getuser() # 获取当前用户名
hostname = socket.gethostname() # 获取当前主机名

print(type(user_name))

print('C:\\Users\\' + user_name + '\\AppData\Local\Temp\\')

print(hostname)
print(user_name)