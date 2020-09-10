import winreg

key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,"Software\\Vim")
print(type(key))
# #获取该键的所有键值，因为没有方法可以获取键值的个数，所以只能用这种方法进行遍历
# try:
#     i = 0
#     while 1:
#         #EnumValue方法用来枚举键值，EnumKey用来枚举子键
#         name, value, type = winreg.EnumValue(key, i)
#         i += 1
#         print(repr(name),i)
# except WindowsError:
#         print('error')

#如果知道键的名称，也可以直接取值
value, type = winreg.QueryValueEx(key, "Installer Language")
# xa,ya=winreg.QueryValue(key,'Menulcons')
print(repr(value),repr(type))
