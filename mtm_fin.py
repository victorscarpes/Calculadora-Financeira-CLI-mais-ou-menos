import os
from scipy.optimize import newton

modulo = __name__

def clear():
    os.system("cls")

def F_P(i, n):
    return (1+i*0.01)**n

def P_F(i, n):
    return 1/((1+i*0.01)**n)

def F_A(i, n, ante=False):
    if ante == False:
        return ((1+i*0.01)**n -1)/(i*0.01)
    return ((1+i*0.01)**n -1)/(i*0.01) * (1+i*0.01)

def P_A(i, n, ante=False):
    if ante == False:
        return ((1+i*0.01)**n -1)/(i*0.01*((1+i*0.01)**n))
    return ((1+i*0.01)**n -1)/(i*0.01*((1+i*0.01)**(n-1)))

def A_F(i, n, ante=False):
    if ante == False:
        return (i*0.01)/((1+i*0.01)**n -1)
    return (i*0.01)/((1+i*0.01)**n -1) * 1/(1+i*0.01)

def A_P(i, n, ante=False):
    if ante == False:
        return (i*0.01*((1+i*0.01)**n))/((1+i*0.01)**n -1)
    return (i*0.01*((1+i*0.01)**(n-1)))/((1+i*0.01)**n -1)

def taxa_equivalente(i=1, n=1):
    return ((1+i*0.01)**n-1)*100

def taxa_efetiva_equivalente(i=1, n=1):
    return 100*((1 + (i*0.01)/n)**n -1)

def taxa(P=None, F=None, A=0, n=0, ante=False):
    if (P != None and F != None and A in (None, 0)):
        def func(x):
            return P - F*P_F(i=x, n=n)
    elif P == None and F != None and A != None:
        def func(x):
            return F - A*F_A(i=x, n=n, ante=ante)
    elif P != None and F == None and A != None:
        def func(x):
            return P - A*P_A(i=x, n=n, ante=ante)
    else:
        return None
    return newton(func, 0.01, fprime=None, args=(), tol=1.48e-10, maxiter=100, fprime2=None)

def periodos(P=None, F=None, A=0, i=0, ante=False):
    if (P != None and F != None and A in (None, 0)):
        def func(x):
            return P - F*P_F(i=i, n=x)
    elif P == None and F != None and A != None:
        def func(x):
            return F - A*F_A(i=i, n=x, ante=ante)
    elif P != None and F == None and A != None:
        def func(x):
            return P - A*P_A(i=i, n=x, ante=ante)
    else:
        return None
    return newton(func, 0.01, fprime=None, args=(), tol=1.48e-10, maxiter=100, fprime2=None)

if modulo == "__main__":
    print(F"Este módulo é para ser usado com um terminal interativo de Python!")