# !/usr/bin/env python2.7
# --*-- coding:utf-8 --*--
# Author: Mellon
# DateTime:2018/1/3


from math import sqrt


##--------------以下使用欧几里得 计算用户之间的相似度--------------------##

def sim_adcos(prefer, person1, person2):
    '''
         define function: 定义函数
         :sim_adcos: 函数名
         :prefer: 
         :person1: 
         :person2: 
         :for...: 查找共同项 
         :sim: dictionary 存储字典形式
         '''
    sim = {}
    for item in prefer[person1]:
        if item in prefer[person2]:
            # 添加共同项到字典中
            sim[item] = 1

    # 无共同项，返回0
    if len(sim) == 0:
        return 0.3


    # 计算共有项目之和
    sum1 = sum([prefer[person1][item] for item in prefer[person1]])
    sum2 = sum([prefer[person2][item] for item in prefer[person2]])

    n1 = len(prefer[person1])
    n2 = len(prefer[person2])

    # 平均值
    avg1 = sum1/n1
    avg2 = sum2/n2

    # 计算所有共有项目的差值的平方和
    summulti = sum([(prefer[person1][item] - avg1) * (prefer[person2][item] - avg2) for item in sim])

    sq1 = sqrt(sum([pow((prefer[person1][item] - avg1),2) for item in prefer[person1]]))
    sq2 = sqrt(sum([pow((prefer[person2][item] - avg2),2) for item in prefer[person2]]))
    sq = sq1 * sq2

    if sq == 0:
        return 0.3

    # 返回改进的相似度函数
    result = summulti / sq
    return result


##-----------------------pearson相关度系数------------------------##

def sim_person(prefer, person1, person2):
    '''
         define function: 定义函数
         :sim_person: 函数名
         :prefer: 
         :person1: 
         :person2: 
         :for...: 查找共同项 
         :sim: dictionary 存储字典形式
         '''
    sim = {}
    # 查找双方都评价过的项,并将相同的项添加到字典sim中
    for item in prefer[person1]:
        if item in prefer[person2]:
            sim[item] = 1

    # 无共同项，返回0
    if len(sim) == 0:
        return 0.3

    # 所有偏好之和
    sum1 = sum([prefer[person1][item] for item in prefer[person1]])
    sum2 = sum([prefer[person2][item] for item in prefer[person2]])

    n1 = len(prefer[person1])
    n2 = len(prefer[person2])

    avg1=sum1/n1
    avg2=sum2/n2

    # 求乘积之和 ∑XY
    summulti = sum([(prefer[person1][item] - avg1) * (prefer[person2][item] - avg2) for item in sim])

    # 求平方和
    sq1 = sqrt(sum([pow((prefer[person1][item] - avg1),2) for item in sim]))
    sq2 = sqrt(sum([pow((prefer[person2][item] - avg2),2) for item in sim]))

    sq = sq1 * sq2

    if sq == 0:
        return 0.3
    result = summulti/sq
    return result

##-----------------------Cosine Similarity 余弦相似度 计算用户之间的相似度------------------------##
def sim_cos(prefer, person1, person2):
    '''
         define function: 定义函数
         :sim_cos: 函数名
         :prefer: 
         :person1: 
         :person2: 
         :for...: 查找共同项 
         :sim: dictionary 字典形式存储
         '''
    sim = {}
    # 查找双方都评价过的项,并将相同的项添加到字典sim中
    for item in prefer[person1]:
        if item in prefer[person2]:
            sim[item] = 1

    # 无共同项，返回0
    if len(sim) == 0:
        return 0.3

    summulti = sum( [ ( prefer[person1][item] * prefer[person2][item] ) for item in sim ] )
    sq1 = sqrt( sum( [ pow(prefer[person1][item], 2) for item in sim] ) )
    sq2 = sqrt( sum( [ pow(prefer[person2][item], 2) for item in sim] ) )
    sq = sq1 * sq2
    if sq == 0:
        return 0.3
    result = summulti/sq
    return result

