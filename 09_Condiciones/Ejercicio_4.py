import numpy as plt 
import matplotlib.pyplot as plt


#definir la función   >.<
F = lambda T: ((204165.5)/(330 - 2*T)) + (10400/(T-20))
dF= lambda x,dx: (F(x+dx)-F(x-dx))/(2*dx)
dF2= lambda x, dx: (F(x+dx)-2*F(x)+F(x-dx))/(dx**2)
dx= 0.001
x0= 40
a= 40
b= 90
x= 0
epsilon1= dx

#Bisección
for i in range (1,1000):
    aph = (b-a)/2+a
    if dF(a,dx)*dF(aph,dx)<0:
        b=aph
    else:
        a = aph
    if abs(dF(aph,dx))<epsilon1:
        break
print("Bisección")
print(aph)


#Golden Section
F = lambda T: ((204165.5)/(330 - 2*T)) + (10400/(T-20))
a= 40
b=90
epsilon= 0.00001
gr=0.618
start_time = time()

for i in range (1,100):
    d= gr*(b-a)
    x1= a+d
    x2= b-d
    if F(x1)<F(x2):
        a=x2
    else: 
        if F(x1)>F(x2):
            b=x1
    if abs(b-a)<epsilon:
        break


#Elif
z = 3
if z % 2 == 0:
    print("z es divisible entre 2")
elif z % 3 == 0:
    print("z es divisible entre 3")
else: 
    print("z no es divisible entre 2 ni 3")