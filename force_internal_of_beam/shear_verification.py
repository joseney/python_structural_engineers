import numpy as np
a = 400 #mm - height of the section
b = 300 #mm - width of the section
c = 50  #mm - concrete cover
d = a - c #mm - is the effective section
z = 0.9*d #mm - is the inner lever arm
Abar = 201.062 #mm^2 - is the total area of a dia 16 reba
fck = 25 #N/mm^2
fyk = 450 #N/mm^2
gamma_s = 1.15
gamma_c = 1.5
fcd = 0.85*fck/gamma_c # N/mmm^2
#==================

bw = b
k = 1 + (200/d)**0.5
rho_l = max(3*Abar/ (bw*d), 0.02 )
sig_cp = 0
Ac = b*a
CRd_c = 0.18/gamma_c
k1 = 0.15
nu_min = 0.035*k**1.5*fck**0.5

Vrd_c = max((CRd_c*k*(100*rho_l*fck)**(1/3) + k1*sig_cp)*bw*d, (nu_min+k1*sig_cp)*bw*d)

print(Vrd_c)
#print("Vrd_c = %s is %d years old." % (Vrd_c, b))
print("Vrd_c = %d"%(Vrd_c*0.001)+" kN")

Asw = 100 #mm^2, 2phi8
s = 250 #mm, step
rho_w = Asw/(s*bw)
rho_w_min = (0.08*(fck)**0.5)/fyk
print("rho_w = %.6f" %(rho_w) )
print("rho_w_min = %.6f" %(rho_w_min) )