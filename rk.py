

def RK_method(f, x0, y0, h, k):
    """
    Runge Kutta method of fourth order 

    Arguments:
    f: Function representing the derivative dy/dx
    x0: Initial value of x
    y0: Initial value of y
    h: Step size
    n: Number of iterations
    """

    x_values = [x0]
    y_values = [y0]
    for _ in range(n):
        x = x_values[-1]
        y = y_values[-1]
        dy_dx = f(x, y)
        k1 = h * dy_dx
        dy_dx2 = f(x + h/2, y + k1/2)
        k2 = h * dy_dx2
        dy_dx3 = f(x + h/2, y + k2/2)
        k3 = h * dy_dx3
        dy_dx4 = f(x + h, y + k3)
        k4 = h * dy_dx4
        k = (k1 + 2*k2 + 2*k3 + k4)/6
        x_next = x+h
        y_next = y + k
        x_values.append(x_next)
        y_values.append(y_next)

    return x_values, y_values

# Get the equation, initial values, step size, and number of iterations from the user
equation = input("Enter the equation:\ndy/dx = ")
f = lambda x, y: eval(equation)
x0 = float(input("Enter the initial value of x: "))
y0 = float(input("Enter the initial value of y: "))
h = float(input("Enter the step size: "))
n = int(input("Enter the number of iterations: "))

# Solve the ODE using Runge Kutta Method
x_values, y_values = RK_method(f, x0, y0, h, n)

# Print the results
for x, y in zip(x_values, y_values):
    print(f"x = {x:.2f}, y = {y:.6f}")
