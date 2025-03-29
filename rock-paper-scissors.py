import random

print("Rock, Paper, Scissors !!!")

userScore = 0
computerScore = 0

while True:
    userInput = input("\nType Rock/Paper/Scissors or Q to Quit: ").lower()
    if userInput == "q":
        quit()

    if userInput not in ["rock", "paper", "scissors"]:
        print("\nInvalid input, Please try again")
        continue

    computerInput = random.choice(["rock", "paper", "scissors"])

    print("\nComputer chose: ", computerInput)

    if computerInput == userInput:
        print("\nIt's a tie!")
    elif computerInput == "rock" and userInput == "scissors":
        print("\nComputer wins!")
        computerScore += 1
    elif computerInput == "paper" and userInput == "rock":
        print("\nComputer wins!")
        computerScore += 1
    elif computerInput == "scissors" and userInput == "paper":
        print("\nComputer wins!")
        computerScore += 1

    else:
        print("\nYou Win!")
        userScore += 1
    print(f"\nYour score: {userScore}")
    print(f"Computer score: {computerScore}")

print("\nThanks for playing!")
