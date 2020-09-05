# coding:utf-8
import psutil


# pl = psutil.pids()
# for pid in pl:
#     if psutil.Process(pid).name() == 'notepad++.exe':
#         print(pid)

#判断进程是否存在
def checkprocess(processname):
    pl = psutil.pids()
    for pid in pl:
        if psutil.Process(pid).name() == processname:
            return pid


# print(isinstance(checkprocess("notepad++.exe"),int))

if isinstance(checkprocess("ccSvcHst.exe"), int):
    print("进程存在")
else:
    print("进程不存在")
