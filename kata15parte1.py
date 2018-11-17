import math
import matplotlib.pyplot as plt
import numpy as np
def Euler(f, xa, xb, ya, n):
      h = (xb - xa) / float(n)
      x = xa
      y = ya
      for i in range(n):
          y += h * f(x, y)
          x += h
      return y
print ('Valor de y Cuando X=1.5     y=',Euler(lambda x, y: 2*x*y, 1, 1.5, 1, 5))
