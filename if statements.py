temperature = input("Enter the temperature: ")

if float(temperature) > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif float(temperature) > 20:  # (20,30]
    print("It's a nice day")
elif float(temperature) > 10:
    print("It's a bit cold")  # (10,20]
else:
    # this code is executed if none of the above conditions are true
    print("It's a cold day.")
print("done")
