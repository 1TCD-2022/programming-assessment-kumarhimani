"""
Filename: True or False Quiz
Author: Himani Kumar
Date:2/08/22
Description: A true or false quiz about a range of topics for college kids, year 9 to year 13
"""

import random

#Variables that will be used
VALID_USER_CHOICE = ["1", "2", "3", "4"]
user_choice = []
user_choice = VALID_USER_CHOICE
score = 0


#List of questions
print("")
SCIENCE_QUESTIONS = ["The skin is the largest organ" ,
                     "There are 10 planets in our universe" ,
                     "FE is the symbol for Iron" ,
                     "Amygdala is responsible for memory in your brain" ,
                     "Atoms are more stable when they have a full outer shell" ,
                     "Jupiter has more gravity than Earth",
                     "Sound travels faster in water ",                                  
                     "The stomach is the heavist ogran in the body" ,                           
                     "Adult humans have 32 teeth",
                     "Venus is the closest planet to the sun"]
                     


ANIMAL_QUESTIONS = ["An octopus has four hearts",
                    "The world's largest animal is a blue whale",
                    "Lions have the strongest bite",
                    "Bats use echolocation to find prey",
                    "Tigers have over 150 stripes on their skin",
                    "African Elephants are the bigger than Indian Elephants",
                    "Slugs have four noses",
                    "A giraffes toune is pink"
                    "A bat is the only mammal that can fly",
                    "Cobras are the largest snake in the world"]

            


WORLD_QUESTIONS = ["There are 55 states in the United States" ,
                   "There are 189 countries in the world" ,
                   "Scotland's national animal is the unicorn",
                   "The second tallest moutnain in the world is called K2" ,
                   "There are six starts on the Australian Flag",
                   "Hawaii has 132 islands" ,
                   "Europe was named after a Greek Princess",
                   "There are four stars on Chinas flag",
                   "Canada has the most lakes compared to other countries",
                   "There are four countries in the UK"]
                   
                   
   
#Answers to questions
SCIENCE_ANSWERS = ["T","F","T","F","T","T","T","F","T","F"]
ANIMAL_ANSWERS =["F","T","F","T","F","T","T","F","T","F"]
WORLD_ANSWERS = ["F","F","T","T","F","T","T","F","T","T"]
                



#Menu
print("""Welcome to my true or false quiz!!!

        1.Science - 10 questions
        2.Animals - 10 questions
        3.World - 10 questions
        4.Exit Program/n""")

#asking user to enter a number
print("")
user_choice = input("please enter a number from 1-4: ").strip()
while user_choice not in VALID_USER_CHOICE:
    print("Invalid input.")
    user_choice = input("enter a number from the given options: ")

                 
        
        

#asking user questions
if user_choice == "1":
    print("You have entered 1.")
    for i in range(len(SCIENCE_QUESTIONS)):
        science_questions = random.choice(SCIENCE_QUESTIONS)
        science_questions = SCIENCE_QUESTIONS[i]
        answer = SCIENCE_ANSWERS[i]
        print(science_questions)
        user_answer = input("[Answer with T or F]: ")

        if user_answer == SCIENCE_ANSWERS[SCIENCE_QUESTIONS.index(science_questions)]:
            #scores
            score = score + 1
            print(score)
            print("Correct!")
        else:
            print("Wrong.:( ")
            
           
elif user_choice == "2":
    print("You have entered 2.")
    for i in range(len(ANIMAL_QUESTIONS)):
        animal_questions = random.choice(ANIMAL_QUESTIONS)
        animal_questions = ANIMAL_QUESTIONS[i]
        answer = ANIMAL_ANSWERS[i]
        print(animal_questions)
        user_answer = input("[Answer with T or F]: ")

        if user_answer == ANIMAL_ANSWERS[ANIMAL_QUESTIONS.index(animal_questions)]:
            score = score + 1
            print(score)
            print("That's correct!.")
        else:
            print("Sorry that's wrong.")
         

elif user_choice == "3":
    print("You have entered 2.")
    for i in range(len(WORLD_QUESTIONS)):
        animal_questions = random.choice(WORLD_QUESTIONS)
        world_questions = WORLD_QUESTIONS[i]
        answer = WORLD_ANSWERS[i]
        print(world_questions)
        user_answer = input("[Answer with T or F]:")

        if user_answer == WORLD_ANSWERS[WORLD_QUESTIONS.index(world_questions)]:
            score = + 1
            print(score)
            print("Thats right!")
                
        else:
            print("Thats incorrect :(")
        
            
            

            

elif user_choice == "4":
    print("okay bye :)")

