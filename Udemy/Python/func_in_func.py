#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#関数内関数
def outer(a,b):
  def plus(c,d):
    return c + d
  r1 = plus(a, b)
  r2 = plus(a, b)
  print(r1 * r2)

outer(1,2)


#クロージャー
def circle_area(pi):
  def calculate(radius):
    return radius**2 * pi
  return calculate

calc1 = circle_area(3.14)
calc2 = circle_area(3.141592)

print(calc1(5),calc2(5))

