#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ans_list = []
while (True):
    m, n, p = map(int, input().split(' '))
    # 終了条件の時,答えを出力して終了
    if n == 0 and m == 0 and p == 0:
        for answer in ans_list:
            print(answer)
        break
    # 終了条件でないとき
    else:
        count = 0
        search_list = [p]
        cov_list = []
        num_list = []
        for i in range(n):
            a, b = map(int, input().split(' '))
            num_list.append([a, b])
        # print(num_list)
        for num in num_list:
            # print(f'a:{search_list}')
            for j in search_list:
                _id_index = None
                try:
                    _id_index = num.index(j)  # 感染者のindexを探す
                    # 見つけたら探すリスト更新:
                    if _id_index is not None:
                        for i in num:
                            search_list.append(i)
                            # print(f'b:{search_list}')
                        search_list = list(set(search_list))
                    # print(f'c:{search_list}')
                except:
                    e = 0
        # print(cov_list)
        ans = len(search_list)
        if ans == 0:
            ans = 1
        ans_list.append(ans)
