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
    skillset = {"Programming skills" : 1, "Stamina" : starting_stamina, "Team spirit" : starting_team_spirit}
    # file = open("skills.txt", "w")
    # file.write(f"Programming skills: 1\t\tStamina: {starting_stamina}\t\t\tTeam spirit: {starting_team_spirit}\n")
    # file.close()
    return skillset

def story_turn_page(filename, startline):
    file = open(filename, "r")
    lines = file.readlines()
    return lines[startline - 1]


def print_skills():
    skills_open = open("skills.txt", "r")
    skills = skills_open.read()
    skills_open.close()
    return skills


def other_options():
    print("To do a dojo excercise, press 1.")
    print("To start working on a project, press 2.")
    print("To try passing the Progbasics PA, press 3.")
    user_input = input("Enter 1, 2 or 3: ")
    return user_input


def get_user_input():
    print("If your answer is yes, press 1.")
    print("If your answer is no, press 2.")
    print("For other options, press 3.")
    user_input = input("Enter 1, 2 or 3: ")
    return user_input


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


def main():
    player_skillset = get_basic_skill_values()
    start_game()

if __name__ == "__main__":
    main()