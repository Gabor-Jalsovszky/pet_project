def get_user_input():
    user_input = input("What do you choose: 1 - Yes, 2 - No: ")
    return user_input

def print_story(startline, endline):
    pass

def add_statpoint(skill):
    # here we have to write a statpoint modifier
    print(f"Nice job! Your {skill} is grown by 1.")

def modifying(number_of_chapter, user_answer):
    if number_of_chapter == 1 and user_answer == 1:
        add_statpoint(skill)
    elif number_of_chapter == 2 and user_answer == 2:
        add_statpoint(skill)


def start_chapter(number_of_chapter, storydata_dictonary):
    startline = (storydata_dictonary.get(number_of_chapter)[0]) 
    endline = (storydata_dictonary.get(number_of_chapter)[1])
    startline_choice = (storydata_dictonary.get(number_of_chapter)[3])
    endline_choice = (storydata_dictonary.get(number_of_chapter)[4])
    user_answer = get_user_input()
    if user_answer == 1:
        print_story(startline_choice, endline_choice)
        modifying(number_of_chapter, user_answer)
    elif user_answer == 2:
    
    



def start_game():
    stages = {1 : [1, 2, "start_of_choice_one", "start_of choice_two"],
        2 : ("storystart", "storyend", "start_of_choice_one", "start_of choice_two")}

    for stage_number in stages.keys():
        start_chapter(stage_number, stages)



start_game()