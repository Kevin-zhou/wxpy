#微信 聊天机器人 指定 群聊
# -*- coding: utf-8 -*-
from wxpy import *
bot = Bot()
company_group = bot.groups().search('群名称')[0]#指定群聊

tuling = Tuling(api_key='你的api_key')
# 使用小 i 机器人自动与指定好友聊天
@bot.register(company_group)
def reply_my_friend(msg):
    tuling.do_reply(msg)

# 进入 Python 命令行、让程序保持运行
embed()