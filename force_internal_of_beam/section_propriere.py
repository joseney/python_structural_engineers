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

# Bending moment resist of the sections

Nrd_tot,  Mrd_tot=MN.getDomain(a,b,c, 2*Abar, 2*Abar, fck,fyk)
Mrd1 = np.interp(0,Nrd_tot[::-1], Mrd_tot[::-1])
Nrd_tot, Mrd_tot = MN.getDomain(a,b,c, 3*Abar, 2*Abar, fck, fyk)
Mrd3 = np.interp(0,Nrd_tot[::-1], Mrd_tot[::-1])

if M_pos_max[0]<Mrd1:
    print("sec.1:VERIFIED")
else:
    print("sec.2: NOT VERIFIED")
if M_neg_max[0]>Mrd2:
    print("sec. 2: VERIFIED")
else:
    print("sec.2:NOT VERIFIED")
if M_pos_max[1]<Mrd3:
    print("sec. 3:VERIFIED")
else:
    print("sec.3: NOT VERIFIED")

Vmax = max(max(V_pos_max), max(abs(V_neg_max)))
print("Vmax = \%d"\%(Vmax) + "kN")

