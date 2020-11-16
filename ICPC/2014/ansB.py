#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
ans_list = []
while (True):
    h = int(input())
    # 終了条件の時,答えを出力して終了
    if h == 0:
        for answer in ans_list:
            print(answer)
        break
    # 終了条件でないとき
    else:
        ans = 0
        stones = []
        for row in range(h):
            stone_row = list(map(int, input().split(' ')))
            stones.append(stone_row)
        origin_stones = stones

        while True:
            old_stones = np.array(stones.copy())#ここで１時間取られた np.arrayとlistで挙動が変化する
            print(np.array(old_stones))
            print(np.array(stones))
            # 連続は0にする
            for row in stones:
                check = []
                check.append(row[0])
                start = 0
                for index, stone in enumerate(row):
                    if check[-1] == stone and index != 0:
                        check.append(stone)
                    elif check[-1] != stone and index != 0:
                        check = []
                        check.append(stone)
                        start = index
                    if len(check) >= 3:
                        for i in range(len(check)):
                            row[start+i] = 0
            # print('0にした\n', np.array(stones))
            # 落とす
            stones = np.array(stones)
            for col in range(5):
                check = stones[:, col]
                none_zero = []
                for num in check:
                    if num != 0:
                        none_zero.append(num)
                zeros = [0] * (int(len(check)) - int(len(none_zero)))
                stones[:, col] = (zeros + none_zero)
            # print('落とした\n', stones, '\n', np.array(old_stones))
            ans += old_stones.reshape(
                1, -1).sum() - stones.reshape(1, -1).sum()
            if (old_stones == stones).all():
                ans_list.append(ans)
                break
