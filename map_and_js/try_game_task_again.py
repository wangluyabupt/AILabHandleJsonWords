#.json与.txt的区别
#仅从解决问题的角度，没啥大区别，我把不带后缀默认为新建 txt的data/js和data/js_line文件全部加.json后缀，发现运行没问题

#从data/js中取字段，尤其是vid，我我好像get到一点，就是想存成双引号ok，但是要
# 取json->转dic去字段->转json存

#基于txt
import json


def JDJ():
    origin_json_file=open('origindata_like_map')
    json_save_file=open('save_json_after_pop','a')
    try:
        for line in  origin_json_file:
            #读文件 获取Json->Dict
            # print(type(line),line)#str  双引号
            print("Begin Loads")
            loads_line=json.loads(line)
            # print(type(loads_line),loads_line)#dic  单引号

            #Dict去除字段：
            pop_id=loads_line.pop('class_id','no_class_id')
            pop_time=loads_line.pop('create_time','no_creat_time')
            if pop_id!=None:
                print("pop err",pop_id)
            if pop_time!=None:
                print("pop err",pop_time)
            print('After pop dict')
            print(type(loads_line),loads_line)#dic  单引号

            #Dict->Json 存文件
            back_line=json.dumps(loads_line,ensure_ascii=False)
            json_save_file.write(back_line+'\n')
            #ok,现在 存储到save_json_after_pop文件中的确实是双引号，但是里面的汉字不是，并不符合预期

            #如果直接是个dict：
            dict2={'gid': 6795483011585559815, 'vid': 'v0200f280000bp76fikpg6208pt0tg7g', 'title': '梦幻 婚礼 换装 看 视频 解锁 看 视频 解锁 看 视频 解锁 看 视频 解锁 看 视频 解锁 视频 加载 失败 请 检查 网络 或 重试 看 视频 解锁 看 视频 解锁'}
            back_line2=json.dumps(dict2,ensure_ascii=False)
            json_save_file.write(back_line2+'\n')
            #ok,是双引号，但是也不行，也是编码,加上了那句ensure_ascii=False，就完美解决了！！！
            #原因是中文不在ascll码里面，所以要取消dumps的默认编码


    finally:
        origin_json_file.close()
        json_save_file.close()

#不用转成dict这么折腾：
# def JSJ():






if  __name__=='__main__':
    JDJ()
    # JSJ()





