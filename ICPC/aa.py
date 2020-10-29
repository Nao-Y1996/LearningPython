#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
        p = []
        for i in range(m):
            p.append(list(map(int, input().split(' '))))
        print(p)
        s = 0
        old_s = 0
        a = []
        for i in range(m):
            for j in range(n):
                s += p[i][j]
        a.append(s)
        print(max(a))
