height = float(input("Enter your height (in cms): "))
weight = float(input("Enter your weight (in kgs): "))
BMI = (weight / (height/100)**2)
print("BMI = " + str(BMI))
if BMI < 16:
    print("You're underweight (severe).")
elif BMI >= 16 and BMI < 16.9:
    print("You're underweight (moderate).")
elif BMI >= 17 and BMI < 18.4:
    print("You're underweight (mild) ")
elif BMI >= 18.5 and BMI < 24.9:
    print("You're healthy.")
elif BMI >= 25 and BMI < 29.9:
    print("You're overweight.")
elif BMI >= 30 and BMI < 34.9:
    print("You're Obese (Class I)")
elif BMI >= 35 and BMI < 39.9:
    print("You're Obese (Class II)")
else:
    print("You're Obese (Class III)")
print("NOTE - The range of BMI of a healthy person is 18.5 to 24.9")
