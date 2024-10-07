import math
def Trapazoidal(f, l, h, n):
    """
    Simpson 1/3 rd

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
        sum2 = sum2 + y[i+2]
    sum3 = 0
    for i in range(2, n-1):
        sum3 = sum3 + y[i+2]
    
    integral = (h/3)*(sum1 + 4*sum2 + 2*sum3)
    return integral

# Get the equation, initial values, step size, and number of iterations from the user
equation = input("Enter the equation:\ndy/dx = ")
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
    #n = int(input("Enter the number of iterations: "))
#x0 = float(input("Enter the initial value of x: "))
#y0 = float(input("Enter the initial value of y: "))
#h = float(input("Enter the step size: "))
#n = int(input("Enter the number of iterations: "))

# Solve the ODE using Euler's method
integral = Trapazoidal(f, l, h, n)

# Print the results
print("Approximate Integral: ", integral)
