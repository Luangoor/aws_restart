import random

print("Guess the number:")
print("I'll think of a number and you will try to guess it")
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print(f"You guessed {guess}. That's correct!")
        isGuessRight = True
    else:
        print(f"You guessed {guess}. Sorry, that's wrong. Try again.")