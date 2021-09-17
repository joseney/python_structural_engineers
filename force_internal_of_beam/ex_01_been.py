import numpy as np
l = 5 #m
q = 20 #kN/m

# The equilibrium equations are:
# Ha = 0
# Va+Vb -ql=0
# VbL-q^2/2 = 0
#solving the sistem we obtain
# Ha=0 , Va = q*L/2 , Vb = q*l
# So the bending moment M and the shear V of the beam will be equal to
# M= Va.x - q*x^2/2
#  =q/2(l*x-X^2)
# V = Va-q*x
#   = q*(L/2 - x)
## SOLUTION
x = np.linspace(0,1,20)

M = q/2*(l*x-x**2)
V = q*(l/2-x)

print(V)
# [ 0. 2.60387812  5.15235457  7.64542936 10.08310249 12.46537396  14.79224377 17.06371191 19.27977839 21.44044321 23.54570637 25.59556787  27.5900277  29.52908587 31.41274238 33.24099723 35.01385042 36.73130194 38.3933518  40. ]

print(M)
# [50. 48.94736842 47.89473684 46.84210526 45.78947368 44.73684211
#  43.68421053 42.63157895 41.57894737 40.52631579 39.47368421 38.42105263 37.36842105 36.31578947 35.26315789 34.21052632 33.15789474 32.10526316 31.05263158 30. ]

from matplotlib import pyplot as plt
plt.figure(figsize=(10,4))
plt.plot(([0])*len(x), color= 'y')
plt.plot(-M)
plt.plot(V)