# -*- coding: utf-8 -*-
"""Лабораторная1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AsnH710BXjBdK8jDBhbLSRUUjnYXkuwZ

вывели фразу командой print
"""

print("Hello World")

"""Задали два числа, a и b."""

a=5
b=2

"""определили значение числа с с помощью других переменных и вывели значение командой print"""

c=a+b
print(c)

"""задали значение переменной d (сторона равностороннего треугольника) и рассчиали площадь треугольника в новой переменной S,вывели площадь командой print"""

d=7.5
S=3**(0.5)*d**2/4
print(S)

"""задали значения переменных, просчитали и вывели значение x"""

a=2
b=7
c=4
x=(a**(2)+b**(2)-c**(3))/2
print(x)

"""задание 1"""

a=5
b=int(input())
print(b)
print(a*b)

"""задание 2"""

a=int(input())
b=int(input())
print((a+b)**2)

"""задание 3"""

a=15
b=10
c=int(input())
print((a+b)/c)

"""задание 4"""

a=int(input())
b=int(input())
print(f"({a}+{b})^2={a}^2+2ab+{b}^2")

"""задание 5"""

a=int(input())
b=int(input())
c=int(input())
P=a+b+c
p=P/2
S=(p*(p-a)*(p-b)*(p-c))**0.5
print(f"S={S},P={P}")

"""задание 6"""

a=int(input())
b=int(input())
print(((a**(3)+14)/5)*b)

"""задание 7"""

a=int(input())
n=int(input())
print((a**(2))//n)

"""задание 8"""

a=float(input())
b=float(input())
print(a//b)
c=int(input())
d=int(input())
print(c*d)
e=int(input())
f=int(input())
print(e%f)

"""задание повышенной сложности 1"""

sec=int(input())
min=sec/60
h=min/60
d=h/24
print(f"минут={min},часы={h},дни={d}")

"""задание повышенной сложности 2"""

n=int(input())
a=str(n)
sum1=a+a
sum2=a+a+a
sum3=n+int(sum1)+int(sum2)
print(sum3)