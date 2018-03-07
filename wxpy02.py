# coding=utf-8
#微信群 找老板 消息
from wxpy import *

bot = Bot(cache_path=True)

# 定位公司群
company_group = bot.groups().search('群名称')[0]

# 定位老板

boss = company_group.search('老板名称')[0]#备注名称

# 将老板的消息转发到文件传输助手
@bot.register(company_group)
def forward_boss_message(msg):
    if msg.member == boss:
        msg.forward(bot.file_helper, prefix='老板发言:')

# 堵塞线程
embed()