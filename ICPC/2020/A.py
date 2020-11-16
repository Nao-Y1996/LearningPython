#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time
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
      p=[]
      time.sleep(0.5)
      p=list(map(int,input().split(' ')))
      box = ([0]*4)
      count = 0
      for i in range(n-3):
        box[0] = p[i]
        box[1] = p[i+1]
        box[2] = p[i+2]
        box[3] = p[i+3]
        if box[0]==2 and box[1]==0 and box[2]==2 and box[3]==0:
          count += 1
      ans_list.append(count)
