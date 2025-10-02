import math
def smpl_iter(x0, epsilon, max_iter):
    f = lambda x: (4*x**2 +4*x -16)**(1/3)
    xn = x0
    for n in range(0,max_iter):
        x1 = f(xn)
        if abs(x1-xn) <= epsilon:
            print('Found solution after',n,'iterations.')
            return x1
        print('Iteration',n,': x =',x1,': New x =',xn,'\n')
        xn = x1
    print('Exceeded maximum iterations. No solution found.')
    return None

def approxI(x0,lend, rend, epsilon):
    f = lambda x: (4*x**2 +4*x -16)**(1/3)
    Df = lambda x: (8*x +4)/(3*(4*x**2 +4*x -16)**(2/3))
    p =  abs(f(x0 )-x0)
    print( Df(lend), Df(rend))
    q=max(abs(Df(lend)), abs(Df(rend)))
    if q >= 1:
        print("The method may not converge q =", q)
        return None
    if p> (1-q)*max(abs(x0-lend), abs(x0-rend)):
        print("The initial approximation must satisfy the condition |f(x0)-x0| <= (1-q)*max(|l|,|r|).")
        print("Here p =", p, "and (1-q)*max(|l|,|r|) =", (1-q)*max(abs(x0-lend), abs(x0-rend)))
        return None
    n= math.ceil((math.log(abs(f(x0)-x0)/((1-q)*epsilon))/math.log(1/q))+1)
    print("The number of iterations apriori:", n)
    return n