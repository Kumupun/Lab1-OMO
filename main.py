import newton
import smpl_iter
import scipy.optimize as opt

def print_menu():
    print("Menu:")
    print("1. Find root using Newton's method")
    print("2. Find root using Simple Iteration method")
    print("3. Exit")

def Newton(x0,inter, epsilon):
    (l,r) = map(float, inter.split())
    max_iter = newton.approxN(x0, l, r, epsilon)
    if max_iter is None:
        return [None, None]
    res = newton.newton(x0,epsilon,max_iter)
    res_s = opt.newton(lambda x: x**3 + x**2 - 4*x - 4, x0)
    return [res, res_s]


def Simple_iteration(x0, inter, epsilon):
    (l,r) = map(float, inter.split())
    max_iter = smpl_iter.approxI(x0, l, r, epsilon)
    if max_iter is None:
        return None
    res= smpl_iter.smpl_iter(x0,epsilon,max_iter)
    return res

def main():
    print_menu()
    c= input("Choose an option (1-3): ")
    if c == '1':
        print("Newton's Method Selected.")
        inter = input("Enter interval [l, r]: ")
        x0 = float(input("Enter initial guess x0: "))
        epsilon = float(input("Enter epsilon: "))
        result = Newton(x0,inter, epsilon)
        answ = result[0]
        scpy_res = result[1]
        if answ is not None:
            print("Root found:", answ)
            print("Root found by scipy:", scpy_res)
        else:
            print("No root found.")
            

    elif c == '2':
        print("Simple Iteration Method Selected.")
        inter = input("Enter interval [l, r]: ")
        x0 = float(input("Enter initial guess x0: "))
        epsilon = float(input("Enter epsilon: "))
        result = Simple_iteration(x0,inter, epsilon)
        if result is not None:
            print("Root found:", result)
        else:
            print("No root found.")

    elif c == '3':
        print("Exiting the program.")
        return 0
    return 0
main()