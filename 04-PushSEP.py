# coding:utf-8
import psutil


# 判断进程是否存在
def checkprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            return pid


if isinstance(checkprocess("ccSvcHst.exe"), int):
    print("进程存在")
else:
    print("进程不存在")

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

if routingGateway == '10.219.82.1':
    exefile1 = r'\\10.219.80.250\Sharing\a.exe'
    exefile2 = r'\\10.219.80.250\Sharing\b.exe'
    exefile3 = r'\\10.219.80.250\Sharing\c.exe'
    # 判断SEP进程存在与否，执行不同的exe
    if isinstance(checkprocess("ccSvcHst.exe"), int):
        done = os.system(exefile1)          #执行a.exe并将是否成功执行的返回值赋值给变量done
        if done == 0:
            print('a.exe执行成功！')
        else:
            done = os.system(exefile3)      #执行c.exe并将是否成功执行的返回值赋值给变量done
            if done == 0:
                print('c.exe执行成功！')
            else:
                print('c.exe执行失败')
    else:
        done = os.system(exefile2)          #执行b.exe并将是否成功执行的返回值赋值给变量done
        if done ==0:
            print('b.exe执行成功！')
        else:
            print('b.exe执行失败！')

