"""
Filename: True or False Quiz
Auhtor: Himani Kumar
Date:2/08/22
Description: A true or false quiz about a range of topics for college kids, year 9 to year 13
"""


#Variables that will be used
VALID_USER_CHOICE =["1","2","3","4"]
user_choice = []
user_choice = VALID_USER_CHOICE
score = 0
VALID_USER_CHOICE = []

#List of questions
SCIENCE_QUESTIONS = ["The skin is the largest ogran",
                     "There are 10 planets in our universe",
                     "F is the symbol for Iron"]


ANIMAL_QUESTIONS = ["An octopus has four hears",
                    "The worlds largest animal is a blue whale",
                    "Lions have the strongest bite"]


WORLD_QUESTIONS = ["There are 55 states in the United States",
                   "There are 89 countries in the world",
                   "Scotlands national animal is the unicorn"]
    
#Answers to questions
SCIENCE_ANSWERS = ["T","F","T"]
ANIMAL_QUESTIONS =[ ]
WORLD_QUESTIONS = [ ]
                   

#Menu
print("""welcome to my true or false quiz!!!
        1.Science - 3 questions
        2.Animals - 3 questions
        3.World - 3 questions
        4.Exit Program/n""")

user_choice = input("please enter a number from 1-4 according to want topic you would like to be quizzed on")

while not user_choice in VALID_USER_CHOICE:
    user_choice = input("please enter a number from 1-4")

if user_choice == "1":
    print[SCIENCE_QUESTIONS] ("The skin is the largest organ on the human body")
    




    
 
