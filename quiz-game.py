print("Welcome to the quiz game!")

playing = input("Do you want to play? (yes/no)")

if playing.lower() != "yes":
    quit()

print("Great! Let's Play :)")

score = 0

answer = input("What is the capital of India? : ")
if answer.lower() == "new delhi":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the scientific name of the northern lights? : ")
if answer.lower() == "aurora borealis":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the largest mammal in the world? : ")
if answer.lower() == "blue whale":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the largest planet in our solar system? : ")
if answer.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What type of whale is actually a dolphin? : ")
if answer.lower() == "orca":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")


print(f"You got {str(score)} questions correct!")
print(f"You got {str((score / 5) * 100)}%.")
