#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n, m = map(int, input().split(' '))
a_list = list(map(int, input().split(' ')))

ans = 0
for i in range(len(a_list)):
  for j in range(i + 1, len(a_list)):
    pre_ans = a_list[i] + a_list[j]
    if ans < pre_ans and m >= pre_ans:
      ans = pre_ans
if ans == 0:
  ans = 'NONE'

print(ans)


