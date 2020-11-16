#!/usr/bin/env python3
# -*- coding: utf-8 -*
# def search(array, n, m):
#     a = [[[0] * 3 for i in range(3)]
import numpy as np
ans_list = []
while (True):
    _w, _h = map(int, input().split(' '))
    # 終了条件の時,答えを出力して終了
    if _w == 0 and _h == 0:
        for answer in ans_list:
            print(answer)
        break
    # 終了条件でないとき
    else:
        nums = []
        nums.append([0] * (_w + 2))
        for i in range(_h):
            row = list(map(int, input().split(' ')))
            row.append(0)
            row.insert(0, 0)
            nums.append(row)
        nums.append([0] * (_w + 2))
        island_num = 1
        for n in range(1, _h+1):
            for m in range(1, _w+1):
                if nums[n][m] == 1:  # もしマップの現在地が1なら調査
                    a = []
                    for h in range(-1, 2):
                        for w in range(-1, 2):
                            a.append(nums[n+h][m+w])
                    # print(a)
                    if max(a) == 1:
                        nums[n][m] = island_num + 1
                        island_num = island_num + 1
                    else:
                        nums[n][m] = max(a)#0,1を除いた最小値で上書き
                
        print(np.array(nums))
        print(island_num - 1)
