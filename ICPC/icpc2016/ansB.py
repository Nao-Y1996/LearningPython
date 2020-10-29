#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ans_list = []
while (True):
    n = int(input())
    # 終了条件の時,答えを出力して終了
    if n == 0:
        for answer in ans_list:
            print(answer)
        break
    # 終了条件でないとき
    else:
        vote_list = list(input().split(' '))
        name_set = set(vote_list)
        point = [0] * len(list(name_set))
        ans, flag, index = 0, 0, 0

        for i in range(len(vote_list)):
            for name in name_set:
                if vote_list[i] == name:
                    point[list(name_set).index(name)] += 1
                    ranking = sorted(point, reverse=True)
                    print(f'{ranking}:残り{len(vote_list) - (i+1)} : {i+1}番目')
                    if ranking[0] > ranking[1] + (len(vote_list) - (i+1)) and flag == 0:
                        ans = i+1
                        flag = 1
                        index = point.index(ranking[0])
        ans_list.append((list(name_set)[index], ans))
