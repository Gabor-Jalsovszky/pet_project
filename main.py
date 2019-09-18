import random


def roll_dice():
    dice_result = random.randrange(1, 7)
    print(f"Your roll: {dice_result}")
    return dice_result


def mainmenu():  
    mainmenu = open("mainmenu.txt", "r")
    print(mainmenu.read())


def print_skills():
    skills_open = open("skills.txt", "r")
    skills = skills_open.readlines()
    skills_open.close()
    print("".join(skills))
    return skills


def main():
    print_skills()

if __name__ == "__main__":
    main()
