import json

fff=open('test.json','r')
for line in fff:
    print(type(line))
    print(line)
    decodes=json.loads(line)
    print(decodes)
    print(type(decodes))