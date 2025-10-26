import random

flashcards = open("flashcards.txt")

def play_quiz(filename = "flashcards.txt"):
    print(f"play_quiz function called with {filename}")
    # "r" opens in readmode
    # with helps regulate files ?
    with open(filename, "r") as f:
        # strip removes spaces at the beginning and end of the string/line
        # reads the line only if "," is in it
        lines = [line.strip() for line in f.readlines() if "," in line]
    # create a tuple out of the line in the file and indicate that its split by comma
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

#add term to file
def add_terms(entered_term):
    print("call file to append to it flashcards")
    with open("flashcards.txt", "a") as flashcards:
        flashcards.write(f"\n{entered_term}")
    print("Term added!")

#clear terms func
def clear_terms():
    clear_q = input("Are you sure you want to clear all terms? (y)es or (n)o: ").lower()
    if clear_q == "y":
        with open("flashcards.txt", "w") as flashcards: #write mode
            flashcards.write("Flashcards:") 
        print("terms cleared")    
    elif clear_q == "n":
        print("okay")
        print("going back...")

#add flashacrds to deck func
def add_flashcards():
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
        add_terms(term)

        if i < 24:
            add_q = input("Would you like to add another flashcard? (y)es or (n)o: ").lower()
            if add_q == "n":
                break

#to add score to score file
def add_scores(correct, total):
    print("add_scores function called to append new score to score file")
    with open("scores.txt", "a") as scores:
        scores.write(f"{correct}/{total}\n")
    print(f"Score added: {correct}/{total}")   

def show_scores():
    print("shows_scores function called")
    print("Here is your score History:")
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

'''
dont need anymore i think
#restart function
y_or_n = ["y", "n"]
def restart(choices = ["yes", "no"]):
    print("___________________________________________________________")
    player_input = input("Do you want to study again? (y)es or (n)o: ").lower()
    while player_input not in choices:
        print("Invalid. Please enter ", choices, ".")
        player_input = input("Do you want to study again? (y)es or (n)o: ").lower()
    if player_input == "y":
        print("___________________________________________________________")
        print("                                                           ")
        print("                                                           ")
        print("                Okay, let's study again....")
        print("                                                           ")
        print("                                                           ")
        print("___________________________________________________________")
        main()
    elif player_input == "n":
        with open("flashcards.txt", "w") as flashcards: #write mode
            flashcards.write("Flashcards:") 
        print("                                                           ")
        print("Thanks for visiting!")
        print("        __________________๑ï")
        print("        ꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷")'''

def main():
    while True:
        #intro
        print("Welcome to Flashstudy!")
        print(" ----- MENU -----")
        print("1. Add flashcards")
        print("2. Start quiz")
        print("3. Show scores")
        print("4. Clear flashcards")
        print("5. Exit")

        choice = input("Choose and option from 1-5: ").strip()

        if choice == "1":
            add_flashcards()
        elif choice == "2":
            play_quiz()
        elif choice == "3":
            show_scores()
        elif choice == "4":
            print("Be warned that if you want to change anything, all flashcards will be erased.")
            clear_terms()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print_error()
main()

