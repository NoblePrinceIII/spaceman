from random import choice
import string


def load_word():
    # '''
    # # A function that reads a text file of words and randomly selects one to use as the secret word
    # #     from the list.
    # # Returns:
    # #        string: The secret word to be used in the spaceman guessing game
    # # '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()

    words_list = words_list[0].split(' ')
    secret_word = choice(words_list)
    return secret_word


def is_word_guessed(secret_word, letters_guessed):
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True
    # A function that checks if all the letters of the secret word have been guessed.
    # Args:
    #     secret_word (string): the random word the user is trying to guess.
    #     letters_guessed (list of strings): list of letters that have been guessed so far.
    # Returns:
    #     bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_"
    return guessed_word
    # '''
    # A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
    # Args:
    #     secret_word (string): the random word the user is trying to guess.
    #     letters_guessed (list of strings): list of letters that have been guessed so far.
    # Returns:
    #     string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    # '''
    #
    # #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    #
    # pass
def is_guess_in_word(guess, secret_word):
    if guess in secret_word:
        return True
    else:
        return False
    # '''
    # A function to check if the guessed letter is in the secret word
    # Args:
    #     guess (string): The letter the player guessed this round
    #     secret_word (string): The secret word
    # Returns:
    #     bool: True if the guess is in the secret_word, False otherwise
    # '''
    # TODO: check if the letter guess is in the secret word
def get_wrong_letters(letters_guessed,secret_word):
        wrongLetters = []
        for letter in letters_guessed:
            if letter not in secret_word:
                wrongLetters+=letter
                return wrongLetters

def spaceman(secret_word):
    length = len(secret_word)
    print("Spaceman Word Guessing Game")
    print ("The Secret Word has:",length,"Letters")
    print("You have 7 Attempts Remaining")
    print(secret_word)

    letters_guessed = []
    attempt = 3

    letters_left = list(string.ascii_lowercase)

    while attempt > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        letter = str.lower(input("Please Enter a Letter: "))


        while len(letter) != 1:
            letter =  str.lower(input("Please Enter a Single Letter: "))

        while letter in letters_guessed:
            letter = input("You Have Already Guessed This Letter Please Enter a New Letter: ")

        while str.isalpha(letter) == False:
            letter = input("Please Enter a Single Letter With no Space")

        if is_guess_in_word(letter, secret_word) == True:
             print("The Letter is Correct!")

        else:
            print("Incorrect Letter Try again!")
            attempt -= 1

        if letter in letters_left:
           letters_left.remove(letter)
           letters_guessed.append(letter)
        else:
            pass

        print("Attempted Letters: ", *letters_guessed)
        print(letters_guessed)
        print(get_guessed_word(secret_word, letters_guessed))
        print("Guess Remaining", attempt)
        print("Letters Left", *letters_left)

        if is_word_guessed(secret_word, letters_guessed):
             print("You Win")

        if attempt == 0:
            print("You Lose")


secret_word = load_word()
spaceman(secret_word)
again = input("Do you want to play again?(Y/N): ")
if again == "y" or again == "Y":
    secret_word = load_word()
    spaceman(secret_word)
else:
    print("Thanks for Playing")

    # '''
    # A function that controls the game of spaceman. Will start spaceman in the command line.
    # Args:
    #   secret_word (string): the secret word to guess.
    # '''
    # TODO: show the guessed word so far
    # TODO: show the player information about the game according to the project spec
    # TODO: Ask the player to guess one letter per round and check that it is only one letter
    #  determine the number of turns
    #TODO: show the player information about the game according to the project spec
    #TODO: show the guessed word so far
    #TODO: check if the game has been won or lost
    #TODO: Check if the guessed letter is in the secret or not and give the player feedback
    #check why the y/n is not working
