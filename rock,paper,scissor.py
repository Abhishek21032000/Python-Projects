import random

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "s", -1: "w", 0: "g"}

computer = random.choice(list(youDict.values()))

youstr = input("Enter your choice (s, w, g): ")

if youstr not in youDict:
    print("Invalid choice! Please choose 's', 'w', or 'g'.")
else:
    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")
    elif (you == 1 and computer == -1) or (you == -1 and computer == 0) or (you == 0 and computer == 1):
        print("You win!")
    else:
        print("You lose!")
