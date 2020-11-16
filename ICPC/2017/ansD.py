#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
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
        num_list = []
        for i in range(n):
            nums = list(map(int, input().split(' ')))
            num_list.append(nums)
        patterns = list(itertools.permutations(num_list))

        a = []
        b = 0
        for pattern in patterns:
            pattern_sum = 0
            for index, num in enumerate(pattern):
                pattern_sum += num[0]
                if all([int(x) % 2 == 0 for x in str(pattern_sum)]):
                    b = index+1
                a.append(b)
        ans_list.append(max(a))

# def a(arg):
#     return all([int(x) % 2 == 0 for x in str(arg)])
