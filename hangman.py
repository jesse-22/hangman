# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    # print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    letters_guessed_list = [letters_guessed]
    guessed_word = get_guessed_word(secret_word, letters_guessed)
    # guessed_list = []
    # guessed_list.append(guessed_word)
    guess_word_string = ''.join(guessed_word)
    correct_word = guessed_word + letters_guessed
    if guess_word_string == secret_word:
        return True
    else:
        return False


def get_guessed_word(secret_word, letters_guessed):
    guess = [l if l in letters_guessed else "_" for l in secret_word]
    string_guess = "".join(guess)
    return string_guess


def get_available_letters(letters_guessed):
    list_alpha = list(string.ascii_lowercase)
    avail_letters = [i for i in list_alpha if i not in letters_guessed]
    string_letters = ''.join(avail_letters)
    print("Available Letters:", string_letters)
    return avail_letters


def hangman(secret_word):
    guessed = False
    guess_count = 6
    warnings = 3
    guessed_letters = []
    guessed_words = []
    correct_letters = []
    vowels = ('a', 'e', 'i', 'o', 'u')
    hint = '*'
    print("Welcome to hangman!")
    print("You have 6 guesses to win.")
    print("You get 3 warnings")
    length_of_secret_word = len(secret_word)
    print("Total letters in the word are: ", length_of_secret_word)

    while guessed is False and guess_count > 0 and warnings > 0:
        guess = input("Enter letter you want to guess:")
        if guess == secret_word:
            print("You got the word:", guessed_words)
        else:
            if not guess.isalpha() and guess_count > 3:
                warnings -= 1
                print("Please enter a letter only!")
                print("Warnings left:", warnings)
                print("Guess count:", guess_count)

            elif guess not in secret_word:
                if guess not in guessed_letters:
                    if guess in vowels:
                        guess_count -= 2
                        print("Warnings left:", warnings)
                        print("Guesses Left:", guess_count)
                        guessed_letters.append(guess)
                        guessed_word = get_guessed_word(secret_word, guessed_letters)
                        print("That vowel is not in the word, you lose two guesses", guessed_word)
                        get_available_letters(guessed_letters)

                    else:
                        guess_count -= 1
                        print("Warnings left:", warnings)
                        print("Guesses left:", guess_count)
                        guessed_letters.append(guess)
                        guessed_word = get_guessed_word(secret_word, guessed_letters)
                        print("Sorry, that letter is not in the word!", guessed_word)
                        get_available_letters(guessed_letters)


                else:
                    warnings -= 1
                    print("Warnings left:", warnings)
                    print("Guesses left:", guess_count)
                    guessed_word = get_guessed_word(secret_word, guessed_letters)
                    print("You already guessed that letter! You lose a warning!", guessed_word)

                    if warnings == 0:
                        guess_count -= 1
                        print("You ran out of warnings!")
                        print("Guesses left:", guess_count)
            else:
                if guess in guessed_letters:
                    warnings -= 1
                    print("Warnings left:", warnings)
                    print("Guesses left:", guess_count)
                    guessed_word = get_guessed_word(secret_word, guessed_letters)
                    print("You already guessed that letter! You lost a warning!", guessed_word)

                else:
                    guess_count -= 1
                    guessed_letters.append(guess)
                    print("Guesses left:", guess_count)
                    get_available_letters(guessed_letters)
                    guessed_word = get_guessed_word(secret_word, guessed_letters)
                    word_complete_string = ''.join(guessed_word)

                    if word_complete_string == secret_word:
                        print("you got the word!", guessed_word)
                    else:
                        guess_count -= 1
                        print("Good guess!", guessed_word)

    if guess_count == 0:
        print("Sorry you didn't get the word.")
        print("The word was:", secret_word)


def match_with_gaps(my_word, other_word):
    my_word_list = list(my_word)
    my_enumerate = list(enumerate(my_word_list))
    my_word_length = len(my_word)
    total_other_words = len(other_word)
    possible_words = []
    total_word_count = 0
    stored_myenum = []
    stored_myenum_set = {}

    while total_word_count != 52780:
        for s in my_enumerate:
            if s[1] != "_":
                stored_myenum.append(s)
                stored_myenum_set = set(stored_myenum)
        for i in other_word:
            other_word_list = list(i)
            other_word_length = len(other_word_list)
            other_word_enum = list(enumerate(other_word_list))
            set_otherenum = set(other_word_enum)
            matches = stored_myenum_set.intersection(set_otherenum)
            if matches == stored_myenum_set and my_word_length == other_word_length:
                possible_words.append(i)
                total_word_count += 1
            else:
                total_word_count += 1

    print(possible_words)


def hangman_with_hints(secret_word):
    guessed = False
    guess_count = 6
    warnings = 3
    guessed_letters = []
    guessed_words = []
    correct_letters = []
    cl = len(correct_letters)
    vowels = ('a', 'e', 'i', 'o', 'u')
    hint = '*'
    print("Welcome to hangman!")
    print("You have 6 guesses to win.")
    print("You get 3 warnings")
    length_of_secret_word = len(secret_word)
    print("Total letters in the word are: ", length_of_secret_word)

    while guessed is False and guess_count > 0 and warnings > 0:
        guess = input("Enter letter you want to guess:")
        if guess == secret_word:
            print("You got the word:", guessed_words)
        else:
            if not guess.isalpha() and cl < 1:
                warnings -= 1
                print("Please enter a letter only!")
                print("Warnings left:", warnings)
                print("Guess count:", guess_count)
            elif guess == hint and cl >= 1:
                other_word = load_words()
                my_word = get_guessed_word(secret_word, guessed_letters)
                match_with_gaps(my_word, other_word)
            elif guess not in secret_word:
                if guess not in guessed_letters:
                    if guess in vowels:
                        guess_count -= 2
                        print("Warnings left:", warnings)
                        print("Guesses Left:", guess_count)
                        guessed_letters.append(guess)
                        guessed_word = get_guessed_word(secret_word, guessed_letters)
                        print("That vowel is not in the word, you lose two guesses", guessed_word)
                        get_available_letters(guessed_letters)

                    else:
                        guess_count -= 1
                        print("Warnings left:", warnings)
                        print("Guesses left:", guess_count)
                        guessed_letters.append(guess)
                        guessed_word = get_guessed_word(secret_word, guessed_letters)
                        print("Sorry, that letter is not in the word!", guessed_word)
                        get_available_letters(guessed_letters)

                else:
                    warnings -= 1
                    print("Warnings left:", warnings)
                    print("Guesses left:", guess_count)
                    guessed_word = get_guessed_word(secret_word, guessed_letters)
                    print("You already guessed that letter! You lose a warning!", guessed_word)

                    if warnings == 0:
                        guess_count -= 1
                        print("You ran out of warnings!")
                        print("Guesses left:", guess_count)
            else:
                if guess in guessed_letters:
                    warnings -= 1
                    print("Warnings left:", warnings)
                    print("Guesses left:", guess_count)
                    guessed_word = get_guessed_word(secret_word, guessed_letters)
                    print("You already guessed that letter! You lost a warning!", guessed_word)

                else:
                    guess_count -= 1
                    guessed_letters.append(guess)
                    print("Guesses left:", guess_count)
                    get_available_letters(guessed_letters)
                    guessed_word = get_guessed_word(secret_word, guessed_letters)
                    word_complete_string = ''.join(guessed_word)

                    if word_complete_string == secret_word:
                        print("you got the word!", guessed_word)
                    else:
                        guess_count -= 1
                        correct_letters.append(guess)
                        cl = len(correct_letters)
                        print("Good guess!", guessed_word)
                        if cl >= 1:
                            print("Enter a * for a hint")
    if guess_count == 0:
        print("Sorry you didn't get the word.")
        print("The word was:", secret_word)


if __name__ == "__main__":
    secret_word = 'apple'
    hangman_with_hints(secret_word)
###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

# secret_word = choose_word(wordlist)
# hangman_with_hints(secret_word)
