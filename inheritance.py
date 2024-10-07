class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):       # Mammal is the parent class which is inherited to avoid repetation of code
    def bark(self):        # this method is specific to Dog class
        print("Bark")     


class Cat(Mammal):
    pass                 # a class cannot be empty that's why we write pass to pass the code


dog1 = Dog()
dog1.walk()
dog1.bark()
