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
    Gets the word from the list randomly
    """
    word = random.choice(guess_word_list)
    return word.upper()

word = pull_the_word(guess_word_list)
letters_in_word = set(word)
alphabet = set(string.ascii_uppercase)
used_letters = set()


def get_user_letter_input():

    lives = 6
    while len(letters_in_word) > 0 and lives > 0:
        '''
        Shows the letters that user has used
        this also shows in the terminal the string of letters with a space
        '''
        print("\nYou have", lives, "lives remaining")
        print("You have used these letters ", " ".join(used_letters))
        # shows what stage the word is in
        word_stage = [
            letter if letter in used_letters else "_" for letter in word
        ]

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in letters_in_word:
                letters_in_word.remove(user_letter)
                print("")
            else:
                lives = lives - 1  # decucts from life points
                print("\nLetter", user_letter, "is not in the word!")

        elif user_letter in used_letters:
            print("Uh oh you have already used that one! Try another ")

        else:
            print("Invalid character please use a letter")

        print("Current guesses ", " ".join(word_stage))

    check_lives(lives)


def check_lives(lives):

    if lives == 0:
        print("Game over! Better luck next time.")
    else:
        print("Congratulations you won!!!")

print("* * * * * * * * * * * * *")
print("Lets play guess the word!!")
print("Are you ready?")
print("* * * * * * * * * * * * *")


def main():
    get_user_letter_input()
    while input("Play Again? (Y/N) ").upper() == "Y":
        get_user_letter_input()

main()
