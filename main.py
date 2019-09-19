import random
import os
import time


clear = lambda: os.system('clear')


def show_stats(skillset):
    for key, value in skillset.items():
        print(str(key) + ": " + str(value))


def roll_dice():
    x = 0
    while x != "":
        x = input("Press enter to roll: ")
    dice_result = random.randrange(1, 7)
    print(f"Your roll: {dice_result}")
    time.sleep(2)
    return dice_result


def get_basic_skill_values():
    print("\nYour starting Programming skills is 1. Don't worry, it gets better with practice!\n")
    print("To set your starting Stamina, you have to roll twice. We will add 12 to your result.\n")
    first_roll = roll_dice()
    clear()
    second_roll = roll_dice()
    clear()
    starting_stamina = first_roll + second_roll + 12
    print(f"\nYour starting Stamina is {starting_stamina}.\n")
    print("To set your starting Team spirit, you have to roll once.\n")
    team_spirit_roll = roll_dice()
    clear()
    starting_team_spirit = team_spirit_roll
    skillset = {"Programming skills" : 1, "Stamina" : starting_stamina, "Team spirit" : starting_team_spirit}
    show_stats(skillset)
    time.sleep(5)
    return skillset


def story_turn_page(filename, startline, skillset):
    file = open(filename, "r")
    lines = file.readlines()
    return lines[startline - 1]


def other_options():
    print("To do a dojo excercise, press 1.")
    print("To start working on a project, press 2.")
    print("To try passing the Progbasics PA, press 3.")
    print("To check your skillset, press 4.")
    user_input = input("Enter 1, 2, 3 or 4: ")
    return user_input


def get_user_input():
    print("If your answer is yes, press 1.")
    print("If your answer is no, press 2.")
    print("For other options, press 3.")
    user_input = input("Enter 1, 2 or 3: ")
    return user_input


def modify_statpoint(skill, modifier, skillset):
    print("\n")
    if modifier == 1:
        skillset[skill] += 1
        print(f"Nice job! Your {skill} has grown by 1.\n")
        time.sleep(4)
        clear()
    elif modifier == -1:
        skillset[skill] -= 1
        print(f"That's not very nice. Your {skill} has decreased by 1.\n")
        time.sleep(4)
        clear()
    show_stats(skillset)
    return skillset


def modifying(number_of_stage, user_answer, skillset):
    if number_of_stage == 1 and user_answer == "1":
        skillset = modify_statpoint("Team spirit", 1, skillset)
    elif number_of_stage == 1 and user_answer == "2":
        skillset = modify_statpoint("Team spirit", -1, skillset)
    if number_of_stage == 2 and user_answer == "1":
        skillset = modify_statpoint("Programming skills", 1, skillset)
    elif number_of_stage == 2 and user_answer == "2":
        skillset = modify_statpoint("Programming skills", -1, skillset)
    return skillset


def start_chapter(number_of_stage, stagedata_dictonary, skillset):
    startline = (stagedata_dictonary.get(number_of_stage)[0]) 
    print("\n")
    print(story_turn_page("story.txt", number_of_stage, skillset))
    user_answer = get_user_input()
    time.sleep(1)

    if user_answer == "1":
        skillset = modifying(number_of_stage, user_answer, skillset)
    elif user_answer == "2":
        skillset = modifying(number_of_stage, user_answer, skillset)
    return skillset


def start_game(skillset):
    stages = {1 : (1, 2),
        2 : (3, 4),
        3: ("startline", "start_of_choice")}
    story_turn_page("story.txt", 1, skillset)
    for stage_number in stages.keys():
        skillset = start_chapter(stage_number, stages, skillset)
    return skillset


def main():
    player_skillset = get_basic_skill_values()
    clear()
    player_skillset = start_game(player_skillset)


if __name__ == "__main__":
    main()
