
import numpy as np
import pandas as pd


# COLUMN BUCKLING
fyk = 355 #N/mm^2
E = 200000 #Mpa
G = 81000 #N/mm^2

# HE300B
h = 300 #mm (section height)
b = 300 #mm (section width)
tw = 11 #mm (web width)
tf = 19 #mm (flange width)
A = 161.3*10**2  #mm^2 (total area)
Iy = 25170*10**4 #mm^4 (second moment of area, y axis)
iy = 13*10 #mm (radius of gyration, y axis)
Wy = 1678*10**3 #mm^3 (elastic section modulus, y axis

Iz = 8563*10**4 #mm^4 (torsional constant)
Iw = (Iz*(h - tf)**2)/4 #mm^6 (warping constant
L = 7.5*10**3 #mm
fyk  = 355 # N/mm^2
E =  200000 # Mpa
G = 81000 # N/mm^2


alpha_y = 0.21
Lcr_y = 2*L
lambda_l =  0.4
lambda_y = (Lcr_y/iy)*(1/lambda_l)
phi_y = 0.5*(1+alpha_y*(lambda_y - 0.2) + lambda_y**2)
chi_y = 1/(phi_y + np.sqrt(phi_y**2 - lambda_y**2))

print("Mcr = %.2f" %(alpha_y))
print("Lcr_y = %.2f" %(Lcr_y ))
print("lambda_y = %.2f" %(lambda_y))
print("phi_y= %.2f" %(phi_y))
print("chi_y= %.2f" %(chi_y))