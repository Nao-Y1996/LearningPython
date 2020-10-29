#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ans_list = []
# while (True):
#     A = input()
#     # 終了条件の時,答えを出力して終了
#     if A == 0:
#         for answer in ans_list:
#             print(answer)
#         break
#     # 終了条件でないとき
#     else:

A = 999999999
i = 1

num_list1 = []
ans1 = []
ans2 = []

while True:
    num_list1.append(i)
    # print(num_list1)
    i += 1
    if sum(num_list1) == A:
        ans1 = num_list1
        break
    if sum(num_list1) > A:
        break

num_list2 = num_list1.copy()
while True:
    num_list2.pop(0)
    if sum(num_list2) == A:
        ans2 = num_list2
        break
    elif sum(num_list2) < A:
        num_list2.append(max(num_list2)+1)

if len(ans1) > len(ans2):
    ans = ans1
else:
    ans = ans2
print(ans[0], len(ans))


# b = 999999999 #Input
# sum = 0
# Check = 0
# Count = 0 #フロア数
# Pcount = 1 #足すべき数値を記憶
# Mcount = 1 #引くべき数値を記憶
# Bottom = 1 #最下層の階数
# while True:
#     if sum < b:
#         sum += Pcount
#         Pcount += 1
#         Count += 1
#     else:
#         sum -= Mcount
#         Mcount += 1
#         Count -= 1
#         Bottom += 1
#     if sum == b:
#         break
# print(Bottom)
# print(Count)
