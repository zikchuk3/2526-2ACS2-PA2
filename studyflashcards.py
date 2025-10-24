
flashcards = open("flashcards.txt")

def play_quiz(filename):
    print(f"play_quiz function called with {filename}")

def add_terms(entered_term):
    print("call file to append to it flashcards")
    flashcards = open("flashcards.txt", "a")
    flashcards.write(f"\n{entered_term}")

def clear_terms():
    flashcards = open("flashcards.txt", "w") #write mode
    flashcards.write("Flashcards:") 
    print("terms cleared")    

def show_scores():
    print("shows_scores function called")
    

def add_scores():
    print("add_scores function called")


def print_error():
    print("*"*50)
    print(" "*22+"error!"+" "*22)
    print(" "*12+"that is not a valid option"+" "*12)
    print(" "*17+"please try again"+" "*17)
    print("*"*50)

#restart function
y_or_n = ["y", "n"]
def restart(choices = ["yes", "no"]):
    print("___________________________________________________________")
    player_input = input("Is there more you want to do? (y)es or (n)o: ").lower()
    while player_input not in choices:
        print("Invalid. Please enter ", choices, ".")
        player_input = input("Do you want to play again? (y)es or (n)o: ").lower()
    if player_input == "y":

        print("___________________________________________________________")
        print("                                                           ")
        print("                                                           ")
        print("                Okay, lets go back to the office....")
        print("                                                           ")
        print("                                                           ")
        print("___________________________________________________________")
        main()
    elif player_input == "n":
        print("                                                           ")
        print("Thanks for visiting!")
        print("        __________________๑ï")
        print("        ꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷꒦꒷")

def main():
    #intro and instructions
    print("Welcome to Flashstudy!")
    print("Enter the terms you want to study one at a time. Seperate sides of the flashcards with a comma inbetween.")
    print("Here is an example:")
    print(" H, Hydrogen ----- or ----- Opulent, ostentatiously rich and luxurious or lavish.")
    print("If there is an error, I'll let you know!")
    print("You will only be able to enter a max of 25 terms.")

    # adding stuff
    user_input = input("Enter both sides of the flashcard: ")
    while "," not in user_input:
        print("Make sure you have the right format!")
        user_input = input("Enter both sides of the flashcard: ")
    else:
        add_terms(user_input)
        for i in range(25):
            add_q = input("Would you like to add another flashcard? (y)es or (n)o")
            while add_q == "y":
                new_term = input("Enter both sides of the flashcard: ")
                add_terms(new_term)
                add_q = input("Would you like to add another flashcard? (y)es or (n)o")
            if add_q == "n":
                print('okay')
                break
            else:
                print_error()
                break
    
    #clearing terms/ if user wants to change anything
    print("If there is anything you want to change, do so now.")
    print("Be warned that if you want to change anything, all flashcards will be erased.")
    clear_q = input("Would you like to change anything?")
    while clear_q == "y":
        clear_terms()
        break
    #actually showing flashcards now
    user_input = input("Do you want to start studying now?")
    while user_input == "y":
        print("Okay!")


main()

