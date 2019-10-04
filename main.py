import random
import os
import time
import sys
import getch
from playsound import playsound

def get_other_options_input():
    invalid_input = True
    valid_inputs = ["1", "2", "3"]
    while invalid_input:
        user_input = input("Enter 1, 2 or 3: ")
        if user_input in valid_inputs:
            invalid_input = False
        else: delay_print("You can choose only from 1, 2 or 3")
    return user_input

def modifying_chapter1(number_of_stage, user_answer, skillset):
    if user_answer == "1":
        skillset = modify_statpoint("Team spirit", 1, 1, skillset)
    elif user_answer == "2":
        skillset = modify_statpoint("Team spirit", -1, -1, skillset)
    return skillset


def modifying_chapter2(number_of_stage, user_answer, skillset):
    if user_answer == "1":
        skillset = modify_statpoint("Programming skills", 1, 1, skillset)
        skillset = modify_statpoint("Team spirit", 1, 1, skillset)
    elif user_answer == "2":
        skillset = modify_statpoint("Programming skills", -1, -1, skillset)
    return skillset


def modifying_chapter3(number_of_stage, user_answer, skillset):
    if user_answer == "1":
        skillset = modify_statpoint("Team spirit", 1, 1, skillset)
        skillset = modify_statpoint("Stamina", 1, 1, skillset)
    elif user_answer == "2":
        skillset = modify_statpoint("Team spirit", -1, -1, skillset)
        return skillset


def modifying_chapter4(number_of_stage, user_answer, skillset):
    if user_answer == "1":
        skillset = modify_statpoint("Stamina", 1, 2, skillset)
        skillset = modify_statpoint("Team spirit", 1, 1, skillset)
    elif user_answer == "2":
        delay_print("\nYou missed am awesome opportunity to socialize with other codecoolers and to boost your stamina. :(")
        time.sleep(2)
        skillset = modify_statpoint("Team spirit", -1, -1, skillset)
    return skillset


def modifying_chapter5(number_of_stage, user_answer, skillset):
    if user_answer == "1":
        skillset = modify_statpoint("Programming skills", 1, 1, skillset)
        skillset = modify_statpoint("Team spirit", 1, 1, skillset)
    elif user_answer == "2":
        delay_print("\nPoor you! It was a really great workshop, and you have missed it.")
        time.sleep(2)
    return skillset


def ask_dojo_question():
    clear_screen()
    delay_print("\nYou are doing a string-based dojo. What will print the following expression?")
    delay_print("\n\033[1;37mdojo_word = 'basics'")
    delay_print("print(dojo_word[-5:-2] == dojo_word[1:4])\033[0;37m\n")
    GREEN = '\033[1;32m'
    WHITE = '\033[0;37m'
    RED = '\033[1;31m'
    BLUE = '\033[1;34m'

    delay_print(f"If your answer is {GREEN}True{WHITE}, press{GREEN} 1{WHITE}.")
    delay_print(f"If your answer is {RED}False{WHITE}, press {RED}2{WHITE}.")
    invalid_input = True
    valid_inputs = ["1", "2"]
    while invalid_input:
        user_input = input("Enter 1 or 2: ")
        if user_input in valid_inputs:
            invalid_input = False
        else: delay_print("You can choose only from 1 or 2")
    if user_input == "1":
        return True
    elif user_input == "2":
        return False


def try_pa(skillset):
    skill_check = skills_check(skillset, "Programming skills", 5)
    clear_screen()
    if skill_check == True:
        delay_print("60 minutes is passing by so quickly")
        time.sleep(2)
        clear_screen()
        with open("winning_page.txt") as picture:
            for line in picture:
                print(line, end="")
            playsound('queen.mp3')      
        time.sleep(10)
        exit()
    elif skill_check == False:
        delay_print("60 minutes is passing by so quickly")
        time.sleep(1)
        delay_print("You have tried it, but ... ")
        time.sleep(1)
        delay_print("\033[1;31mYou are not prepared!")
        time.sleep(2)        
        delay_print("Your programming skills are not good enough ...") 
        delay_print("Yet ... Keep working \033[0;37m")
        time.sleep(3)


def do_dojo(skillset):
    stamina_check = skills_check(skillset, "Stamina", 14)
    if stamina_check == True:
        dojo_answer = ask_dojo_question()
        if dojo_answer == True:
            skillset = modify_statpoint("Programming skills", 1, 1, skillset)
            skillset = modify_statpoint("Stamina", -1, -1, skillset)
        elif dojo_answer == False:
            delay_print("\nWrong answer. Never mind, you will be better next time")
            time.sleep(2)
    else:
        delay_print("Your Stamina is too low. Try to increase it (have a coffee", end="")
        delay_print(" or do some excercise) before you do a Dojo!")
        time.sleep(5)
    return skillset


def work_on_project(skillset):
    team_spirit_check = skills_check(skillset, "Team spirit", 1)
    if team_spirit_check == True:
        delay_print("\n\033[1;37mYou seriously rocked this project thing.\033[0;37m")
        skillset = modify_statpoint("Programming skills", 1, 3, skillset)
    else:
        delay_print("\nYou need friends to work on a project!")
        delay_print("Try to be more social to boost your team spirit!")
        time.sleep(4)
    clear_screen()
    return skillset


def print_instuctions(instruction_file):
    clear_screen()
    with open(instruction_file) as picture:
        for line in picture:
            print(line, end = "")
    return_sign = input()
    if return_sign == "":
        printing_menu()
    

def print_welcome_picture(file_to_print):
    print("\033[0;33m")
    with open(file_to_print) as picture:
        for line in picture:
            print(line, end = "")
    print("\033[0;37m\n")


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
        print(f"{i+1}. {element}".center(94))
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
    print("\n\033[0;32m")
    width = 22
    print("/", end="")
    print(f"-"*width, end="")
    print("\\")
    for key, value in skillset.items():
        print(f"|{key}: ", end="")
        print(f"{value}|".rjust(21-len(key)))
    print("\\", end="")
    print(f"-"*width, end="")
    print("/\033[0;37m")


def roll_dice():
    x = 0
    while x != "":
        x = input("Press enter to roll: ")
    dice_result = random.randrange(1, 7)
    print(f"Your roll: {dice_result}")
    time.sleep(1)
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
    time.sleep(2)
    return skillset


def story_turn_page(filename, startline, skillset):
    file = open(filename, "r")
    lines = file.readlines()
    return lines[startline - 1]


def other_options(skillset, number_of_stage, stagedata):
    clear_screen()
    menu_header = "\033[1;32m Quests: \n\033[0;37m" 
    other_options_menu = [menu_header, "To do a dojo excercise, press 1." , "To start working on a project, press 2.", "To try passing the Progbasics PA, press 3."]
    for menu_item in other_options_menu:
        delay_print(menu_item)
    user_input = get_other_options_input()
    if user_input == "1":
        skillset = do_dojo(skillset)
    elif user_input == "2":
        skillset = work_on_project(skillset)
    elif user_input == "3":
        try_pa(skillset)

    start_chapter(number_of_stage + 1, stagedata, skillset)
    return skillset


def get_user_input():
    GREEN = '\033[1;32m'
    WHITE = '\033[0;37m'
    RED = '\033[1;31m'
    CYAN = '\033[1;36m'

    delay_print(f"If your answer is {GREEN}Yes{WHITE}, press{GREEN} 1{WHITE}.")
    delay_print(f"If your answer is {RED}No{WHITE}, press {RED}2{WHITE}.")
    delay_print(f"For other options, press {CYAN}3{WHITE}.")
    invalid_input = True
    valid_inputs = ["1", "2", "3"]
    while invalid_input:
        user_input = input("Enter 1, 2 or 3: ")
        if user_input in valid_inputs:
            invalid_input = False
        else: delay_print("You can choose only from 1, 2 or 3")
    return user_input


def modify_statpoint(skill, modifier, amount, skillset):
    print("\n")
    if modifier == 1:
        skillset[skill] += amount
        delay_print(f"Nice job! Your {skill} will increase by {amount}.\n")
        time.sleep(4)
        clear_screen()
    elif modifier == -1:
        skillset[skill] += amount
        delay_print(f"Your {skill} will decrease by {abs(amount)}.\n")
        time.sleep(4)
        clear_screen()
    return skillset


def modifying(number_of_stage, user_answer, skillset):  
    if number_of_stage == 1:
        modifying_chapter1(number_of_stage, user_answer, skillset)
    elif number_of_stage == 2:
        modifying_chapter2(number_of_stage, user_answer, skillset)
    elif number_of_stage == 3:
        modifying_chapter3(number_of_stage, user_answer, skillset)
    elif number_of_stage == 4:
        modifying_chapter4(number_of_stage, user_answer, skillset)
    elif number_of_stage == 5:
        modifying_chapter5(number_of_stage, user_answer, skillset)
    return skillset


def start_chapter(number_of_stage, stagedata, skillset):
    startline = (stagedata[number_of_stage - 1]) 
    clear_screen()
    show_stats(skillset)
    print("\n")
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
    stages = [1, 2, 3, 4, 5, 6]
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
