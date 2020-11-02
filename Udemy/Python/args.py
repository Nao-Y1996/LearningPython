#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def names(name1, name2, name3):
  print(name1, name2, name3, sep='\n')
#位置引数
names('yamada','tanaka','saito')
#キーワード引数
# names(name2='yamada',name3='tanaka',name1='saito')

#位置引数は引数の数が増えそうな時は *をつけて増えた分の引数をタプルとして受け取れる
def names2(name1, name2, name3, *args):
  print(args)
  print(name1, name2, name3, sep='\n')
  for name in args:
    print(name)
# names2('yamada','tanaka','saito', 'imai', 'ishimaru', 'kaneko')


#キーワード引数は　**をつけることで辞書として受け取れる
def names3(**kwargs):
  print(kwargs)
  for k,v in kwargs.items():
    print(k,v)

# names3(name2='yamada',name3='tanaka',name1='saito')


#位置引数、位置引数のタプル化、キーワード引数、キーワード引数の辞書化、の組み合わせ
def names4(name1, name2, *args, **kwargs):
  print(name1, name2, sep='\n')
  for name in args:
    print(name)
  for k,v in kwargs.items():
    print(k,v)

names4('saito', 'ito', 'nishi', 'katou', name4='yamada',name5='tanaka')