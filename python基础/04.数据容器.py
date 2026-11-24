# 列表：list[]       切片：list[开始索引:结束索引:步长]
# 列表推导式：快速生成一个列表       格式：list[ s(要插入的值) for i in 序列 if 条件 ]

# 字符串str()

# 元组tuple()
# 组包：t1 = (5,7,9,1)              解包：5,7,9,1 = t1         x,*y,z = t1 # x为5，y为[7,9]，z为1    *表示收集剩余所有元素

# 集合set{}      空集合set()         集合操作运算符：&：交集    | ：并集   - ：差集
# 集合推导式：set = {s表达式 for i in 列表 if 条件}

# 字典dict{}     dict{ key : value }


# # 案例1
# data = (
#     ("S001","王林",85,92,78),
#     ("S002","李慕婉",92,88,95),
#     ("S003","十三",78,85,82),
#     ("S004","曾牛",88,79,91),
#     ("S005","周铁",95,96,89),
#     ("S006","王卓",76,82,77),
#     ("S007","红蝶",89,91,94),
#     ("S008","徐立国",75,69,82),
#     ("S009","许木",86,89,98),
#     ("S010","遁天",66,59,72)
# )
#
# print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
# for s in data:
#     total = s[2] + s[3] + s[4]
#     avg = total/3
#     print(f"{s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {total} \t {avg:.2f}")
#
# chinese_scores = [s[2] for s in data]
# math_scores = [s[3] for s in data]
# english_scores = [s[4] for s in data]
# print()
#
# print("最高分\t最低分\t\t平均分")
# print(f"{min(chinese_scores)} \t\t {max(chinese_scores)} \t\t {sum(chinese_scores)/len(chinese_scores)}")
# print(f"{min(math_scores)} \t\t {max(math_scores)} \t\t {sum(math_scores)/len(math_scores)}")
# print(f"{min(english_scores)} \t\t {max(english_scores)} \t\t {sum(english_scores)/len(english_scores)}")
# print()
#
# print("优秀学生名单：")
# for s in data:
#     total = s[2] + s[3] + s[4]
#     avg = total/3
#     if avg > 90:
#         print(f"学号：{s[0]}  姓名：{s[1]}  平均分：{avg:.2f}")
#


# 案例2：购物车管理系统
# print("欢迎使用购物车管理系统！")
# print('''
# ########## 购物车系统 ##########
# #        1.添加购物车          #
# #        2.修改购物车          #
# #        3.删除购物车          #
# #        4.查询购物车          #
# #        5.退出购物车          #
# ##############################
# ''')
#
# shopping_cars = {}
#
# while True:
#     choice = int(input("请选择要执行的操作："))
#     match choice:
#         case 1:
#             name = input("请输入要添加的商品：")
#             if name in shopping_cars:
#                 print("该商品已存在")
#                 continue
#             price = float(input("请输入商品价格："))
#             num = int(input("请输入商品数量："))
#             shopping_cars[name] = {"price": price, "num": num}
#         case 2:
#             name = input("请输入要修改的商品：")
#             if name not in shopping_cars:
#                 print("该商品已不存在")
#                 continue
#             price = float(input("请输入要修改商品价格："))
#             num = int(input("请输入要修改商品数量："))
#             shopping_cars[name] = {"price": price, "num": num}
#         case 3:
#             name = input("请输入要删除的商品：")
#             if name not in shopping_cars:
#                 print("该商品已不存在")
#                 continue
#             del shopping_cars[name]
#         case 4:
#             for name in shopping_cars.keys():
#                 info = shopping_cars[name]
#                 print(f"商品名称：{name} 商品价格：{info["price"]} 商品数量：{info["num"]}")
#         case 5:
#             print("Byebye!")
#             break
#         case _:
#             print("输入错误！！！请重新输入！")