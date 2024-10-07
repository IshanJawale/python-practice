# to add two numbers
first_number = input("Enter First Number: ")
second_number = input("Enter Second Number: ")
sum = float(first_number) + float(second_number)
# use float so that the program takes decimal input too
print("sum: " + str(sum))
# use str() to concatenate string with a string and not two different functions

# program can also be written as:
# first_number = float(input("Enter First Number: "))           used float here
# second_number = float(input("Enter Second Number: "))         used float here
# sum = first_number + second_number                            not here
# print("sum: " + str(sum))
