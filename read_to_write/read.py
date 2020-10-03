#读取文件以及获取流

#三中分开的方式读取data.txt
file='data'
def readfile1():
    # first read
    f1 = open('data')
    # context1=f1.read()  #context1 is string type
    # print(type(context1),context1,'\n')

    context2 = f1.read().splitlines()  # 出现一个坑就是，用这一句的时候，必须注释掉'context1=f1.read() '，不然读进来的就是空，
    # #原因是：open.read结束以后得到的是一个string，然且失去了对打开文件的引用
    print(type(context2), len(context2), context2[0], '\n')  # context2 is list type

    f1.close()  # 不关闭会占用 内存

    # 用with打开可以自动close

#readlines
def readlines():
    file='data'
    with open(file) as f2:  #with可以不close
        for line in f2.readlines(): #readlines 本身就是一个list，但是每行都会引入一个'\n'， line的类型是str
            line=line.strip('\n')   #使用换行符去解决时，还是要记得赋值，直接进行line.strip是不起作用的
            print(type(line))


#readline
def readline():
    file='data'
    with open(file) as f3:
        line=f3.readline()  #line是str，而且会有一个'\n'
        # print(type(line))
        while line:
            print(line)
            line=f3.readline()




#不read
def getfileNoread():
    file=open('data')
    try:
        for line in file:
            do_something_line(line)#传入的line是有'\n'的
    finally:
        file.close()
def do_something_line(line):
    # while line:
    #     print(line)
    print(line)


def writefile():
    string="hi"
    write_file='write_something.txt'
    w=open(write_file,'w')  #这里加上了'w'就没有报错，如果是'a'，每次会叠加（没有自动\n），如果是w，那么每次都会去掉以前有的东西
    # 'w' 没有则创建，有则覆盖
    w.write(string)

def writelines():
    with open(file,'r') as f_read:
        lines=f_read.readlines()
    with open('write_something.txt','a') as f_write:
        f_write.writelines(lines)  #writelines是可以写list的

def writeline():
    with open(file,'r') as f_read:
        line=f_read.readline()
        while line:
            print(line)
            # line=line.strip('\n') #这里不要去掉'\n'，因为writelines是不会自己添加行于行之间的分隔符的
            with open('write_something.txt','a') as f_write:    #这得是'a'，如果是'w'那只会留下最后一行
                f_write.write(line)
            line=f_read.readline()


if __name__=='__main__':
    #readfile1()
    # readlines()
    #readline()
    # getfileNoread()
    # writefile()
    # writelines()
    writeline()





