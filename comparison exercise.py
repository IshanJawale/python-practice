# if name has less than 3 characters print name must have atleast 3 characters
# if name has more than 50 chracters print name can be a maximum of 50 characters
# otherwise print looks good

name = input("Enter you're name: ")
if len(name) < 3:
    print("Name must have atleast 3 characters.")
elif len(name) >= 50:
    print("Name can have maximum 50 characters.")
else:
    print("You're name looks good!")
