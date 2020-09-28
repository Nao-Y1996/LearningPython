#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input())
a_list = list(map(int, input().split(' ')))

ave = sum(a_list)/int(n)

ans_list = []
for i in a_list:
  if ave >= i:
    ans_list.append(i)
print(len(ans_list))
