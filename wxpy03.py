# coding=utf-8
#微信 好友 地区数据统计 (会报错)

from wxpy import *
bot = Bot()
bot = Bot(cache_path=True)
friends_stat = bot.friends().stats()

friend_loc = [] # 每一个元素是一个二元列表，分别存储地区和人数信息
for province, count in friends_stat["province"].iteritems():
    if province != "":
        friend_loc.append([province, count])

# 对人数倒序排序
friend_loc.sort(key=lambda x: x[1], reverse=True)

# 打印人数最多的10个地区
for item in friend_loc[:10]:
    print(item[0], item[1])