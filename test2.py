# aa = input("请输入你的年龄：")
#
# if int(aa) >= 18:
#     print('请进')
# else:
#     print("未满18，禁止入内")


num = int(input("请输入一个数字"))
if num % 7 == 0 and num % 3 == 0:
    print('可以同时被3或7整除')