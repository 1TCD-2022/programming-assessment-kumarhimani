"""
Filename: True or False Quiz
Author: Himani Kumar
Date:2/08/22
Description: A true or false quiz about a range of topics for college kids, year 9 to year 13
"""

import random

#Variables that will be used
VALID_USER_CHOICE =["1","2","3","4"]
user_choice = []
user_choice = VALID_USER_CHOICE
score = 0
VALID_USER_CHOICE = []

#List of questions
SCIENCE_QUESTIONS = ["The skin is the largest organ",
                     "There are 10 planets in our universe]",
                     "FE is the symbol for Iron"]


ANIMAL_QUESTIONS = ["An octopus has four hearts",
                    "The world's largest animal is a blue whale",
                    "Lions have the strongest bite"]


WORLD_QUESTIONS = ["There are 55 states in the United States",
                   "There are 189 countries in the world",
                   "Scotland's national animal is the unicorn"]
   
#Answers to questions
SCIENCE_ANSWERS = ["T","F","T"]
ANIMAL_ANSWERS =["F","T","F" ]
WORLD_ANSWERS = ["F","F","T"]



#Menu
print("""welcome to my true or false quiz!!!
        1.Science - 3 questions
        2.Animals - 3 questions
        3.World - 3 questions
        4.Exit Program/n""")


user_choice = input("please enter a number from 1-4 according to what topic you would like to be quizzed on. Answer with T OR F")

if user_choice == "1":
    print("You have entered 1.")
    for i in range(len(SCIENCE_QUESTIONS)):
        science_questions = random.choice(SCIENCE_QUESTIONS)
        science_questions = SCIENCE_QUESTIONS[i]
        answer = SCIENCE_ANSWERS[i]
        print(science_questions)
        user_answer = input("[T/F]: ")

        if user_answer == SCIENCE_ANSWERS[SCIENCE_QUESTIONS.index(science_questions)]:
            print("CORRECT")
        else:
            print("Wrong")

elif user_choice == "2":
    print("You have entered 2.")
    for i in range(len(ANIMAL_QUESTIONS)):
        animal_questions = random.choice(ANIMAL_QUESTIONS)
        animal_questions = ANIMAL_QUESTIONS[i]
        answer = ANIMAL_ANSWERS[i]
        print(animal_questions)
        user_answer = input("[T/F]: ")

        if user_answer == ANIMAL_ANSWERS[ANIMAL_QUESTIONS.index(animal_questions)]:
            print("That's correct")
        else:
            print("Sorry that's wrong")

elif user_choice == "3":
    print("You have entered 2.")
    for i in range(len(WORLD_QUESTIONS)):
        animal_questions = random.choice(WORLD_QUESTIONS)
        world_questions = WORLD_QUESTIONS[i]
        answer = WORLD_ANSWERS[i]
        print(world_questions)
        user_answer = input("[T/F]: ")

        if user_answer == WORLD_ANSWERS[WORLD_QUESTIONS.index(world_questions)]:
            print("Thats right")
        else:
            print("Wrong")

elif user_choice == "4":
    print("okay bye :)")

