import random

def roll_dice():
    dice_result = random.randrange(1, 7)
    print(f"Your roll: {dice_result}")
    return dice_result

def main():
    Programming_skills = 1
    roll_dice()

main()
