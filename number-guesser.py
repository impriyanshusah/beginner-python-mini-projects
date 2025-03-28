import random

print("Welcome to the Number Guesser Game!")

playing = input("Do you want to play? (yes/no) : ")
if playing.lower() != "yes":
    quit()

print("Great! Let's play!")
print(
    "\nYou need to select a range of numbers\nAnd then try to guess the random number\nThat the computer has chosen within 3 guesses.\n"
)


while True:
    topRange = input("Enter the top of the range: ")

    if topRange.isdigit():
        topRange = int(topRange)

        if topRange <= 0:
            print("\nPlease enter a number greater than 0")
            continue
        else:
            break

    else:
        print("\nPlease enter a number")
        continue


randomNumber = random.randint(0, topRange)
guesses = 0

while guesses < 3:
    guesses += 1
    userGuess = input("\nMake a guess: ")
    if userGuess.isdigit():
        userGuess = int(userGuess)
    else:
        print("\nPlease enter a number next time.")
        continue

    if userGuess == randomNumber:
        print(f"\nCongratulations! You guessed the correct number in {guesses} guesses!")
        break
    elif userGuess > randomNumber:
        print("\nGuess lower")
    else:
        print("\nGuess higher")

if guesses >= 3:
    print(f"\nSorry! You did not guess the correct number within 3 chances. The number was {randomNumber}")

print("\nThanks for playing!")
