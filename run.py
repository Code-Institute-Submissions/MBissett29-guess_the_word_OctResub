"""
This imports the words from the list
of words that was created im the words.py file.
It also allows the run.py file to use the
random file in python
"""
import random
from words import guess_word_list
import string


def pull_the_word(guess_word_list):

    """
    Gets the word from the words.py file and randomly
    selects a word for player to guess
    """
    word = random.choice(guess_word_list)
    return word.upper()


def get_user_letter_input():

    """
    This is the main game function where the player
    inputs a letter and the code checks to see if it
    is correct or not. Then tracks the life counter.
    """

    word = pull_the_word(guess_word_list)
    letters_in_word = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    lives = 6
    while len(letters_in_word) > 0 and lives > 0:
        '''
        Shows the letters that user has used
        this also shows in the terminal the string of letters with a space
        '''
        print("\nYou have", lives, "lives remaining")
        print("You have used these letters ", " ".join(used_letters))


        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            word_stage = [
                letter if letter in used_letters else "_" for letter in word
            ]
            if user_letter in letters_in_word:
                letters_in_word.remove(user_letter)
            else:
                lives = lives - 1  # decucts from life points
                print("\nLetter", user_letter, "is not in the word!")
            print("Current guesses ", " ".join(word_stage))

        elif user_letter in used_letters:
            print("Uh oh you have already used that one! Try another ")

        else:
            print("Invalid character please use a letter")


    check_lives(lives)


def check_lives(lives):
    """
    Checks the players lives remaining and then when lives 
    hit zero or player guesses correctly they get to have 
    the option to play again.
    """

    if lives == 0:
        print("Game over! Better luck next time.")
        play_again()
    else:
        print("Congratulations you won!!!")
        play_again()

def play_again():
    """
    The play again option allows the player to make a decision
    if they want to play or not. The code asks for input of either
    Y or any other key.
    """

    print("\nPlay Again?")
    print("Enter Y or hit the Run Program button above.")
    print("Or hit any other key to stop")

    new_game = input(
        "Please press y to play again, \nor any other key to quit the game: "
        )

    if new_game.lower() == "y":
        get_user_letter_input()
    else:
        print("Thank you for playing Guess the Word!")

def main():
    """
    Main function that introduces the game and runs
    the game.
    """
    print("* * * * * * * * * * * * *")
    print("Lets play guess the word!!")
    print("Are you ready?")
    print("* * * * * * * * * * * * *")

    get_user_letter_input()

main()
