#首先，txt文件与json文件对于python的区别：

#关于dict的创建

#1  可以由dict（元组们），
tup1=(1,"a")
tup2=(2,"b")
tup3=(3,"c")    #这里单引号双引号后面都是单引号
t=(tup1,tup2,tup3)
print(type(t),t)#<class 'tuple'> ((1, 'a'), (2, 'b'), (3, 'c'))
print(dict(t))#{1: 'a', 2: 'b', 3: 'c'}

#2  或者dict（list(元组们））创建
lt=list(t)
print('lt：',lt)#lt： [(1, 'a'), (2, 'b'), (3, 'c')]
print(dict(lt)) #{1: 'a', 2: 'b', 3: 'c'}

#可以用zip合并创建
firstl=[4,5,6]
secondl=['e','f','g']
print(dict(zip(firstl,secondl)))    #{4: 'e', 5: 'f', 6: 'g'}

#直接用 key=value的方式创建字典的时候，key只能是字符串类型而且不要加''
#所以这个时候就不能直接把key弄成全部是数字的
# print(dict(1='a',2='b'))
# print(dict('1'='a','2'='b'))
print(dict(s1='a',s2='b'))

#删除：

print("delete part")
dict1={1: 'a', 2: 'b', 3: 'c',4:'d',5:'e'} #不用= 赋值，直接这样列写dic的时候key是数字 是ok的
#del
del dict1[1]
print(dict1)

#pop +default value
is_two=dict1.pop(2,'2222')  #{3: 'c', 4: 'd', 5: 'e'} b
print(dict1,is_two)

is_six=dict1.pop(6,'no 6 key')  #{3: 'c', 4: 'd', 5: 'e'} no 6 key
print(dict1,is_six)

key_value=dict1.popitem()   #删除的是最后一个k-v
print(key_value)    #是个元组(5, 'e')
print(dict1)    #{3: 'c', 4: 'd'}


#遍历
dict2={1: 'a', 2: 'b', 3: 'c',4:'d',5:'e'}
for k in  dict2.keys():
    print(k)
for v in dict2.values():
    print(v)
for each_k,each_v in dict2.items():
    print('key:{0},value:{1}'.format(each_k,each_v))

newdict={new_k:new_v for new_k,new_v in dict2.items() if int(new_k)%2==0 }
print(newdict)  #{2: 'b', 4: 'd'}

