# coding=utf-8
#微信 好友 性别 数据统计 (会报错)

from wxpy import *
bot = Bot()
bot = Bot(cache_path=True)
friends_stat = bot.friends().stats()
for sex, count in friends_stat["sex"].iteritems():
    # 1代表MALE, 2代表FEMALE
    if sex == 1:
        print("MALE %d" % count)
    elif sex == 2:
        print("FEMALE %d" % count)