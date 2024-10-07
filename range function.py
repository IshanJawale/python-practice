numbers = range(5)      # numbers is a range object which has numbers 0 to 5 but excluding 5
print(numbers)          # output is range(0, 5) and not the actual numbers

for number in numbers:  # this prints the actual numbers
    print(number)   

print("--------------")

term = range(11, 20)    # this prints numbers between 11 and 20 excluding 20
for unit in term:
    print(unit)

print("--------------")

x = range(5, 20, 2)     # jumps two numbers at a time, output is 5, 7, 9,...
for z in x:
    print(z)

# shorter way for range function
for i in range(5): 
    print(i)
# so no need to store the range function in a variable
