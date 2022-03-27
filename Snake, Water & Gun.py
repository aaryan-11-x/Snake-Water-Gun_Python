import random
from os import system, name
from time import sleep


def result(player, computer, nam):
    """Prints The Final Result"""
    print("Final Result:-")
    if player > computer:
        print("Congrats", nam, "You Have Won This Game!")
    elif computer > player:
        print("Oops, You Have Lost This Game, Try Again Later!")
    elif player == computer:
        print("It's a Draw!")


nam = input("Enter Your Name : ")
nam = nam.capitalize()
print('''Following are the rules of the game:
Name Of The Game : Snake, Water And Gun

Snake vs. Water: Snake drinks the water hence wins.
Water vs. Gun: The gun will drown in water, hence a point for water
Gun vs. Snake: Gun will kill the snake and win.
In situations where both players choose the same object, the result will be a draw.

For Snake Press : 1 / "Snake" / "s"
For Water Press : 2 / "Water" / "w"
For Gun Press : 3 / "Gun" / "g"''')

rounds = int(input("Enter The Number Of Rounds You Want To Play : "))
opt = ["Snake", "Water", "Gun"]
player = 0
computer = 0
for x in range(1, rounds + 1):
    print()
    print(f"Round {x} Begins In 3.....2....1...")
    sleep(3)
    while 1:
        cho = input("Enter Your Choice : ")
        cho = cho.capitalize()
        cpu = random.choice(opt)

        if cho == "Snake" or cho == "S" or cho == "1":
            print(f"{nam} Selected : Snake")
            break
        elif cho == "Water" or cho == "W" or cho == "2":
            print(f"{nam} Selected : Water")
            break
        elif cho == "Gun" or cho == "G" or cho == "3":
            print(f"{nam} Selected : Gun")
            break
        else:
            print("You Have Entered The Wrong Character/Number, Try Again")
            continue

    if cpu == "Snake":
        print("CPU Selected : Snake")
    elif cpu == "Water":
        print("CPU Selected : Water")
    elif cpu == "Gun":
        print("CPU Selected : Gun")

    if cho == "Snake" or cho == "S" or cho == "1":
        if cpu == "Snake":
            print(f"Round {x} Result : Draw")
        elif cpu == "Water":
            player += 1
            print(f"Round {x} Result : {nam} Wins")
        elif cpu == "Gun":
            computer += 1
            print(f"Round {x} Result : CPU Wins")
    elif cho == "Water" or cho == "W" or cho == "2":
        print(f"{nam} Selected : Water")
        if cpu == "Water":
            print(f"Round {x} Result : Draw")
        elif cpu == "Snake":
            computer += 1
            print(f"Round {x} Result : CPU Wins")
        elif cpu == "Gun":
            player += 1
            print(f"Round {x} Result : {nam} Wins")
    elif cho == "Gun" or cho == "G" or cho == "3":
        print(f"{nam} Selected : Gun")
        if cpu == "Snake":
            player += 1
            print(f"Round {x} Result : {nam} Wins")
        elif cpu == "Water":
            computer += 1
            print(f"Round {x} Result : CPU Wins")
        elif cpu == "Gun":
            print(f"Round {x} Result : Draw")

print()
# print(result.__doc__)
result(player, computer, nam)