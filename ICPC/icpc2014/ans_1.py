#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import itertools

def taxed_price(rate,p):
  return math.floor(p * (100 + rate)/100)

ans_list = []
while (True):
  x, y, s = map(int, input().split(' '))
  #終了条件の時,答えを出力して終了
  if x==0 and y==0 and s==0:
    for answer in ans_list:
      print(answer)
    break
  #終了条件でないとき
  else:
    #合計がsになるような2組の価格の組み合わせ(重複あり)p_combinationsを求める
    p_combinations = list(itertools.combinations_with_replacement(range(1,s), 2))
    # print(len(p_combinations))

    #組み合わせに対して税込価格の合計がsとなる組み合わせを配列pricesに格納する
    prices = []
    for p1, p2 in p_combinations:
      if s == taxed_price(x,p1) + taxed_price(x, p2):
        prices.append((p1, p2))
    # print(len(prices))

    #配列pricesのなかで新たな税率で税込価格を計算し、最大値をansとする
    ans = 0
    for p1, p2 in prices:
      if ans <= taxed_price(y,p1) + taxed_price(y,p2):
        ans = taxed_price(y,p1) + taxed_price(y,p2)
    ans_list.append(ans)
