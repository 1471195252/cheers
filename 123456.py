'''
enumerate()
    用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
count()
    用于统计字符串里某个字符或子字符串出现的次数
str()
    将对象转化为适于人阅读的形式
with 变量 as F
    变量赋值给F
range()
    创建一个列表
len()
    返回对象（字符、列表、元组等）长度或项目个数
split()
    通过指定分隔符对字符串进行切片
append()
    用于在列表末尾添加新的对象
'''

import time
while True:
    a = []
    with open(r'baidu_x_system.log') as f1:
        hang = f1.readlines()
    for i in range(0, len(hang)):
        hang[i] = str(i + 1) + ' ' + hang[i]
        b = hang[i].split(" ")
        c = b[1]
        a.append(c)
    for index,value in enumerate(a):
        if value in a[:index]:#切片 如果value在从零角标开始到现在这个值-1出现过，直接跳过这一轮
            continue
        print(value,"出现了",a.count(value),"次！")
    time.sleep(60)