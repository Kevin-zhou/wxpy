# coding=utf-8
# 找出 特定的朋友 发消息  并 自动回复  及加好友自动同意
from wxpy import *
bot = Bot()
bot = Bot(cache_path=True)
# 搜索名称含有 "游否" 的男性深圳好友
my_friend = bot.friends().search('好友昵称', sex=MALE, city="城市")[0]
# 发送文本给好友
my_friend.send('想搞事情吗')
# 发送图片
my_friend.send_image('01.jpg')
# 打印来自其他好友、群聊和公众号的消息
@bot.register()
def print_others(msg):
    print(msg)

# 回复 my_friend 的消息 (优先匹配后注册的函数!)
@bot.register(my_friend)
def reply_my_friend(msg):
    # return '自动回复: {} ({})'.format(msg.text, msg.type)
    my_friend.send_image('01.jpg')
    return  '搞事情搞事情'

# 自动接受新的好友请求
@bot.register(msg_types=FRIENDS)
def auto_accept_friends(msg):
    # 接受好友请求
    new_friend = msg.card.accept()
    # 向新的好友发送消息
    new_friend.send('哈哈，我自动接受了你的好友请求')

# 进入 Python 命令行、让程序保持运行
embed()

# 或者仅仅堵塞线程
# bot.join()