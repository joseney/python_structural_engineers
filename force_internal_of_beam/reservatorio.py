import math

Hi = 10
Hf = 1
D = 20
d = 0.05
g = 9.81
C = 0.51
C = [0.98,0.61,0.8,0.51]
t = ((math.pi*D**2)/2)/(C[3]*(math.pi*D**2)/2)*(math.sqrt(Hi)-math.sqrt(Hf))*(math.sqrt(2/g))

print(t)
print(t/3600/24)
