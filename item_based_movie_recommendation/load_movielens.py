# !/usr/bin/env python2.7
# --*-- coding:utf-8 --*--
# Author: Mellon
# DateTime:2018/1/2


# 将训练集转化为字典  # 打开指定文件
def loadMovieLensToDict(filename = 'ratings.csv'):
    str1 = 'c://Users/mellon/Downloads/ml-latest-small/'
    # 添加字典集 Dictionary  dataSet
    dataSet = {}
    line_num = 0
    for line in open(str1 + filename, 'r'):   # 打开指定文件
        # 需要跳过第一行
        line_num += 1
        if (line_num != 1):
            # 数据集中每行有4项，分割符为逗号
            (userid, movieid, rating, ts) = line.split(',')
            # 给字典中不存在的键赋值为字典 # 设置字典的默认格式,元素是userid:{}字典
            dataSet.setdefault(userid, {})
            # 字典里面套字典形式
            dataSet[userid][movieid] = float(rating)
    return dataSet