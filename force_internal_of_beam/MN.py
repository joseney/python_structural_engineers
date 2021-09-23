import numpy as np
def getDomian (a,b,c, As1, As2, fck, fyk):
        '''
        Calculates Mrd for a given section and a given axial force.
        :param a: Section height (mm)
        :param b: Section width (mm)
        :param c: concrete cover (mm)
        :param As1: bottom rebar area (mm^2)
        :param As2: top rebar area (mm^2)
        :param fck: Concrete resistence (Mpa)
        :param fyk: concrete resistence (Mpa)
        :return:
        (Nrd, Mrd) = resostance diagram (kNm)
        '''

        d = a - c

        # concret
        gamma_c = 1.5
        fcd = 0.85*fck/gamma_c # MPa
        eps_cc = -0.0020
        eps_cu = -0.0035

        # steel
        gamma_s = 1.15
        fyd = fyk/gamma_s # Mpa
        Es = 200000       # Mpa
        eps_su = 0.01
        eps_y = fyd/Es

        def rel_c (eps):
            # stress-strain for concrete
            n = len (eps)
            sig = np.zeros(n)
            for i in range (n):
                if eps[i] >=0:
                    sig[i]=0
                elif 0>eps[i] and eps[i]>=eps_cc:
                    sig[i]=-fcd*(2-eps[i]/eps_cc)*eps[i]/eps_cc
                    sig[i] = -fcd
                else:
                    print('invalid eps value')
            return(sig)
    # DOMAIN I
        yn_sup = -9999
        yn_inf = 0
        yn = np.linspace(yn_sup, yn_inf, n_step)
        psi = eps_su / (d - yn)
        eps_s1 = np.full(n_step, eps_su)
        eps_s2 = - psi * (yn - c)
        sig_s1 = rel_s(eps_s1)
        sig_s2 = rel_s(eps_s2)

        Nrd_1 = As1 * sig_s1 + As2 * sig_s2
        Mrd_1 = As1 * sig_s1 * (a / 2 - c) - As2 * sig_s2 * (a / 2 - c)

    # DOMANIN II
        yn_sup = 0.1
        yn_inf = -d*eps_cu/(eps_su - eps_cu)
        yn = np.linspace(yn_sup, yn_inf, n_step)
        psi = eps_su/(d -yn)
        eps_s1 = np.full(n_step, eps_su)
        eps_s2 = -psi*(yn-c)
        sig_s1 = rel_s(eps_s1)
        sig_s2 = rel_s(eps_s2)

        Nc = np.zeros(n_step)
        Mc = np.zeros(n_step)
        for i in range(n_step):
            y = np.linspace(0,yn[i],10)
            eps_c = -(yn[i]-y)*psi[i]
            eps_c = np.round(eps_c,7)
            sig_c = rel_c(eps_c)
            Nc[i] = b*np.trapz(sig_c,y)
            ygc = np.nan_to_num(np.trapz(sig_c*y,y)/np.trapz(sig_c,y))
            #ygc = np.nan_to_num(np.trapz(sig_c*y,y)/np.trapz(sig_c,y))
            Mc[i]=Nc[i]*(a/2 - ygc)
        Nrd_2 = Nc+As1*sig_s1 + As2*sig_s2
        Mrd_2 = -Mc + As1*sig_s1*(a/2-c) - As2*sig_s2*(a/2-c)


    # Domani III
        yn_sup = -d * eps_cu / (eps_su - eps_cu)
        yn_inf = -d * eps_cu / (eps_su - eps_cu)
        yn = np.linspace(yn_sup, yn_inf, n_step)
        psi = -eps_cu / yn
        eps_s1 = -psi*(yn-d)
        eps_s2 = -psi*(yn-c)
        eps_s1 = np.round(eps_s1,5)
        eps_s2 = np.round(eps_s2, 5)


        for i in range(n_step):
            y = np.linspace(0, yn[i], 10)
            eps_c = - (yn[i] - y) * psi[i]
            eps_c = np.round(eps_c, 7)
            sig_c = rel_c(eps_c)
            Nc[i] = b * np.trapz(sig_c, y)
            ygc = np.trapz(sig_c * y, y) / np.trapz(sig_c, y)
            Mc[i] = Nc[i] * (a / 2 - ygc)

        Nrd_3 = Nc + As1 * sig_s1 + As2 * sig_s2
        Mrd_3 = -Mc + As1*sig_s1*(a/2 - c) - As2*sig_s2 * (a/2 - c)

    # DOMANI IV
        yn_sup = -d*eps_cu/(eps_y - eps_cu)
        yn_inf =a
        yn = np.linspace(yn_sup, yn_inf, n_step)
        psi = -eps_cu / yn
        eps_s1 = -psi*(yn-d)
        eps_s2 = -psi*(yn-c)
        sig_s1 = rel_s(eps_s1)
        sig_s2 = rel_s(eps_s2)
        Nc = np.zeros(n_step)
        Mc = np.zeros(n_step)
        for i in range(n_step):
            y = np.linspace(0,yn[i],10)
            eps_c = -(yn[i] - y)*psi[i]
            eps_c = np.round(eps_c,7)
            sig_c = rel_c(eps_c)
            Nc[i] = b*np.trapz(sig_c,y)
            ygc   = np.trapz(sig_c*y,y)  / np.trapz(sig_c,y)
            Mc[i] = Nc[i]*(a/2 - ygc)
        Nrd_4 = Nc + As1*sig_s1 + As2*sig_s2
        Mrd_4 = - Mc + As1*sig_s1*(a/2 -c) - As2*sig_s2*(a/2 - c)
    # DOMANI  V
        yn_sup = a
        yn_inf = a + 9999
        yn = np.linspace(yn_sup, yn_inf, n_step)
        t = 3/7*a
        psi = - eps_cc/(yn-t)
        eps_s1 = -psi*(yn - d)
        eps_s2 = -psi*(yn - c)
        sig_s1 = rel_s(eps_s1)
        sig_s2 = rel_s(eps_s2)
        Nc = np.zeros(n_step)
        Mc = np.zeros(n_step)
        for i in range(n_step):
            y = np.linspace(0,a,10)
            eps_c = -(yn[i] - y*psi[i])
            eps_c = np.round(eps_c,7)
            sig_c = rel_c(eps_c)
            Nc[i] = b*np.trapz(sig_c, y)
            ygc = np.trapz(sig_c*y,y)  / np.trapz(sig_c,y)
            Mc[i] = Nc[i]*(a/2 - ygc)
        Nrd_5 = Nc + As1*sig_s1 + As2*sig_s2
        Mrd_5 = -Mc + As1*sig_s1*(a/2 -c) - As2*sig_s2*(a/2 - c)

        Mrd = np.hstack((Mrd_1*1E-6, Mrd_2*1E-6, Mrd_3*1E-6, Mrd_4*1E-6*Mrd_5*1E-6))
        Nrd = np.hstack((Nrd_1*1E-6, Nrd_2*1E-6, Nrd_3*1E-6,Nrd_4*1E-6, Nrd_5*1E-6))
    return((Nrd,Mrd))

#getDomian (400,300,50, 1017, 452, 25, 450)