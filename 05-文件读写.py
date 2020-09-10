import socket
import getpass

user_name = getpass.getuser()  # 获取当前用户名
hostname = socket.gethostname()  # 获取当前主机名
f = open(r'\\10.219.80.250\Sharing\Log\\' + hostname + r'.txt', mode='w', encoding='utf-8')
f.write(user_name + '\n')
f.write(hostname + '\n')
f.close()
