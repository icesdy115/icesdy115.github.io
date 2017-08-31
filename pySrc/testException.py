#coding=utf-8

x1 = [1,3,5]
y1 = [9,12,13]

L = []

for (x,y) in zip(x1,y1):
    if y > 10:
        L.append(x**2)
print L
