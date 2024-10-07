# first_name and last_name are the parameter of the function greet_user
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome aboard")


print("Start")
# we get two outputs for both names by using only one function
greet_user("Ishan", "Jawale")
# argument is the actual information that we supply to these functions
greet_user("John", "Smith")
print("Finish")
