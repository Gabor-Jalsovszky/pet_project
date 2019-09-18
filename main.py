import random


def set_basic_skills():
    update_stamina = roll_dice()
    update_team_spirit = roll_dice()


def import_basic_skills():
    skills = "skills.txt"
    basic_skills = open(skills, "r")
    return basic_skills
    basic_skills.close()


def roll_dice():
    dice_result = random.randrange(1, 7)
    print(f"Your roll: {dice_result}")
    return dice_result


def mainmenu():
    mainmenu = open("mainmenu.txt", "r")
    print(mainmenu.read())


def get_basic_skills_values(basic_skills_file):
    starting_skillset = basic_skills_file.readlines()
    print(starting_skillset)
    for item in starting_skillset:
        skillset_to_split = (starting_skillset[item]).split(':')
    skill_values = []
    item_counter = -1
    index_of_stamina = 1
    index_of_programming_skills = 3
    index_of_team_spirit = 5
    for item in skillset_to_split:
        item_counter += 1
        if item_counter == index_of_stamina or item_counter == index_of_programming_skills or item_counter == index_of_team_spirit:
            skill_values.append(item)
    return skill_values


def main():
    Programming_skills = 1
    start = mainmenu()
    print(start)
    basic_skills = import_basic_skills()
    basic_skill_vaues_list = get_basic_skills_values(basic_skills)


def print_skills():
    skills_open = open("skills.txt", "r")
    skills = skills_open.readlines()
    skills_open.close()
    print("".join(skills))
    return skills


if __name__ == "__main__":
    main()
