#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np

a = np.array([1,2,3])
b = list(a)
b.append(4)
print(b)
b = np.array(b)
print(type(b))


# d = {'nao': 24, 'ryoya': 24, 'shota': 23}

# # print(d['nao'])

# print(type(d.keys()))

# print(help('dict_keys'))

# a = [1,2,3,4,5,6,1,2,3,4,5]
# print( a.index(3) )


