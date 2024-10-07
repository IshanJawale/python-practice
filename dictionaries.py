# dictionaries are an unordered collection of data values, used to store data values like a map
customer = {
    "Name": "Ishan Jawale",
    "Age": 18,  # key value is unique; there cannot be two age values
    "is_verified": True
}
# key is case sensitive, will show an error if entered "name" now
print(customer["Name"])
# the get method gives output as none if the entered key value is nonexistant or in the wrong case
print(customer.get("name"))
# this suplies a default value
print(customer.get("Birthdate", "March 16,2004"))
customer["Name"] = "John Smith"  # changes the value of "Name"
print(customer["Name"])
customer["E-mail"] = "xyz@gmail.com"  # to add a new key
print(customer["E-mail"])
