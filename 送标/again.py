# -*- coding:utf-8 -*-
import json

data = {}  # 定义一个空字典
filename = 'test.json'  # 写入的文件名
# for n in range(3):
#     key = input('please input key:')
#     value = input('please input value:')
#     data[key] = value  # 将输入的值存储为字典
f=open("origindata","r")
ff=open(filename, 'w')
# s=open('save_origin','w')
for line in f:
    decodes=json.loads(line)
    # print (decodes[u"class_id"])
    decodes.pop('class_id')
    decodes.pop('create_time')
    # with open(filename, 'w') as ff:
    #     json.dump(decodes, ff, ensure_ascii=False)  # 或者[data],list格式也OK
    #     # ensure_ascii为True的时候，所有非ASCII码字符显示为\uXXXX序列
    #     # 所以将其设置为False即可，此时存入json的中文可正常显示

    ff.write(json.dumps(decodes, ensure_ascii=False)+'\n')


# fff=open('test.json','r')
# for line in fff:
#     decodes=json.loads(line)
#     print(decodes)
#     print(type(decodes))