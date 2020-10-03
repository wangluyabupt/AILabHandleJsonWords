#-*-coding:utf-8 -*-
import json


f=open("origindata","r")

s=open('save_origin.json','w')

for line in f:
    # print(line)

    # decodes=json.loads(line)
    decodes=eval(line)
    print(type(decodes))
    print(decodes)




    # print (decodes[u"class_id"])
    # print(type(decodes))
    decodes.pop("class_id")
    decodes.pop("create_time")
    # print(decodes)

    decodes=json.dumps(decodes)

    print(type(decodes))
    # decodes.decode('utf-8')
    print("json.dumps():",decodes)

    s.write(decodes+'\n')
f.close()
s.close()