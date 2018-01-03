# !/usr/bin/env python2.7
# --*-- coding:utf-8 --*--
# Author: Mellon
# DateTime:2018/1/3


from math import sqrt


def sim_adcos(prefer, person1, person2):
    sim = {}

    for item in prefer[person1]:
        if item in prefer[person2]:
            sim[item] = 1

    if len(sim) == 0:
        return 0.3
    sum1 = sum([prefer[person1][item] for item in prefer[person1]])
    sum2 = sum([prefer[person2][item] for item in prefer[person2]])
    n1 = len(prefer[person1])
    n2 = len(prefer[person2])
    avg1 = sum1/n1
    avg2 = sum2/n2
    summulti = sum([(prefer[person1][item] - avg1) * (prefer[person2][item] - avg2) for item in sim])
    sq1 = sqrt(sum([pow((prefer[person1][item] - avg1),2) for item in prefer[person1]]))
    sq2 = sqrt(sum([pow((prefer[person2][item] - avg2),2) for item in prefer[person2]]))
    sq = sq1 * sq2
    if sq == 0:
        return 0.3
    result = summulti/sq
    return result


def sim_person(prefer, person1, person2):
    sim = {}
