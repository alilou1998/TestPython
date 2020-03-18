T=[3,1,4,2]
def function(T):
    for i in range(4):
        x=T[i]
        j=i-1
        while j>=0 and T[j]<x:
            T[j+1]=T[j]
            j=j-1
        T[j+1]=x
        print("Iteration ",i,"T=",T)
    return T

print(function(T))
