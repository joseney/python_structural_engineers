
import numpy as np
import matplotlib.pyplot as plt
from celluloid import Camera
P=10
l = 20
a = 4
EI = 200000*(10**6)*(0.05*0.05**3)/12

fig = plt.figure()
camera = Camera(fig)

b = l - a
R1 = P*b/l
R2 = P*a/l

x = np.linspace(0,l,100)

for i in x:
    a = i
    # SHEAR FORCE
    V = np.linspace(0,0,100)
    V[x<a]  = R1
    V[x>=a] = -R2

    # BENDING MOMENT
    M = np.linspace(0,0,100)
    M[x<a] = R1*x[x<a]
    M[x>=a] = R1*x[x>=a] - P*(x[x>=a]-a)

    # D
    D = np.linspace(0,0,100)
    D[x<a] = P*b*x[x<a]/(6*l*EI)*(l**2-b**2-x[x<a]**2)
    D[x>=a] = P*a*(l-x[x>=a])/(6*l*EI)*(2*l*x[x>=a] - x[x>=a]**2-a**2)
   # Camera.snap()
    #print(D)

    #fig = plt.figure()
    ax1 = fig.add_subplot(311)
    plt.title("SHEAR FORCE DIAGRAM")
    ax2 = fig.add_subplot(312)
    plt.title("BENDING MOMENT DIAGRAM")
    ax3 = fig.add_subplot(313)
    plt.title("DEFLECTED SHAPE ELASTIC CURVE")

    ax1.plot(x,V,color = "red", linewidth=3)
    ax1.plot(x,V,color = "green", linewidth=3)
    ax1.plot(x,V,color = "blue", linewidth=3)

    fig.tight_layout()
    camera.snap()
animation = camera.animate()
animation.save("beam_analisis.mp4")
plt.show