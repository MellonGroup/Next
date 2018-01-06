# !/usr/bin/env python2.7
# --*-- coding:utf-8 --*--
# Author: Mellon
# DateTime:2018/1/4


from load_movielens import loadMovieLensToDict
from user_based_similarity_function import sim_adcos
from user_based_similarity_function import sim_person
from user_based_similarity_function import sim_cos

import time

start_time = time.time()


def topkMatches(trainSet, presenUserid, persenItemid, sim, k = 30):
    '''
        define function: 定义函数
        :topkMatches: 函数含义是什么？
        :trainSet: 
        :presenUserid: 
        :persenItemid: 
        :sim:
        :k:
        '''
    # userSet 表示评价过当前商品的所有用户
    userSet = []


    for user in trainSet:
        if presenUserid in trainSet[user]:
            userSet.append(user)
    scores = [(sim(trainSet, presenUserid, other),other) for other in userSet if other!= presenUserid]
    scores.sort()
    scores.reverse()
    # neighborSimAndUser最近邻居用户。
    if len(scores) <= k:
        neighborSimAndUser = scores
        return neighborSimAndUser
    else:
        kscore = scores[0:k]
        neighborSimAndUser = kscore
        return neighborSimAndUser


def getUserAverage(trainSet, userid):
    '''
           define function: 定义函数
           :getUserAverage: 函数含义是什么？
           :trainSet: 
           :userid: 
           '''
    count = 0
    sum = 0
    for item in trainSet[userid]:
        sum = sum + trainSet[userid][item]
        count = count + 1
    return sum/count


def getRating(trainSet, presentUserid, presentItemid, sim):
    '''
              define function: 定义函数
              :getUserAverage: 函数含义是什么？
              :trainSet: 
              :userid: 
              '''
    # 存放所有用户对这个项目的评分。
    all_scores_for_item = []

    for (user, items) in trainSet.items():
        if presentItemid in items:
            all_scores_for_item.append(trainSet[user][presentItemid])

    # 如果当前用户是新用户，当前商品又是新项目，则返回默认评分3.
    if presentUserid not in trainSet:
        if len(all_scores_for_item) == 0:
            return 3

        # 如果当前用户是新用户，但当前商品不是新项目，则返回当前商品的平均评分。
        else:
            return sum(all_scores_for_item) / len(all_scores_for_item)
    # 如果当前用户不是新用户，但当前商品是新项目。则返回当前用户的平均评分
    else:
        if len(all_scores_for_item) == 0:
            return getUserAverage(trainSet, presentUserid)
        else:
            neighborSimAndUsers = topkMatches(trainSet, presentUserid, presentItemid, sim)
            averageOfUser = getUserAverage(trainSet, presentUserid)
            s = 0
            simSum = 0
            for i in neighborSimAndUsers:
                averageOfneighborUser = getUserAverage(trainSet, i[1])
                s = s + abs(i[0]) * (trainSet[ i[1] ] [presentItemid] - averageOfneighborUser)
                simSum += abs(i[0])
            if simSum == 0:
                return averageOfUser

            return (averageOfUser + s/simSum)















