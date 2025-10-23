
flashcards = open("flashcards.txt")

def play_quiz(filename):
    print(f"play_quiz function called with {filename}")

def add_terms(filename):
    print(f"call file to append to it {filename}")

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

def restart():
    print("hi")

def main():
    print("welcome")