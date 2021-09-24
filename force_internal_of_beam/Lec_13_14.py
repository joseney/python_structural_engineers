import matplotlib.pyplot as plt
import sympy as s
import numpy as np

s.init_printing(use_unicode=True)
EI, w, L,x, C1, C2 = s.symbols('EI w_o L x C1 C2')
y = s.Function('y')
M = 1/2*w*L*x-1/2*w*x**2
expr1 = s.Eq(y(x).diff(x,x)*EI,M)
s.pprint(expr1)
#expr2 = s.integrate(M,x)
#expr3 = s.integrate(expr2,x)
expr2 = s.dsolve(expr1)
s.pprint(expr2)
expr3 = expr2.subs([(x,0), (y(0),0)])
expr4 = expr2.subs([(x,L), (y(L),0)])
constants = s.solve([expr3,expr4],C1,C2)
s.pprint(constants)
Dx = expr2.subs(constants)
s.pprint(s.simplify(Dx))
diffDx = Dx.rhs.diff(x)
s.pprint(diffDx)
xmax = s.solve(diffDx,x)[0]
Dmax = Dx.subs(x,xmax)
s.pprint(Dmax)
Dx2=Dx.subs([(EI, 200E9*0.05**4/12),
              (L,10),
              (w,4)])
s.pprint(Dx2)
lambdaX = s.lambdify(x,Dx2.rhs, modules=['numpy'])
print(lambdaX)
xval = np.linspace(0,10,100)
yval = lambdaX(xval)
#plt.plot(xval, xval**2)
plt.plot(xval, xval)
#plt.ylabel("Deflection (m)")
plt.show()