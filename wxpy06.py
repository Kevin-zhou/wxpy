#微信 聊天机器人  专对某一个人  与5  相同
# -*- coding: utf-8 -*-
from wxpy import *
bot = Bot()
my_friend = ensure_one(bot.search('好友昵称'))
tuling = Tuling(api_key='你的api_key')
# 使用小 i 机器人自动与指定好友聊天
@bot.register(my_friend)
def reply_my_friend(msg):
    tuling.do_reply(msg)

# 进入 Python 命令行、让程序保持运行
embed()