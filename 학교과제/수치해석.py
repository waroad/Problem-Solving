from matplotlib.projections import axes
import math
import numpy as np
import matplotlib.pyplot as plt
import sys
import sympy as sym


a1=math.cos(math.pi/3)
for i in range(6):
    xx = sym.Symbol('x')
    aa = sym.diff((sym.cos(xx)), xx,i)
    print(aa)
a=math.cos(math.pi/4)
b=math.sin(math.pi/4)*(-(math.pi/12))
c=math.cos(math.pi/4)*(-(math.pi/12)**2)/2
print(a+b)
print(a+b+c)
print("{:.2f}".format(((a1-a)/a1)*100))
print("{:.2f}".format(((a1-(a+b))/a1)*100))

