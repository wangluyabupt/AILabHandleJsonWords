# -*- coding: utf-8 -*-
import json
f=open("origindata","r")

# s=open('save_origin','w')
decodes=""
for line in f:
    decodes=json.loads(line)
    # print (decodes[u"class_id"])
    # print(type(decodes))
    decodes.pop('class_id')
    decodes.pop('create_time')
    # print(decodes)
    # s.write(str(decodes))



with open('save_origin', 'w') as ff:
    json.dump(decodes, f, ensure_ascii=False)
f.close()
ff.close()