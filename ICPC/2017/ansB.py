#!/usr/bin/env python3
# -*- coding: utf-8 -*-
ans_list = []
while (True):
    A = input()
    # 終了条件の時,答えを出力して終了
    if A == ".":
        for answer in ans_list:
            print(answer)
        break
    # 終了条件でないとき
    else:
        B = input()
        count = 0
        if A == B:
            ans_list.append("IDENTICAL")
        else:
            n = int((A.count('"'))/2)
            for i in range(n):
                if '"' in A:
                    str1 = A[A.find('"')+1:]
                    A = str1[str1.find('"')+1:]
                    str1 = str1[0:str1.find('"')]
                    str2 = B[B.find('"')+1:]
                    B = str2[str2.find('"')+1:]
                    str2 = str2[0:str2.find('"')]
                    if str1 != str2:
                        count += 1
            if count == 1:
                ans_list.append("CLOSE")
            else:
                ans_list.append("DIFFERENT")
