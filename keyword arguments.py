def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
greet_user(last_name = "Jawale", first_name = "Ishan" ) # this is keyword arguments; this will print Ishan Jawale irrespective of the postion in which they are written
greet_user("John", "Smith")                            # this is positional arguments; avoid using for numerical values; this cannot be written as "Smith", "John" as it will print it in the same order
print("Finish")





