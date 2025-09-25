def newton(x0,epsilon,max_iter):
    f = lambda x: x**3+x**2-4*x-4
    Df = lambda x: 3*x**2+2*x-4
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
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

