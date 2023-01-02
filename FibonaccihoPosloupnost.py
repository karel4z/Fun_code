a=[0,1]
b=int(input("Zadej kolik chceš čísel posloupnosti: "))
for i in range(b):
    a.append(a[-1]+a[-2])
print(a[0:b])

#↑ kód pro výpočet fibonacciho posloupnosti

from turtle import *
color("black")
speed(0)
pensize(3)
a=a[1:len(a)]

    

def ctverec(x):
    for i in range(4):
        fd(x)
        rt(90)
    rt(90)
    fd(x)
    lt(90)
    circle(x,90)

x=a[0]*10
ctverec(x)
for i in range(b-1):
    x=a[i+1]*10
    lt(90)
    fd(x)
    rt(90)
    ctverec(x)
input()
