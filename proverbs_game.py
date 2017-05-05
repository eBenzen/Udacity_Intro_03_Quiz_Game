#Level 1 - 1 answer options
#Level 2 - 3 answer options
#Level 3 - 5 answer options

#IMPORTS
from random import * #source - https://pythonspot.com/en/random-numbers/
import random
from random import shuffle
import time #source - http://pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/

#GLOBAL VAR
 
# The following are verses that will be displayed at random, top the game player
q_1 = "A false balance is an abomination to the Lord, but a _______ weight is his delight."
q_2 = "When pride comes, then comes disgrace, but with the _______ is wisdom."
q_3 = "The integrity of the upright guides them, but the crookedness of the treacherous _______ them."
q_4 = "Riches do not profit in the day of wrath, but _______ delivers from death."
q_5 = "The righteousness of the blameless keeps his way straight, but the wicked _______ by his own wickedness."
q_6 = "The righteousness of the upright delivers them, but the treacherous are taken captive by their _______."
q_7 = "When the wicked dies, his hope will perish, and the _______ of wealth perishes too."

#Make a question bank that can be called with indexing
q_bank = []
q_bank.append(q_1)
q_bank.append(q_2)
q_bank.append(q_3)
q_bank.append(q_4)
q_bank.append(q_5)
q_bank.append(q_6)
q_bank.append(q_7)

#Make a Answer bank that can be called with indexing
a_bank = ["just", "humble", "destroy", "righteousness", "falls","lusts","expectations"]

#Making Yes and No work more broadly
yes_options = ["yes","Yes","Y","y"]
no_options = ["no","No","N","n"]

#Appendix-----------------------------------------------------------------------------

#A.1 - Removing duplicates
#source - http://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
def remove_duplicates(l):
    return list(set(l))

#A.2 - Quiz cycle compelte
def quiz_complete():
    print " "
    print "Horray, you finished!"
    time.sleep(3)

#A.3 - Final function to close out the program, went asked by user input
def thanks_goodbye():
    print " "
    print "We hope that you enjoyed today's Proverb, see you tomorrow!"
    time.sleep(2)
    quit() #source - http://stackoverflow.com/questions/73663/terminating-a-python-script

#A.4 - Welcome menu and first thing called, keep open until user input starts the game
def welcome_menu():
    print " "
    print "WELCOME to the Proverb Garden"  
    print "-------------------------------------------------"
    print " "
    print "To EXIT - Hold 'control' and press 'Z' at any point to end the game" #source - http://stackoverflow.com/questions/18047657/stop-python-in-terminal-on-mac
    time.sleep(1) #source - http://pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/

#A.5 - Level of difficulty selected, will return the number of multiple choices for the quiz questions
def select_level():
    #estalish the local variable that start at 0
    number_of_choices = 0

    while number_of_choices == 0:
        print " "
        print "Please select the difficulty level, or to hit esc to exit:"
        difficulty_selected = raw_input("  For Easy type E, for Medium type M, and for Hard type H, and hit enter: ")
        difficulty_selected = difficulty_selected.upper()
        
        #with that input, a level is selected
        if difficulty_selected=="E":
            number_of_choices = 1
            print " "
            print "Easy level, here we go:"
            time.sleep(1)
            return number_of_choices
        if difficulty_selected=="M":
            number_of_choices = 3
            level="M"
            print " "
            print "Medium level, on it's way:"
            time.sleep(1)
            return number_of_choices
        if difficulty_selected=="H":
            number_of_choices = 5
            level="H"
            print " "
            print "Hard as it gets, time to start:"
            time.sleep(1)
            return number_of_choices
        else:
            print " "
            print "Sorry, invalid selection:"
            time.sleep(1)

#A.6 - Replace the blank with the word
def replaced(q,a):
    split_q = q.split()    #source - http://stackoverflow.com/questions/743806/split-string-into-a-list-in-python
    new_q = []
       
    for x in split_q:
        if x != "_______":
            new_q.append(x)
        else:
            new_q.append(a)
            
    return " ".join(new_q)



#MAIN FUNCTIONS---------------------------------------------------------

#CREATE MULTIPLE CHOICES
#number_of_choices - The total # of options
#a_bank - import the total list of answers
#index - this is the index of the correct answer
def create_multiple_choices(number_of_choices,a_bank,index):
    #creat a list of possible indexes for the answer choices

    #Step 1 - Start the list with the correct answer
    temp_a_bank = [a_bank[index]]

    #Step 2 - Add the other options, based on the input number_of_choices
    #define the range to exclude the correct answer
    #Source - http://stackoverflow.com/questions/10666661/can-python-generate-a-random-number-that-excludes-a-set-of-numbers-without-usin
    i_range = range(0,index) + range(index+1,len(a_bank))


    #Step 3 - From that range, pick a unique set of numbers
    #source - http://stackoverflow.com/questions/22842289/generate-n-unique-random-numbers-within-a-range
    other_choices = random.sample(i_range,number_of_choices-1)     


    #Step 4 - Add other answers to the temporary anser bank using the new indexies
    for x in other_choices:
        temp_a_bank.append(a_bank[x])


    #Step 5 - Shuffle answer optins in random order
    # Source - http://stackoverflow.com/questions/42674509/how-to-shuffle-a-list-of-strings-order
    temp_a_bank = random.sample(temp_a_bank, len(temp_a_bank))


    #Step 6 - Print the multiple choice options, with numbering
    #print Easty level with no numbering for a better look
    if number_of_choices==1:
        for x in temp_a_bank:
            number = temp_a_bank.index(x) + 1
            print "   "+ str(x)
    else:
        for x in temp_a_bank:
            number = temp_a_bank.index(x) + 1
            print "   "+ str(number) + ": " + str(x)

#QUIZ FUNCTION - pass the number of choices, and both banks for the quiz
def quiz(number_of_choices,q_bank,a_bank):
    #Local variables that will be removed down to a blank list
    index = 0

    #Print out the instructions
    print " "
    print "Please fill in the blank to complete the Proverb."  
    print "-------------------------------------------------"
    print " "

    #Cycle through each question in simple order with 1 option
    while index<len(q_bank):
        print q_bank[index]
        print " "
        create_multiple_choices(number_of_choices,a_bank,index)
        print " "
        user_input_answer = raw_input("From the options above, type the word that best fits: ")

        # check for a correct answer, and so, remove it from the local list and move on
        if user_input_answer == a_bank[index]:
            print " "
            print "Correct! " + replaced(q_bank[index],a_bank[index])       
            print " "
            index+=1
        else:
            print " "
            print "Incorrect, please try again"
            print " "
            #index remains the same if incorrect, so we cycle again

    quiz_complete()# Displays a message when complete

#---------------------------PRIMARY OPERATION---------------------------


#GAME PLAY--------------------------------------------------------
def play_game(q_bank,a_bank):
    #Step 1 - Question and answer banks imported from Global Variables
    
    #Step 2 - Welcome Message to start
    welcome_menu() #will loop until user starts

    #Step 3 - Main Game Loop
    game_play = True #bolean varible to keep game going

    while game_play ==True:
        #Step 3a - Pull user input to Select a Level
        number_of_choices = select_level() #the number of answer choices corresponds to the level selected

        #Step 3b - Start the quiz
        quiz(number_of_choices,q_bank,a_bank)

        #Step 3c - Play again?
        play_again = raw_input("Would you like to play again? (Type yes or no): ")

        if play_again in yes_options:
            game_play = True
        else:
            game_play = False
        
    #Step 4 - Good Bye - once the game loop is stopped, send them home
    thanks_goodbye()

#TESTING -----------------------------------
play_game(q_bank,a_bank)

