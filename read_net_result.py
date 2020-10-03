# -*- coding: UTF8 -*-

# cPickle是python2系列用的，3系列已经不用了，直接用pickle就好了
import pickle
import sys
from importlib import reload

reload(sys)
save=open('savepkl.txt','w')
# 重点是rb和r的区别，rb是打开2进制文件，文本文件用r
f = open('/Users/wangluya/Downloads/down_from_devbox/202008221114_epoch1/prediction.pkl','rb')
data = pickle.load(f,encoding='bytes')
save.write(str(data))
print(data.size)
f.close()
save.close()