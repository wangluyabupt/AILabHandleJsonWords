import os

def osMoudle():
    print(os.curdir)#. 相对路径
    # print(os.listdir(os.curdir))#['file2', 'nil.txt', 'tryOs.py', 'file1']

    # print(os.listdir(os.pardir))

    # for item in os.walk('.'):# 入参是dir。返回是一个 三元组：str：路径；list:目录名 列表；list 文件名列表
    #     print(item)
    ##demo：
    # ('.', ['file2', 'file1'], ['nil.txt', 'tryOs.py'])
    # ('./file2', [], [])
    # ('./file1', [], ['file2'])

def filePath():
    #绝对路径
    file='nil.txt'
    print(os.path.abspath(file))

    file2='zero'
    print(os.path.abspath(file2))


if __name__=='__main__':
    osMoudle()
    filePath()