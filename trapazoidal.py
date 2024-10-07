import math
def Trapazoidal(f, l, h, n):
    """
    Trapazoidal

    Arguments:
    f: Function representing the derivative dy/dx
    x0: Initial value of x
    y0: Initial value of y
    h: Step size
    n: Number of iterations
    """

    x = [l]
    y = [f(l)]
    #x[-1] = 0
    for i in range(1, n+1):
        x_next = x[i-1] + h
        y_next = f(x_next)
        x.append(x_next)
        y.append(y_next)
    print("Values of x: \n")
    for i in range(0,n):
        print(x[i])
        print("\n")
    print("Values of y: \n")
    for i in range(0, n):
        print(y[i])
        print("\n")
    sum1 = y[0] + y[n]
    sum2 = 0
    for i in range(1, n-1):
        sum2 = sum2 + y[i]
    integral = (h/2)*(sum1 + 2*sum2)
    return integral

# Get the equation, initial values, step size, and number of iterations from the user
equation = input("Consider the integral\n∫ i*dx then,\nEnter, i = ")
f = lambda x: eval(equation)

ch = int(input("Enter:\n1: limits\n2: step size\nYour choice: "))
if ch==1:
    u = float(input("Enter the upper limit: "))
    l = float(input("Enter the lower limit: "))
    n = int(input("Enter the number of intervals: "))
    a = u-l+1
    h = (a)/n
elif ch==2:
    u = float(input("Enter the upper limit: "))
    l = float(input("Enter the initial value of x: "))
    h = float(input("Enter the step size: "))
    a = u-l+1
    n = int((u-l)/h)
    n = n+1

# Solve the ODE using Euler's method
integral = Trapazoidal(f, l, h, n)

# Print the results
print("Approximate Integral: ", integral)
