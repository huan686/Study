# 函数
# # 求三角形面积
# def sjx_area(a,h):
#     '''
#     计算三角形面积
#     :param a: 三角形的底
#     :param h: 三角形的高
#     :return: 三角形的面积
#     '''
#     area = a * h /2
#     return area
#
# print(f"三角形的面积为：{sjx_area(3,4)}")



# # 计算传入字符串中元音字母的个数
# def yy(s):
#     '''
#     计算传入字符串中元音字母的个数
#     :param s: 传入的字符串
#     :return: 元音字母的个数
#     '''
#     total = 0
#     for c in s:
#         if c in "aeiouAEIOU":
#             total += 1
#     return total
#
# x = "dhiunioofanwqaiifdopDIWNIC"
# print(yy(x))



# # 计算传入的班级学生高考成绩列表中成绩的最高分、最低分、平均分（保留一位小数）
# def gk(scores_list):
#     '''
#     计算传入的班级学生高考成绩列表中成绩的最高分、最低分、平均分（保留一位小数）
#     :param scores_list: 高考成绩
#     :return: 最高分、最低分、平均分
#     '''
#     max_scores = max(scores_list)
#     min_scores = min(scores_list)
#     avg_scores = round(sum(scores_list)/len(scores_list),1)
#     return max_scores, min_scores, avg_scores
#
# x_list = [588,487,276,647,620,560,581,333]
# print(gk(x_list))


# 不定长参数（位置传递）：* args
# 不定长参数（关键字传递）：* kwargs
# 例如：def calc_data(*args,*kwargs):-------->calc_data(100,200,300,400,round=2,count=0)


# 匿名函数：lambda 参数列表 : 函数体
# 例如：add = lambda x,y : x+y


# 定义一个函数，用于传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单总金额
# 优惠券和积分抵扣需要商品总金额满5000才可使用，100积分抵扣1元（且抵扣金额不能超过商品总价，积分只能整百抵扣）

# def total_w(*args,coupon=0,points=0,fee=0.0):
#     '''
#     计算传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息订单总金额
#     :param args: 商品信息
#     :param coupon: 优惠券
#     :param points: 积分
#     :param fee: 运费
#     :return: 订单总金额
#     '''
#     total = 0
#     for goods in args:
#         s = goods[1]*goods[2]
#         total += s
#
#     if total >= 5000 and coupon <= total and points <= total*100:
#         total = total - coupon - points//100
#
#     total += fee
#
#     return total
#
# w = total_w(('大米',90,3),('茶叶',500,5),('猪肉',36,10),coupon=200,points=3000,fee=9.9)
# print(w)


# 函数递归：计算一个数的阶乘
# def jc (x):
#     '''
#     计算一个数的阶乘
#     :param x: 数
#     :return: 数的阶乘
#     '''
#     if x == 1:
#         return 1
#     else:
#         return x * jc(x - 1)
#
# print(jc(10))