#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ans_list = []
while (True):
  m, n_min, n_max = map(int, input().split(' '))
  #終了条件の時,答えを出力して終了
  if m==0 and n_min==0 and n_max==0:
    for ans in ans_list:
      print(ans)
    break
  #終了条件でないとき
  else:
    p_list = []
    for i in range(m):
      p_list.append(int(input()))
    #ギャップの配列gapsと, 合格者数の配列n_listを作成
    gaps = []
    n_list = list(range(n_min, n_max+1))
    for n in n_list:
      gaps.append(p_list[n-1] - p_list[n])#入力データはソート済みなのでこれでgapの計算ができる
    #gapが最大となるindexを, 配列max_indexesに格納
    max_gap = 0
    max_indexes =[]
    for index, gap in enumerate(gaps):
      if max_gap <= gap:
        max_gap = gap
        max_indexes.append(index)
    #gapが最大となるindexを持つn_listの中で,最大値(合格者数最大)を求める
    n_ans = 0
    for index in max_indexes:
      if n_ans < n_list[index]:
        n_ans = n_list[index]
    #求めた合格者数n_ansを配列に格納
    ans_list.append(n_ans)


