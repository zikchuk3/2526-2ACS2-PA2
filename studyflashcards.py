import random
import time

# this is just pre-made flashcards (so just the periodtic table one)
def pre_made():
    print()
    time.sleep(0.5)
    print("---- PREMADE DECKS ---- ")
    print("1. Periodic Table")
    print()
    time.sleep(0.2)
    answer = input("What deck would your like to use? ")
    if answer == "1":
        play_quiz("periodic_table.txt")

#add term to custom flashcards
def add_terms(entered_file, entered_term): #made a way for user to name own file (added enterd_file)
    #print("call file to append to it flashcards")
    with open(f"{entered_file}", "a") as flashcards:
        flashcards.write(f"\n{entered_term}")
    print("Flashcard added to deck!")
    time.sleep(0.5)
    print("-----------------------------------------------")
    print(f"               {entered_term}")
    print("-----------------------------------------------")

y_or_n = ["y", "n"]
#create own deck
def add_flashcards():
    #naming the file/deck
    valid_files = [".csv", ".txt", "txt", "csv"]
    #figure out way to not include file type here
    print()
    time.sleep(0.5)
    file_input = input("What would you like to name this deck? (Do not include the file type): ")
    time.sleep(0.5)
    type_input = input("What type of file would you like it to be?: ")
    while type_input not in valid_files:
        print("Error! File must be a .csv or .txt file.")
        type_input = input("What kind of file would you like it to be?: ")
    if "." in type_input:
        user_file = file_input+type_input
        print()
        print(f"Great! Your deck is named {user_file}.")
    else:
        user_file = file_input+"."+type_input
        print()
        print(f"Great! Your deck is named {user_file}.")

    #to save custom made files so that they can show up in custom_decks file so user can see
    # that file and choose to play from a deck there
    with open(user_file, "w") as f:
        f.write("Flashcards:\n")
    with open("decks.txt", "a") as g:
        g.write(user_file + "\n")

    #entering the terms instructions
    print()
    time.sleep(0.5)
    print("Enter the terms you want to study one at a time. Seperate sides of the flashcards with a comma inbetween.")
    time.sleep(0.3)
    print("Here is an example:")
    time.sleep(0.3)
    print(" H, Hydrogen ----- or ----- Opulent, ostentatiously rich and luxurious or lavish.")
    time.sleep(0.3)
    print("If there are any other commas besides to seperate the cards, do not put them. If there is an error, I'll let you know!")
    time.sleep(0.3)
    print("You will only be able to enter a max of 25 terms.") #made it like this so it doesn't just keep going lol

    # adding stuff to the users file
    for i in range(25):
        print()
        time.sleep(0.5)
        term = input("Enter both sides of the flashcard: ").lower()
        while "," not in term:
            print("Make sure you have the right format! Remember, a comma has to be inbetween the sides of the flashcard.")
            print()
            time.sleep(0.5)
            term = input("Enter both sides of the flashcard: ").lower()
        add_terms(user_file, term)
        if i < 24:
            print()
            time.sleep(0.2)
            add_q = input("Would you like to add another flashcard? (y)es or (n)o: ").lower()
            while add_q not in y_or_n:
                print("Please enter 'y' or 'n' ")
                print()
                add_q = input("Would you like to add another flashcard? (y)es or (n)o: ").lower()
            if add_q == "n":
                break


#to save custom decks by all users in one place so they don't have to rewrite them
# to also play the deck after creating it
def custom_decks():
    #try reading the decks.txt except if it dne yet then say that it dne
    try:
        with open("decks.txt", "r") as g:
            decks = [line.strip() for line in g.readlines() if line.strip()]
    except FileNotFoundError:
        time.sleep(1)
        print("No custom deck list found. Create a deck. ")
        return
    # if the decks.txt exists and there is nothing in it
    if not decks:
        time.sleep(1)
        print("There are no exsisting custom decks. You need to create one using the 'Make your own deck' menu option.")
        return

    print()
    time.sleep(0.5)
    print("---- CUSTOM DECKS ---- ")
    #enumerate to get the index of which deck it is
    for i, deck in enumerate(decks, 1):
        print(f"{i}. {deck}")

    print()
    #user can pick what deck they want to use
    choice = input("Enter the number of the deck you want to study, or enter 'b' to go back to the menu: ").strip()
    if choice.lower() == "b":
        print()
        time.sleep(1)
        print("Returning to the menu...")
        return
    try:
        # int is to fit with the index of deck
        choice = int(choice)
        1 <= choice <= len(decks)
        chosen_deck = decks[choice - 1]
        time.sleep(0.5)
        print(f"Okay! Loading {chosen_deck} to study... ")
        play_quiz(chosen_deck)
    except ValueError:
        print("Please enter a valid number or 'b'. ")

#clear terms func
# to clear custom deck
def clear_terms():
    print()
    time.sleep(0.5)
    print("---- CUSTOM DECKS ---- ")
    with open("decks.txt", "r") as g:
        decks = [line.strip() for line in g.readlines() if line.strip()]
    if not decks:
        time.sleep(1)
        print("There are no exsisting custom decks. You need to create one using the 'Make your own deck' menu option.")
        return
    #enumerate to get the index of which deck it is
    for i, deck in enumerate(decks, 1):
        print(f"{i}. {deck}")
    
    print()
    time.sleep(0.3)
    clear_input = input("Which of your decks would you like to clear?: ")
    try:
        clear_input = int(clear_input)
        #input has to be less than or equal to one or less than or equal to the number of decks
        1 <= clear_input <= len(decks)
        chosen_deck = decks[clear_input - 1]
        time.sleep(0.3)
        clear_q = input("Are you sure you want to clear all terms? (y)es or (n)o: ").lower()
        if clear_q == "y":
            print()
            print(f"Okay! Clearing flashcards from {chosen_deck}...")
            time.sleep(1)
            chosen_deck.write("") #writing blank in the deck
            print(f"Flashcards from {chosen_deck} cleared!")
        elif clear_q == "n":
            print()
            time.sleep(0.2)
            print("Okay")
            time.sleep(0.5)
            print("Going back...")
    except ValueError:
        print("Please enter a number shown on the list of custom decks.")

#play the flashcards
def play_quiz(filename):
    #print(f"play_quiz function called with {filename}")
    # "r" opens in readmode
    # 'with' helps regulate files 
    with open(filename, "r") as f:
        # strip removes spaces at the beginning and end of the string/line
        lines = [line.strip() for line in f.readlines() if "," in line] # reads the line only if "," is in it
    #creates a tuple out of the line in the file and indicate that its split by comma so that that can be used as two sides of a flashcard
    cards = [tuple(line.split(",", 1)) for line in lines]

    print()
    time.sleep(0.5)
    print("Starting your flashcards.....")
    score = 0
    for front, back in random.sample(cards, len(cards)):
        print()
        time.sleep(0.5)
        answer = input(f"What is '{front.strip()}'? ").strip().lower()
        if answer == back.strip().lower():
            print("Correct!")
            score += 1
        else:
            print(f" Incorrect. The answer was '{back.strip()}'.")

    print()
    time.sleep(0.5)
    print(f"\nYour number of correct flashcards: {score}/{len(cards)}")

    # to save the score to add_scores
    add_scores(score, len(cards))

#to add score to score file
def add_scores(correct, total):
    #print("add_scores function called to append new score to score file")
    print()
    time.sleep(0.3)
    username = input("What is your username so your score can be saved?: ")
    time.sleep(0.5)
    print("Username saved....")
    time.sleep(0.3)
    date = input("What is today's date?: ")
    time.sleep(0.5)
    print("Date saved...")
    with open("scores.txt", "a") as scores:
        scores.write(f"{username}'s Score: {correct}/{total} on {date}\n") 

#show scores in score file
def show_scores():
    #print("shows_scores function called")
    print()
    time.sleep(0.5)
    print("Here is the Score History:")
    # finally able to use try/except yayyyyy!
    try:
        with open("scores.txt", "r") as scores:
            lines = scores.readlines()
            if not lines:
                time.sleep(1)
                print("No scores recorded yet!")
            else:
                for line in lines:
                    print(" -", line.strip())
    except FileNotFoundError:
        time.sleep(1)
        print("No score file found yet. Take a quiz to create one!")

#error message
def print_error():
    print("*"*50)
    print(" "*22+"error!"+" "*22)
    print(" "*12+"that is not a valid option"+" "*12)
    print(" "*17+"please try again"+" "*17)
    print("*"*50)

#made a menu func so that I can just call it easily in main func (specifically in the while loop)
def menu():
    print(" ----- MENU -----")
    print("1. Study from pre-made decks")
    print("2. Make your own deck(s)")
    print("3. Study from custom deck(s)")
    print("4. Show scores")
    print("5. Clear your deck(s)")
    print("6. Exit")


#main func
def main():
    #intro
    print("------------ Welcome to Flashstudy! ------------")
    print()
    time.sleep(0.5)
    menu()

    end_choice = ["6"]

    print()
    choice = input("Choose and option from 1-6: ").strip()

    while choice not in end_choice:
        #for menu
        if choice == "1":
            pre_made()
        elif choice == "2":
            add_flashcards()
        elif choice == "3":
            custom_decks()
        elif choice == "4":
            show_scores()
        elif choice == "5":
            time.sleep(0.3)
            print("Be warned that if you want to change anything, all flashcards will be erased.")
            clear_terms()
        else:
            print_error()
        print()
        time.sleep(0.5)
        menu()
        print()
        choice = input("Choose and option from 1-6: ").strip()

    print()
    time.sleep(0.5)
    print("Goodbye!")
    time.sleep(1)
    print("o       o")
    print("\_____/ ")
    print(" /=O=O=\     _______ ")
    print("/   ^   \   /\\\\\\\\")
    print("\ \___/ /  /\   ___  \'")
    print(" \_ V _/  /\   /\\\\  \'")
    print("   \  \__/\   /\ @_/  /")
    print("    \____\____\______/")

main()

