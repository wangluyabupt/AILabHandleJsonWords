import getopt
import json
import sys

#python get_params.py -i ./origindata_like_map -o ./saved_data -p class_id,create_time

def main(argv):
    print("hello main")
    print(argv)
    inputfile = ''
    outputfile = ''
    params=''
    pop_params = []
    try:
        opts, args = getopt.getopt(argv, "hi:o:p:", ["ifile=", "ofile=", "params="])
        # :和= 表示该选项必须有附加的参数（-i -o --ifile --ofile)，不带符号则表示该选项不附加参数（h)。
        #大姐，注意一下，短参数是只有一个字母哈
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile> -params<pop_params>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-p", "--params"):
            # pop_params=arg.split[',']
            print("arg--params:",arg,type(arg))
            params=arg

    print('输入的文件为：', inputfile)
    print('输出的文件为：', outputfile)
    pop_params=params.split(',')
    print('要删除的字段为：', pop_params,type(pop_params))
    JDJ(inputfile,outputfile,pop_params)


def JDJ(inputfile, outputfile, pop_params):
    print(type(pop_params),pop_params)
    origin_json_file = open(inputfile)
    json_save_file = open(outputfile, 'a')
    try:
        for line in origin_json_file:
            # 读文件 获取Json->Dict
            # print(type(line),line)#str  双引号
            print("Begin Loads")
            loads_line = json.loads(line)
            # print(type(loads_line),loads_line)#dic  单引号

            # Dict去除字段：
            for pop_param in pop_params:
                pop_id = loads_line.pop(pop_param, pop_param)
                if pop_id != None:
                    print("pop err", 'have_no_word_:{}_to_pop'.format(pop_id))

            print('After pop dict')
            print(type(loads_line), loads_line)  # dic  单引号

            # Dict->Json 存文件
            back_line = json.dumps(loads_line, ensure_ascii=False)
            json_save_file.write(back_line + '\n')

    finally:
        origin_json_file.close()
        json_save_file.close()


if __name__ == '__main__':
    # print(len(sys.argv))
    # print('参数列表:',sys.argv)
    # #参数列表: ['get_params.py', '-i', 'inputfile', '-o']#这里只会列出被空格间断的参数

    main(sys.argv[1:])


