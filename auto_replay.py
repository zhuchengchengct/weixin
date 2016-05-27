# 自动回复消息，消息处理过程在auto_replay中，使用方法：
# 1.import auto_replay
# 2.调用auto_replay.handle()处理微信端发来的消息
# 3.content=auto_replay.handle(content)


def handle(content):
    if content=='test':
        return 'content is test!'
    else:
        return 'error!'