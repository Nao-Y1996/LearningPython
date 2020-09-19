#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
【問題】
①九九の結果を２次元配列(numpy配列でも良い)として出力せよ
出力例：
[[ 1  2  3  4  5  6  7  8  9]
 [ 2  4  6  8 10 12 14 16 18]
 [ 3  6  9 12 15 18 21 24 27]
 [ 4  8 12 16 20 24 28 32 36]
 [ 5 10 15 20 25 30 35 40 45]
 [ 6 12 18 24 30 36 42 48 54]
 [ 7 14 21 28 35 42 49 56 63]
 [ 8 16 24 32 40 48 56 64 72]
 [ 9 18 27 36 45 54 63 72 81]]
"""

#回答例１　
#方針：はじめに9*9の２次元配列を用意して1つずつ変更していく
#配列の初期化に注意すること https://note.nkmk.me/python-list-initialize/

#悪い例
ans1_bad = [[0] * 9] * 9
for i in range(9):
  for j in range(9):
    #print((i+1) * (j+1))
    ans1_bad[i][j] = (i+1) * (j+1)
    #print(ans2_bad)
print(ans1_bad)

#良い例
ans1_ok = [[0] * 9 for i in range(9)]
for i in range(9):
  for j in range(9):
    #print((i+1) * (j+1))
    ans1_ok[i][j] = (i+1) * (j+1)
    #print(ans2)
print(ans1_ok)



#回答例２
#方針：1*81の１次元配列を作りnumpyのreshapeメソッドを使って２次元に変換
import numpy as np

ans2 = []
for i in range(9):
  for j in range(9):
    ans2.append((i+1) * (j+1))
ans2 = np.array(ans2).reshape([9,9])
print(ans2)
