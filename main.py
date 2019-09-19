import random


def roll_dice():
    x = 0
    while x != "":
        x = input("Press enter to roll: ")
    dice_result = random.randrange(1, 7)
    print(f"Your roll: {dice_result}")
    return dice_result


def get_basic_skill_values():
    print("\nYour starting Programming skills is 1. Don't worry, it gets better with practice!\n")
    print("To set your starting Stamina, you have to roll twice. We will add 12 to your result.\n")
    first_roll = roll_dice()
    second_roll = roll_dice()
    starting_stamina = first_roll + second_roll + 12
    print(f"\nYour starting Stamina is {starting_stamina}.\n")
    print("To set your starting Team spirit, you have to roll once.\n")
    team_spirit_roll = roll_dice()
    starting_team_spirit = team_spirit_roll
    print(f"\nYour starting Team spirit is {starting_team_spirit}.")
    file = open("skills.txt", "w")
    file.write(f"Programming skills: 1\n")
    file.write(f"Stamina: {starting_stamina}\n")
    file.write(f"Team spirit: {starting_team_spirit}\n")


def story_turn_page(filename, startline):
    file = open(filename, "r")
    lines = file.readlines()
    return lines[startline - 1]


def main():
    get_basic_skill_values()


def print_skills():
    skills_open = open("skills.txt", "r")
    skills = skills_open.readlines()
    skills_open.close()
    print("".join(skills))
    return skills

def other_options():
    print(print_skills())
    print("To do a dojo excercise, press 1.")
    print("To start working on a project, press 2.")
    print("To try passing the Progbasics PA, press 3.")
    user_input = input("Enter 1, 2 or 3: ")
    return user_input

def get_user_input():
    print(print_skills())
    print("If your answer is yes, press 1.")
    print("If your answer is no, press 2.")
    print("For other options, press 3.")
    user_input = input("Enter 1, 2 or 3: ")
    return user_input


if __name__ == "__main__":
    main()
