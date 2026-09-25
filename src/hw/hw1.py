#!/usr/bin/env python

import numpy as np

test1 = np.array([1, 5, 10, 3, 4, 25, 30])
test2 = np.array([11, 15, 20, 21, 35, 40, 45])
test3 = np.array([2, 4, 6, 8])

def homework(a) -> np.ndarray:
    arr = np.array([])
    for i in a:
        if not (i % 5) and (i % 2):
            arr = np.append(arr, i)
    return arr

def prep():
    pass

def hw():
    prep()
    print("2. Manipulating Data Using Numpy （9/24）")
    print(homework(test1))
    print(homework(test2))
    print(homework(test3))
