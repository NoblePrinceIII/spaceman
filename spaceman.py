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

# A function that checks if all the letters of the secret word have been guessed.
def is_word_guessed(secret_word, letters_guessed):
# Loops through the letters in the secret_word and checks if a letter is not in letters Guessed
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
    return True

# A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.
def get_guessed_word(secret_word, letters_guessed):
 # Loops through the letters in secret word and shows if guessed correctly
    guessed_word = ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += "_"
    return guessed_word

# function to check if the guessed letter is in the secret word
def is_guess_in_word(guess, secret_word):
# checks if the letter guess is in the secret word
    if guess in secret_word:
        return True
    else:
        return False

def spaceman(secret_word):
    length = len(secret_word)
    print("Spaceman Word Guessing Game")
    print ("The Secret Word has:",length,"Letters")
    print("You have 7 Attempts Remaining")


    letters_guessed = []
    attempt = 7
    # declaring a variable to a list of alphabets
    letters_left = list(string.ascii_lowercase)
    # while loop that checks if you have won and kost the game based on attempts guessed and if word is right
    while attempt > 0 and is_word_guessed(secret_word, letters_guessed) == False:
        letter = str.lower(input("Please Enter a Letter: "))

        # Ask's the player to guess one letter per round and if not asks to enter 1 letter
        while len(letter) != 1:
            letter =  str.lower(input("Please Enter a Single Letter: "))
        # checks if guessed letter in letters_guessed list
        while letter in letters_guessed:
            letter = input("You Have Already Guessed This Letter Please Enter a New Letter: ")
        # If user makes an input error
        while str.isalpha(letter) == False:
            letter = input("Please Enter a Single Letter With no Space")
        # if user inputs correct letter if not subtract one attempt
        if is_guess_in_word(letter, secret_word) == True:
             print("The Letter is Correct!")
        else:
            print("Incorrect Letter Try again!")
            attempt -= 1
        # checks and removes if guessed letter in already guessed list,
        if letter in letters_left:
           letters_left.remove(letter)
           letters_guessed.append(letter)
        else:
            pass
        # shows the player information about the game according to the project spec
        print("Attempted Letters: ", *letters_guessed)
        print(letters_guessed)
        # displays dashes and the guessed letters
        print(get_guessed_word(secret_word, letters_guessed))

        print("Guesses Remaining:", attempt)
        print("Letters Left:", *letters_left)
        # checks if the game has been won or lost
        if is_word_guessed(secret_word, letters_guessed):
             print("Congratulations!! You Win")
        if attempt == 0:
            print("You Lose :( , the Correct word is", *secret_word)


secret_word = load_word()
spaceman(secret_word)
# checks why the y/n is not working
again = input("Do you want to play again?(Y/N): ")
if again == "y" or again == "Y":
    secret_word = load_word()
    spaceman(secret_word)
else:
    print("Thanks for Playing")
