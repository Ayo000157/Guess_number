import random

def guess_number():
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 20...")

    # Computer chooses a random number
    secret_number = random.randint(1, 20)

 
if guess < secret_number:
            print("Too low! 📉")
elif guess > secret_number:
            print("Too high! 📈")
else:
            print(Congratulations! You guessed it correctly .")
break
    else:
        print(“Sorry, you didn't guess it correctly”)
