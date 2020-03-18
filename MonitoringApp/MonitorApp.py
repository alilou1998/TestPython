from math import *
A=int(input("Lire A:"))
x=float(A)
epsilon=float(input("Lire epsilon:"))
i=0
while abs(x**2-A)>epsilon:
    i=i+1
    x=(x+A/x)/2
    print("Iteration ",i," La valeur de x : ",x)
print("La valeur finale de x : ",x)

############
print("La valeur finale de racinecarre(x) : ",sqrt(A))
print("Le nombre d'iteration : ",log2(526))
print("Mac")
print("Xps")
print("Xps2")
print("Mac2")
