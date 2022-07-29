"""
Filename: True Or False Quiz
Author: Himani Kumar
Date: 6/07/22
Description: A true or false quiz about a range of topics for college kids, year 9 to year 13
"""

#List of questions for true or false quiz
SCIENCE_QUESTIONS = ["The skin the largest organ","There are 10 planets in the world","F is the symbol for Iron"]
ANIMALS_QUESTIONS = ["An octopus has four hearts", "The worlds largest animal is a blue whale", "Lions have the strongest bite"]
WORLD_QUESTIONS = ["there are 55 states in the United States","There are 89 countries in the world","Scotlands national animal is a Unicorn"]

#Answers to true or false questions
SCIENCE_ANSWERS = ["T","F","T"]
ANIMALS_ANSWERS = ["F", "T", "F"]
WORLD_ANSWERS = ["F", "F", "T"]

VALID_USER_CHOICE = ["1", "2", "3", "4"]
user_menu_choice = []
users_menu_choice = VALID_USER_CHOICE

#Menu
print("""welcome to the true or false quiz!!!
        1.Science - 3 questions about Science
        2.Animals - 3 questions about animals
        3.World - 3 questions about the world
        4.Exit Program/n""")

user_menu_choice = input( "please enter a number from 1-4" )

if user_menu_choice!=VALID_USER_CHOICE:
        print("please enter a number from the given options")

if user_menu_choice == "5":
        print("okay bye :)")

elif user_menu_choice == "1":
        print("please answer T or F for each of these questions")
        print(SCIENCE_QUESTIONS)
user_menu_choice =input("please enter T OR F for each of these questions")
        
if user_menu_choice == "2":
        print("please answer T or F for each of these questions")
        print(ANIMALS_QUESTIONS)
user_menu_choice =input("please enter T OR F for each of these questions")
        
if user_menu_choice =="3":
        print("please answer T or F for each of these questions")
        print(WORLD_QUESTIONS)
user_menu_choice =input("please enter T OR F for each of these questions")




            
