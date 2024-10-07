equation = input("Enter an equation: ")
f = lambda x, y : eval(equation, {'x':x, 'y':y})
x = 3
y = 4

print(equation)