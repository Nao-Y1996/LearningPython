#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ans_list = []
while (True):
    h, w = map(int, input().split(' '))
    # 終了条件の時,答えを出力して終了
    if h == 0 and w == 0:
        for answer in ans_list:
            print(answer)
        break
    # 終了条件でないとき
    else:
        keyboard = []
        str_list = None
        for i in range(h):
            keyboard.append(list(input()))
        str_list = list(input())
        cost = 0
        old_row_index, old_col_index = 0, 0
        for s in str_list:
            for index, row in enumerate(keyboard):
                try:
                    row_index, col_index = index, row.index(s)
                except:
                    pass
            cost += abs(old_row_index - row_index) + \
                abs(old_col_index - col_index)
            old_row_index, old_col_index = row_index, col_index
        cost += len(list(str_list))
        ans_list.append(cost)
