#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import numpy as np
ans_list = []

while (True):
    n, m = map(int, input().split(' '))
    # 終了条件の時,答えを出力して終了
    if n == 0 and m == 0:
        for answer in ans_list:
            print(answer)
        break
    # 終了条件でないとき
    else:
        a_list = np.array(list(map(int, input().split(' '))))  # 薬
        w_list = list(map(int, input().split(' ')))  # 分銅

        ans = itertools.product([1, 0, -1], repeat=len(a_list))  # 分銅の重複組み合わせ
        patterns = np.array(list(ans))
        # print(patterns)
        # print(a_list)
        ans = None
        for pattern in patterns:
            for a in a_list:
                print(a)
                if a == sum(pattern * a_list):
                    ans = 0
                    break
                elif ans != 0:
                    for a in a_list:
                        for i in range(a+sum(w_list)+1):
                            if a-i == sum(pattern * a_list):
                                ans = i
                                break
                else:
                    ans = -1
        ans_list.append(ans)
