#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools

n = map(int, input().split(' '))
a_list = list(map(int, input().split(' ')))

#回答１
# ans = abs(a_list[0] - a_list[1])
count = 0
for i in range(len(a_list)):
  for j in range(i + 1, len(a_list)):
      if ans > abs(a_list[i] - a_list[j]):
        ans = abs(a_list[i] - a_list[j])
print(f'回答１：{ans}')

#回答２
comb_a_list = list(itertools.combinations(a_list, 2))
ans = abs(comb_a_list[0][0] - comb_a_list[0][1])
for i, j in comb_a_list:
  if ans > abs(i - j):
    ans = abs(i - j)
print(f'回答２：{ans}')