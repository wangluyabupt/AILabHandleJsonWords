import json
import os
import time

import xlwt

#
# def redis_nil():
#     f=open("0000",'r')
#     lines=f.readlines()
#     wf=open('00','w')
#     for line in lines:
#         # j=json.dumps(line)
#         # vid=json.load(line)
#         # print(vid["vid"])
#
#         l=line.split("\"vid\": \"")
#         for item in l[1:]:
#             try:
#                 vid = item.split('\"')[0]+'\n'
#                 # print(vid)
#                 wf.write(vid)
#
#             except:
#                 pass
#     f.close()
#     wf.close()


def zero():
    f=open('0000')

    #just one line
    line=f.readline()
    js_line=json.loads(line)
    print(js_line)
    #success





if __name__ == '__main__':
    # redis_nil()
    zero()
    #main