import random

def roll_dice():
    x = 0
    while x != "":
        x = input("Press enter to roll: ")
    dice_result = random.randrange(1, 7)
    print(f"Your roll: {dice_result}")
    return dice_result


def get_user_input():
    user_input = input("What do you choose: 1 - Yes, 2 - No: ")
    return user_input


def get_basic_skills_values():
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
    return lines[startline-1]


def add_statpoint(skill):
    # here we have to write a statpoint modifier
    print(f"Nice job! Your {skill} is grown by 1.")


def modifying(number_of_chapter, user_answer):
    if number_of_chapter == 1 and user_answer == "1":
        print("You are a nice person")
        # add_statpoint(skill)
    elif number_of_chapter == 2 and user_answer == "2":
        # add_statpoint(skill)
        pass


def start_chapter(number_of_chapter, stagedata_dictonary):
    startline = (stagedata_dictonary.get(number_of_chapter)[0]) 
    startline_choice = (stagedata_dictonary.get(number_of_chapter)[1])
    print("\n")
    print(story_turn_page("story.txt", number_of_chapter))
    user_answer = get_user_input()

    if user_answer == "1":
        story_turn_page("story.txt", startline_choice)
        modifying(number_of_chapter, user_answer)
    elif user_answer == "2":
        story_turn_page("story.txt", startline_choice)
        modifying(number_of_chapter)

def start_game():
    stages = {1 : (1, 2),
        2 : (3, 4),
        3: ("startline", "start_of_choice")}
    story_turn_page("story.txt", 1)
    for stage_number in stages.keys():
        start_chapter(stage_number, stages)

get_basic_skills_values()
start_game()