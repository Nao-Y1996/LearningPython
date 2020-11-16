#!/usr/bin/env python3
# -*- coding: utf-8 -*
import numpy as np
import matplotlib.pyplot as plt


# 近傍順位関数
# lは学習が進むにつれて小さくすることで学習後半は近接するノードのみ更新することができる
def nearest_neighbor(k, l):
    return np.exp(-1*k/l)

# 収束速度の制御関数
# 近接順位関数における　l を変化せさる関数
# l は t(学習回数)が大きくなるほど小さくしたいので initial < finalとする
def convergence_speed(t, max_t, initial, final):
    return initial * (initial/final)**(t/max_t)


# t = np.array((range(1000)))
# speed = convergence_speed(t, 1000, 30, 1000)

x = np.array([11, 25, 0, 16, 6, 1, 26, 20, 5, 13, 10, 21, 24, 22, 12, 4, 7, 17, 29, 8, 15, 14, 18, 3, 19, 23, 2, 28, 27, 9]
)
y = nearest_neighbor(x, 10)
print(y)
plt.scatter(x, y, c="blue")
plt.show()
