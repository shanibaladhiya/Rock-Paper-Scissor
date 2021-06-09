import random
roundofGame = 1
CompWin = 0
PlyrWin = 0
Tied = 0
com = ["R", "P", "S"]
while roundofGame <= 10:
    print("-------************--------")
    print("-------************--------\n")
    print("Computer's Turn:")
    print("Enter Rock(R) Paper(P) Scissor(S)")
    computer = random.choice(com)
    print("Computer has choosen !!!")
    print("Player's Turn:")
    plyr = input("Enter Rock(R) Paper(P) Scissor(S)\n")
    print(f"Computer entered {computer}")
    print(f"Player entered {plyr}")
    if plyr == "R":
        if computer == "R":
            print("Tie !!!\n")
            Tied = Tied + 1
        elif computer == "P":
            print("Computer Win !!!\n")
            CompWin = CompWin + 1
        else:
            print("Player Win !!!\n")
            PlyrWin = PlyrWin + 1
    elif plyr == "P":
        if computer == "R":
            print("Player Win !!!\n")
            PlyrWin = PlyrWin + 1
        elif computer == "P":
            print("Tie !!!\n")
            Tied = Tied + 1
        else:
            print("Computer Win !!!\n")
            CompWin = CompWin + 1
    elif plyr == "S":
        if computer == "R":
            print("Computer Win !!!\n")
            CompWin = CompWin + 1
        elif computer == "P":
            print("Player Win !!!\n")
            PlyrWin = PlyrWin + 1
        else:
            print("Tie !!!\n")
            Tied = Tied + 1
    else:
        print("Enter valid....")
    roundofGame = roundofGame + 1
print("---------------------------")
print("---------------------------")
print(f"Computer Win {CompWin} times")
print(f"Player win {PlyrWin} times")
print(f"Tie {Tied} times")
print("---------------------------")
print("---------------------------")
print("Game Over")
print("---------------------------")
print("---------------------------")
