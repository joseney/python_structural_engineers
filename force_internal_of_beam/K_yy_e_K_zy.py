
import numpy as np
import pandas as pd

k = 0.7
kw = 0.7
c1 = 2.-92
alpha_lt = 0.34
lambda_lt_0 = 0.4
beta = 0.75

Mcr = c1*np.pi**2*E*Iz/((k*L))**2)*np.sqrt((k/kw)*Iw/(Iz) + (k*L)**2*G*It/(np.pi**2*E*Iz))