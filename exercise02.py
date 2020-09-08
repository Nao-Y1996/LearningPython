#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 02:01:36 2020

@author: NaoYamada

【問題】
①要素数100の配列を作成する
ただし要素の値は0~9のランダムな値が入るとする
②その配列に対し、要素の値が3であるのはいくつか？
関数を作成し、実行すること
③要素の値が3となるインデックスを全て出力する
関数を作成し、実行すること

"""
import random

MAX = 100
array = []

#問題①
for i in range(MAX):
    randint = random.randint(0,9)
    array.append(randint)
print(len(array))
print(array)

#問題②
def num_count(arg_array,num):
    return arg_array.count(num)
print('3は{}個含まれています'.format(num_count(array,3)))

#問題③
def all_index(arg_array,num):
    a = []
    for index, value in enumerate(arg_array):
        if value == num:
            a.append(index)
    return a
print('3のインデックスは{}です'.format(all_index(array,3)))

