# 构成json文档的两种结构为：对象object和数组array
# json对象是无序集合    "名称：值"对集合。  {"string":json1,"string2":json2,"string3":json3}
# json数组是值的有序集合    一连串元素的集合    【"text","html","css"]

# python数据进行网络传输可以转换为json数据，对应关系：
# map    object
# list tuple     array
# encoding

# stering    strting
# int float ...  数字
# True False None    true false null


# encoding to json
# json.dump()是与json.load()搭配用来读写json文件的
# json.dumps()是与json.loads()搭配用来进行json格式处理的
import json


#编码，也就是往文件写入json，dump、dumps
def handleJsonEncode():
    dict1 = {'name': 'tony', 'age': 30, 'sex': True}
    list1 = [1, 3]
    tuple = ('A', 'B', 'C')
    dict1['list'] = list1
    dict1['tuple'] = tuple
    print("merge dict1:", dict1, type(dict1))

    # json_obj = json.dumps(dict1)
    # print("json_obj:", json_obj)
    # with open('./data/js', 'a') as f1:
    #     json.dump(dict1, f1)

    json_obj_format = json.dumps(dict1, indent=4)
    print("json_obj_format:", json_obj_format)
    with open('data/js_format.json', 'a')as f2:
        json.dump(dict1, f2, indent=4)


# 写进去的json或则print出的json都是双引号""

# coding=utf-8
# jsonn.loads()是处理字符串的
def handleJsonDecode():
    json2 = r'{"name": "tony", "age": 30, "sex": true, "list": [1, 3], "tuple": ["A", "B", "C"]}'
    # 上面那个true,开头不可以是大写,所以一开始要有r''
    print(type(json2), json2)  # str

    dict2 = json.loads(json2)

    print(type(dict2), dict2)  # dict
    print(dict2['name'])
    print(dict2['list'])
    list1 = dict2['list']  # 确实是列表形式
    print(list1[1])

    print("Test Open File To Read And Load")

    with open('data/js', 'r')as f1:
        #print("f1：",f1.read())
        #str
        # {"name": "tony", "age": 30, "sex": true, "list": [1, 3], "tuple": ["A", "B", "C"]}
        load_data = json.load(f1)   #执行这个要成功先把有f1.read()的那一行注释掉！！！
        print(type(load_data), load_data)
        #<class 'dict'> {'name': 'tony', 'age': 30, 'sex': True, 'list': [1, 3], 'tuple': ['A', 'B', 'C']}
        #发现没，成了单引号
    #这里，data/js文件如果是两行，就会出错


    with open('data/js_format.json', 'r') as f2:
        load_data2 = json.load(f2)
        print(type(load_data2), load_data2)
    #这里，data/js_format文件里也得是单个


def handleDecodeForLines():
    file=open('data/js_lines.json')
    try:
        for line in file:
            load_data=json.loads(line)
            print('load_data_line:',load_data,type(load_data))
            #load_data_line: {'name': 'tony', 'age': 30, 'sex': True, 'list': [1, 3], 'tuple': ['A', 'B', 'C']}
            # <class 'dict'>
            #这里，用json.load()就不对，得用json.loads()
    finally:
        file.close()





if __name__ == '__main__':
    handleJsonEncode()
    # handleJsonDecode()
    handleDecodeForLines()
