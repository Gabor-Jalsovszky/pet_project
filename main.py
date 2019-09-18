import random

def roll_dice():
    dice_result = random.randrange(1, 7)
    print(f"Your roll: {dice_result}")
    return dice_result

def mainmenu():  
    mainmenu = open("mainmenu.txt", "r")
    return mainmenu.read()


def main():
    Programming_skills = 1
    start = mainmenu()
    print(start)

main()
