import random
import time

flashcards = open("flashcards.txt")

def pre_made():
    print("Here is your seclection of premade decks: ")
    print("1. Periodic Table")
    answer = input("What deck would your like to use? ")
    if answer == "1":
        play_quiz("periodic_table.txt")

#add term to file
def add_terms(entered_file, entered_term): #make a way for user to name own file
    #print("call file to append to it flashcards")
    with open(f"{entered_file}", "a") as flashcards:
        flashcards.write(f"\n{entered_term}")
    print("Term added!")

#add flashacrds to deck func
def add_flashcards():
    #naming the file/deck
    valid_files = [".csv", ".txt"]
    file_input = input("What would you like to name this deck?: ")
    type_input = input("What kind of file would you like it to be?: ")
    while type_input not in valid_files:
        print("Error! File must be a .csv or .txt file.")
        type_input = input("What kind of file would you like it to be?: ")
    user_file = file_input+type_input
    print(f"Great! Your deck is named {user_file}.")

    #to save custom made files so that they can show up in custom_decks file so user can see
    # that file and choose to play from a deck there
    with open(user_file, "w") as f:
        f.write("Flashcards:\n")
    with open("decks.txt", "a") as g:
        g.write(user_file + "\n")

    #entering the terms
    print("Enter the terms you want to study one at a time. Seperate sides of the flashcards with a comma inbetween.")
    print("Here is an example:")
    print(" H, Hydrogen ----- or ----- Opulent, ostentatiously rich and luxurious or lavish.")
    print("If there is an error, I'll let you know!")
    print("You will only be able to enter a max of 25 terms.")

    # adding stuff
    for i in range(25):
        term = input("Enter both sides of the flashcard: ").lower()
        while "," not in term:
            print("Make sure you have the right format! Remember, a comma has to be inbetween the sides of the flashcard.")
            term = input("Enter both sides of the flashcard: ").lower()
        add_terms(user_file, term)

        if i < 24:
            add_q = input("Would you like to add another flashcard? (y)es or (n)o: ").lower()
            if add_q == "n":
                break

#to save custom decks by all users in one place so they don't have to rewrite them
def custom_decks():
    #try reading the decks.txt except if it dne yet then say that it dne
    try:
        with open("decks.txt", "r") as g:
            decks = [line.strip() for line in g.readlines() if line.strip()]
    except FileNotFoundError:
        print("No deck list found yet. Create a deck. ")
        return
    # if the decks.txt exists and there is nothing in it
    if not decks:
        print("There are no exsisting custom files. You need to create one using the 'Make your own deck' menu option.")
        return

    print("Here are the custom decks: ")
    #enumerate to get the index of which deck it is
    for i, deck in enumerate(decks, 1):
        print(f"{i}. {deck}")

    #user can pick what deck they want to use
    choice = input("Enter the number of the deck you want to study, or enter 'b' to go back to the menu: ").strip()
    if choice.lower() == "b":
        print("Returning to the menu...")
        return
    try:
        # int is to fit with the index of deck
        choice = int(choice)
        1 <= choice <= len(decks)
        chosen_deck = decks[choice - 1]
        print(f"Okay! Loading {chosen_deck} to study... ")
        play_quiz(chosen_deck)
    except ValueError:
        print("Please enter a valid number or 'b'. ")

#clear terms func
# need to change this to match with rest
def clear_terms():
    print("Here are the custom decks: ")
    with open("decks.txt", "r") as g:
        decks = [line.strip() for line in g.readlines() if line.strip()]
    if not decks:
        print("There are no exsisting custom files. You need to create one using the 'Make your own deck' menu option.")
        return
    #enumerate to get the index of which deck it is
    for i, deck in enumerate(decks, 1):
        print(f"{i}. {deck}")
    
    clear_input = input("Which of your decks would you like to clear?: ")
    try:
        clear_input = int(clear_input)
        1 <= clear_input <= len(decks)
        chosen_deck = decks[clear_input - 1]
        clear_q = input("Are you sure you want to clear all terms? (y)es or (n)o: ").lower()
        if clear_q == "y":
            print(f"Okay! Clearing flashcards from {chosen_deck}...")
            chosen_deck.write("") #writing blank in the deck
        elif clear_q == "n":
            print("okay")
            print("going back...")
    except ValueError:
        print("Please enter a valid number.")

def play_quiz(filename):
    print(f"play_quiz function called with {filename}")
    # "r" opens in readmode
    # 'with' helps regulate files 
    with open(filename, "r") as f:
        # strip removes spaces at the beginning and end of the string/line
        lines = [line.strip() for line in f.readlines() if "," in line] # reads the line only if "," is in it
    #creates a tuple out of the line in the file and indicate that its split by comma so that that can be used as two sides of a flashcard
    cards = [tuple(line.split(",", 1)) for line in lines]

    print("Starting your flashcards.....")
    score = 0
    for front, back in random.sample(cards, len(cards)):
        answer = input(f"What is '{front.strip()}'? ").strip().lower()
        if answer == back.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f" Incorrect. The answer was '{back.strip()}'.")
    print(f"\nYour number of correct flashcards: {score}/{len(cards)}")

    # to save the score to add_scores
    add_scores(score, len(cards))

#to add score to score file
def add_scores(correct, total):
    #print("add_scores function called to append new score to score file")
    username = input("What is your username so your score can be saved? ")
    with open("scores.txt", "a") as scores:
        scores.write(f"{username}'s Score: {correct}/{total}\n") 

def show_scores():
    #print("shows_scores function called")
    print("Here is your score History:")
    # finally able to use try/except yayyyyy!
    try:
        with open("scores.txt", "r") as scores:
            lines = scores.readlines()
            if not lines:
                print("No scores recorded yet!")
            else:
                for line in lines:
                    print(" -", line.strip())
    except FileNotFoundError:
        print("No score file found yet. Take a quiz to create one!")

def print_error():
    print("*"*50)
    print(" "*22+"error!"+" "*22)
    print(" "*12+"that is not a valid option"+" "*12)
    print(" "*17+"please try again"+" "*17)
    print("*"*50)

def main():
    #intro
    print("Welcome to Flashstudy!")
    # so that when it ges out of the helper functions it automatically goes back to this
    while True:
        print(" ----- MENU -----")
        print("1. Study from pre-made decks")
        print("2. Make your own deck(s)")
        print("3. Study from custom deck(s)")
        print("4. Start the flashcards") #might not need anymore
        print("5. Show scores")
        print("6. Clear your deck(s)")
        print("7. Exit")

        end_choice = ["7"]

        choice = input("Choose and option from 1-7: ").strip()

        while choice not in end_choice:
            #for menu
            if choice == "1":
                pre_made()
            elif choice == "2":
                add_flashcards()
            elif choice == "3":
                custom_decks()
            elif choice == "4":
                play_quiz()
            elif choice == "5":
                show_scores()
            elif choice == "6":
                print("Be warned that if you want to change anything, all flashcards will be erased.")
                clear_terms()
            else:
                print_error()

        print("Goodbye!")
main()

