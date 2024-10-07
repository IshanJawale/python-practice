# age = int(input("Age: "))
# print(age)
# now if you enter any numerical integer value then the program will run
# but if you enter letters like 'asd', then the program will crash
# so we have to print a proper error message to prevent the program from crashing if the user enters wrong input
# Exception is a kind of error which crashes a program
try:                               # try tells the python interprator to execute the program while except indicates the type of error it might face and what to do when it does
    # so if the user enters an invalid value then this line will raise an exception and except function will catch the error and print the error message
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:          # since the denaminator cannot be zero, it shows ZeroDivisionError; therefore use multiple exceptions
    print('Age cannot be zero')
except ValueError:                 # ValueError is an error which indicates invalid input in the program
    print('Invalid Value')
