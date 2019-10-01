import random
import os
import time
import sys
import getch

def try_pa(skillset):
    skill_check = skills_check(skillset, "Programming skills", 2)
    clear_screen()
    if skill_check == True:
        with open("winning_page.txt") as picture:
            for line in picture:
                print(line, end="")
        time.sleep(5)
        exit()
    elif skill_check == False:
        delay_print("\033[11;31mYou are not prepared\033[0;37m")
        time.sleep(2)


def print_instuctions(instruction_file):
    clear_screen()
    with open(instruction_file) as picture:
        for line in picture:
            print(line, end = "")
    return_sign = input()
    if return_sign == "":
        printing_menu()
    

def print_welcome_picture(file_to_print):
    with open(file_to_print) as picture:
        for line in picture:
            print(line, end = "")
    print("\n")


def get_menu_input():
    menu_input = getch.getch()
    if menu_input == "1":
        return
    elif menu_input == "2":
        print_instuctions("instructions.txt")
    

def printing_menu():
    clear_screen()
    print_welcome_picture("welcome_page.txt")
    menu_options = ["Start game", "Instructions"]
    for i, element in enumerate(menu_options):
        print(f"{i+1}. {element}".center(75))
    get_menu_input()
    clear_screen()
    

def clear_screen():
    os.system('clear')

def delay_print(string_to_print):
    for character in string_to_print:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.015)
    print("\n")

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

    delay_print("\nYour starting Programming skills is 1. Don't worry, it gets better with practice!\n")
    delay_print("To set your starting Stamina, you have to roll twice. We will add 12 to your result.\n")
    first_roll = roll_dice()
    second_roll = roll_dice()
    starting_stamina = first_roll + second_roll + 12
    delay_print(f"\nYour starting Stamina is {starting_stamina}.\n")
    delay_print("To set your starting Team spirit, you have to roll once.\n")
    team_spirit_roll = roll_dice()
    starting_team_spirit = team_spirit_roll
    skillset = {"Programming skills" : 1, "Stamina" : starting_stamina, "Team spirit" : starting_team_spirit}
    show_stats(skillset)
    time.sleep(5)
    return skillset


def story_turn_page(filename, startline, skillset):
    file = open(filename, "r")
    lines = file.readlines()
    return lines[startline - 1]


def other_options(skillset, number_of_stage, stagedata):
    clear_screen()
    delay_print("To do a dojo excercise, press 1.")
    delay_print("To start working on a project, press 2.")
    delay_print("To try passing the Progbasics PA, press 3.")
    user_input = input("Enter 1, 2, 3 or 4: ")
    if user_input == "1":
        stamina_check = skills_check(skillset, "Stamina", 14)
        if stamina_check == True:
            skillset = modify_statpoint("Programming skills", 1, 1, skillset)
            skillset = modify_statpoint("Stamina", -1, -1, skillset)
        else:
            delay_print("Your Stamina is too low. Try to increase it (have a coffee", end="")
            delay_print(" or do some excercise) before you do a Dojo!")
            time.sleep(5)
    elif user_input == "2":
        team_spirit_check = skills_check(skillset, "Team spirit", 1)
        if team_spirit_check == True:
            skillset = modify_statpoint("Programming skills", 1, 3, skillset)
    clear_screen()
            skillset = modify_statpoint("Programming skills", 1, skillset)
            skillset = modify_statpoint("Stamina", -1, skillset)
        else:
            print("\033[1;31mYou are not prepared\033[0;37m")
        clear_screen()
    if user_input == "3":
        try_pa(skillset)

    start_chapter(number_of_stage, stagedata, skillset)
    return skillset


def get_user_input():
    GREEN = '\033[0;32m'
    WHITE = '\033[0;37m'
    RED = '\033[0;31m'
    CYAN = '\033[0;36m'

    delay_print(f"If your answer is {GREEN}Yes{WHITE}, press{GREEN} 1{WHITE}.")
    delay_print(f"If your answer is {RED}No{WHITE}, press {RED}2{WHITE}.")
    delay_print(f"For other options, press {CYAN}3{WHITE}.")
    user_input = input("Enter 1, 2 or 3: ")
    return user_input


def modify_statpoint(skill, modifier, amount, skillset):
    print("\n")
    if modifier == 1:
        skillset[skill] += amount
        delay_print(f"Nice job! Your {skill} will increase by {amount}.\n")
        time.sleep(4)
        clear_screen()
    elif modifier == -1:
        skillset[skill] -= amount
        delay_print(f"That's not very nice. Your {skill} will decrease by {amount}.\n")
        time.sleep(4)
        clear_screen()
    show_stats(skillset)
    time.sleep(1)
    return skillset


def modifying(number_of_stage, user_answer, skillset):
    if number_of_stage == 1 and user_answer == "1":
        skillset = modify_statpoint("Team spirit", 1, 1, skillset)
    elif number_of_stage == 1 and user_answer == "2":
        skillset = modify_statpoint("Team spirit", -1, -1, skillset)
    if number_of_stage == 2 and user_answer == "1":
        skillset = modify_statpoint("Programming skills", 1, 1, skillset)
    elif number_of_stage == 2 and user_answer == "2":
        skillset = modify_statpoint("Programming skills", -1, -1, skillset)
    if number_of_stage == 3 and user_answer == "1":
        skillset = modify_statpoint("Team spirit", 1, 1, skillset)
        skillset = modify_statpoint("Stamina", 1, 1, skillset)
    elif number_of_stage == 3 and user_answer == "2":
        skillset = modify_statpoint("Team spirit", -1, -1, skillset)
    if number_of_stage == 4 and user_answer == "1":
        skillset = modify_statpoint("Programming skills", 1, 1, skillset)
    elif number_of_stage == 4 and user_answer == "2":
        print(f"You should have shaprened your skills in Python!")
    return skillset


def start_chapter(number_of_stage, stagedata, skillset):
    startline = (stagedata[number_of_stage - 1]) 
    print("\n")
    clear_screen()
    delay_print(story_turn_page("story.txt", number_of_stage, skillset))
    user_answer = get_user_input()
    time.sleep(1)

    if user_answer == "1":
        skillset = modifying(number_of_stage, user_answer, skillset)
    elif user_answer == "2":
        skillset = modifying(number_of_stage, user_answer, skillset)
    elif user_answer == "3":
        skillset = other_options(skillset, number_of_stage, stagedata)
    return skillset


def start_game(skillset):
    stages = [1, 2, 3, 4]
    story_turn_page("story.txt", 1, skillset)
    for stage_number in stages:
        skillset = start_chapter(stage_number, stages, skillset)
    return skillset


def skills_check(skillset, required_skill, required_min_skill):
    if skillset[required_skill] >= required_min_skill:
        return True
    elif skillset[required_skill] < required_min_skill:
        return False


def main():
    printing_menu()
    player_skillset = get_basic_skill_values()
    clear_screen()
    player_skillset = start_game(player_skillset)


if __name__ == "__main__":
    main()
