import math
def newton(x0,epsilon,max_iter):
    f = lambda x: x**3+x**2-4*x-4
    Df = lambda x: 3*x**2+2*x-4
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) <= epsilon:
            print('Found solution after',n,'iterations.')
            return xn
        print('Iteration',n,': x =',xn,'f(x) =',fxn)
        Dfxn = Df(xn)
        print('Iteration',n,': Df(x) =',Dfxn)
        if Dfxn == 0:
            print('Zero derivative. No solution found.')
            return None
        xn = xn - fxn/Dfxn
        print('Iteration',n,': New x =',xn,'\n')
    print('Exceeded maximum iterations. No solution found.')
    return None

def approxN (x0,lend, rend, epsilon):
    f = lambda x: x**3+x**2-4*x-4
    Df = lambda x: 3*x**2+2*x-4
    D2f = lambda x: 6*x+2
    l=max(abs(x0-lend), abs(x0-rend))
    if f(lend)*f(rend) >= 0:
        print("The function must have different signs at the endpoints.")
        return None
    elif f(x0)*D2f(x0) >= 0:
        print("The initial approximation must satisfy the condition f(x0)*f''(x0) < 0.")
        return None
    m1 = min(Df(lend), Df(rend))
    M2 = max(D2f(lend), D2f(rend))
    q=M2*l/(2*m1)
    if q >= 1:
        print("The method may not converge q =", q)
        return None
    n= math.ceil((math.log2((math.log(l/epsilon)/math.log(1/q))+1)+1))
    print("The number of iterations apriori:", n)
    return n