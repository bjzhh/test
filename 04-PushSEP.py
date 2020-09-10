# coding:utf-8
# 获取电脑用户名和计算机名
import socket
import getpass

user_name = getpass.getuser()  # 获取当前用户名
hostname = socket.gethostname()  # 获取当前主机名


# 判断进程是否存在
import psutil

def checkprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            return pid


if isinstance(checkprocess("ccSvcHst.exe"), int):
    print("进程存在")
    prog = True
else:
    print("进程不存在")
    prog = False

print('进程的值是：', isinstance(checkprocess("ccSvcHst.exe"), int))

# 获取网关
import os
import sys

try:
    import netifaces
except ImportError:
    try:
        command_to_execute = "pip install netifaces || easy_install netifaces"
        os.system(command_to_execute)
    except OSError:
        print("Can NOT install netifaces, Aborted!")
        sys.exit(1)
    import netifaces

routingGateway = netifaces.gateways()['default'][netifaces.AF_INET][0]
print(routingGateway)

#打开日志文件准备记录执行结果
f = open(r'\\10.219.80.250\Sharing\Log\\' + hostname + r'.txt', mode='w', encoding='utf-8')
f.write(user_name + '\n')
f.write(hostname + '\n')

if routingGateway == '10.219.82.1':
    exefile1 = r'\\10.219.80.250\Sharing\a.exe'
    exefile2 = r'\\10.219.80.250\Sharing\b.exe'
    exefile3 = r'\\10.219.80.250\Sharing\c.exe'
    # 判断SEP进程存在与否，执行不同的exe
    if prog:
        done = os.system(exefile1)  # 执行a.exe并将是否成功执行的返回值赋值给变量done
        if done == 0:
            f.write('a.exe执行成功！')
        else:
            done = os.system(exefile3)  # 执行c.exe并将是否成功执行的返回值赋值给变量done
            if done == 0:
                f.write('c.exe执行成功！')
            else:
                f.write('c.exe执行失败')
    else:
        done = os.system(exefile2)  # 执行b.exe并将是否成功执行的返回值赋值给变量done
        if done == 0:
            f.write('b.exe执行成功！')
        else:
            f.write('b.exe执行失败！')

f.close()