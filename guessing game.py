# game of guessing a number where you've three chances to guess the correct number
print("Guess the correct one digit number:-")
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Your Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:  # this else is for the while loop
    print("Sorry, you failed!")
