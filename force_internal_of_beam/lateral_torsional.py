import numpy as np
# HE300B
h = 300 #mm (section height)
b = 300 #mm (section width)
tw = 11 #mm (web width)
tf = 19 #mm (flange width)
A = 161.3*10**2  #mm^2 (total area)
Iy = 25170*10**4 #mm^4 (second moment of area, y axis)
iy = 13*10 #mm (radius of gyration, y axis)
Wy = 1678*10**3 #mm^3 (elastic section modulus, y axis
L = 7.5*10**3 #mm

fyk = 450 #N/mm^2
k = 0.7
kw = 0.7
Cl = 2.092
It = 185*10**4 #mm^4
alpha_lt = 0.4
lambda_lt_0 = 0.4
beta = 0.75
E =  200000 # Mpa
G = 81000 # N/mm^2
Iz = 8563*10**4 #mm^4 (torsional constant)
Iw = (Iz*(h - tf)**2)/4 #mm^6 (warping constant

Mcr = Cl*np.pi**2*E*Iz/((k*L)**2)*np.sqrt((k/kw)*Iw/(Iz) + (k*L)**2*G*It/(np.pi**2*E*Iz))*1e-6

lambda_lt = np.sqrt(Wy*fyk/(Mcr*1e6))
phi_lt = 0.5*(1+alpha_lt*(lambda_lt - lambda_lt_0) + beta*lambda_lt**2)
chi_lt = 1/(phi_lt + np.sqrt(phi_lt**2 - beta*lambda_lt**2))

print("Mcr = %.2f"%(Mcr))
print("lambda_lt = %.2f"%(lambda_lt))
print("phi_lt = %.2f"%(phi_lt))
print("chi_lt = %.2f"%(chi_lt))