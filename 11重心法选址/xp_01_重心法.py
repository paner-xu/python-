# coding=UTF-8
# Version:python3.6.0
# Tools:Pycharm2017.3.2
__date__ = '2019/5/4 14:04'
__author__ = 'Remix'
import numpy as np
from math import sqrt
# input x-axis, y-axis, demand and transportation
A = np.array([[4, 15, 20, 5],[4, 5, 10, 15],[4, 6, 5, 2],[8, 8, 8, 8]])
x = []
y = []
temp = []
temp_1 = 0
temp_2 = 0
temp_3 = 0
for i in range(0, 4):
    temp_1 = A[0, i] * A[2, i] * A[3, i] + temp_1
    temp_2 = A[2, i] * A[3, i] + temp_2
    temp_3 = A[1, i] * A[2, i] * A[3, i] + temp_3
# Calculate the center of gravity
x.append(temp_1 / temp_2)
y.append(temp_3 / temp_2)

print(x[0])
print(y[0])
# Calculate the distance from the center of gravity to each point
d = [0] * 4
for i in range(0, 4):
    d[i] = sqrt((A[0,i]-x[0])**2+(A[1,i]-y[0])**2)
print(d)

# Calculate total shipping cost
T = 0
for i in range(0, 4):
    T = A[2, i] * A[3, i] * d[i] + T
temp.append(T)
print(temp[0])

temp_4 = 0
temp_5 = 0
temp_6 = 0
for i in range(0, 4):
    temp_4 = A[0, i] * A[2, i] * A[3, i]/d[i] + temp_4
    temp_5 = A[2, i] * A[3, i]/d[i] + temp_5
    temp_6 = A[1, i] * A[2, i] * A[3, i]/d[i] + temp_6
# Calculate the second center of gravity
x.append(temp_4 / temp_5)
y.append(temp_6 / temp_5)
print(x[1])
print(y[1])
# Calculate the distance from the second center of gravity to each point
for i in range(0, 4):
    d[i] = sqrt((A[0, i] - x[1]) ** 2 + (A[1, i] - y[1]) ** 2)
print(d)
T = 0
for i in range(0, 4):
    T = A[2, i] * A[3, i] * d[i] + T
# Calculate the second total shipping cost
temp.append(T)
print(temp[1])
# Iteration
j = 1
while temp[j-1] - temp[j] > 0.0001:
    j += 1
    temp_7 = 0
    temp_8 = 0
    temp_9 = 0
    T = 0
    for i in range(0, 4):
        temp_7 = A[0, i] * A[2, i] * A[3, i]/d[i] + temp_7
        temp_8 = A[2, i] * A[3, i]/d[i] + temp_8
        temp_9 = A[1, i] * A[2, i] * A[3, i]/d[i] + temp_9

    x.append(temp_7 / temp_8)
    y.append(temp_9 / temp_8)
    print(x[j])
    print(y[j])
    for i in range(0, 4):
        d[i] = sqrt((A[0, i] - x[j]) ** 2 + (A[1, i] - y[j]) ** 2)
    print(d)
    for i in range(0, 4):
        T = A[2, i] * A[3, i] * d[i] + T
    temp.append(T)
    print(temp[j])
    if temp[j-1] - temp[j] <= 0.0001:
        break
print(j-1)
print(x[j-1])
print(y[j-1])
print(temp[j-1])
