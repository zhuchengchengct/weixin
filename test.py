# -*- coding:utf-8 -*-

shortnumber={}
def handle(content):
    try:
        while shortnumber.get(content):
            value = shortnumber.get(content)
            content = ('%s的短号是%s。' % (content, value))
            return content
        for key in shortnumber.keys():
            if shortnumber.get(key)==content:
                content=('%s是%s的短号。'%(content,key))
                return content
        return '请输入短号或人名'
    except:
        return '未找到!'

while 1:
    content=input()
    print(handle(content))
