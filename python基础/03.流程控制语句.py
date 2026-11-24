# # if案例:三角形类型判断
# a = int(input("请输入第一条边:"))
# b = int(input("请输入第二条边:"))
# c = int(input("请输入第三条边:"))
#
# # 判断能否组成三角形
# if a + c > b and a + b > c and b + c > a:
#     if a == b == c:
#         print("这个三角形是等边三角形")
#     elif a == b or b == c or a == c:
#         print("这个三角形是等腰三角形")
#     else:
#         print("这个三角形是普通三角形")
# else:
#     print("输入错误!")
#


#
# # if案例2:居民年度用电电费计算
# total = int(input("请输入年度用电度数:"))
# if total <= 2880:
#     bush = total * 0.4883
# elif 2880 <= total <= 4800:
#     bush = total * 0.5383
# else :
#     bush = total *0.7883
# print(f"年度电费为:{bush}")


#
# # 模式匹配  match...case '':
# day = input("请输入星期几(1-7):")
# match day:                        # day 为要匹配的变量
#     case "1":                     # 可以在case "" 后加入 ' if + 条件 ' 代表条件,例:case '/' if b !=0 :
#         print("工作会议日")
#     case "2":
#         print("学习培训日")
#     case "3":
#         print("项目开发日")
#     case "4":
#         print("代码审查日")
#     case "5":
#         print("总结规划日")
#     case "6" | "7":              # |  表示 or
#         print("周末休息日")
#     case _:                      # 相当于 else
#         print("输入错误!")


#
# # while 循环: ' while 条件表达式 : '
# # 案例:计算1-100 之间偶数之和
# total = 0
# i = 1
# while i <=100:
#     if i % 2 ==0:
#         total += i
#     i += 1
# print(f"1-100之间所有偶数之和为:{total}")


# range(start,end,step)
# 生成从start到end步长为step的连续数字，包括start，不包括end


# # for循环：计算1-100之间所有奇数之和
# total = 0
# for i in range(1,101,2):
#    total += i
# print(total)
#

#
# # for 循环嵌套：打印长方形
# a = int(input("请输入长方形的长："))
# b = int(input("请输入长方形的宽："))
# for i in range(b):
#     for j in range(a):
#         print("*",end = " ")
#     print()
#



# # 打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j}",end = "\t")
#     print()


# # 打印数字金字塔
# a = int(input("请输入一个数字："))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(j,end = "\t")
#     print()
#


# # 打印国际象棋棋盘
# for i in range(8):
#     for j in range(8):
#         if (i+j)%2 == 0:
#             print("*",end=" ")
#         else:
#             print("#",end = " ")
#     print()


# 循环登录：admin/666888、zhangsan/123456、taoge/888666
#
# while True:
#     account = input("请输入用户名：")
#     password = input("请输入密码：")
#     if account == ""or password == "":
#         print("用户名或密码不能为空！请重新输入")
#         continue
#
#     if account == 'admin' and password == '666888':
#         print("登录成功！")
#         break
#     elif account == 'zhangsan' and password == '123456':
#         print("登录成功！")
#         break
#     elif account == 'taoge' and password == '888666':
#         print("登录成功！")
#         break
#     else:
#         print("用户名或密码输入错误！请重新数输入")
#

#
# # 猜数字游戏
# import random
# x = random.randint(1, 100)
# while True:
#     num = int(input("请输入猜的数字："))
#     if num < x:
#         print("猜小了")
#     elif num > x:
#         print("猜大了")
#     else:
#         print("恭喜你猜对了",x)
#         break