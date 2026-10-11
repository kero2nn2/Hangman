import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------


def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
	# TODO Mena
	# file name is words.txt

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    returns: a word from wordlist at random
    """
	# TODO Mena
    pass


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()


def has_player_won(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    """
	#TODO Youssef
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def get_word_progress(secret_word, letters_guessed):
    """
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    """
	#TODO Mohammed
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass


def get_available_letters(letters_guessed):
    """
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    """
	#TODO Emad
    # FILL IN YOUR CODE HERE AND DELETE "pass"



def reveal_a_letter(secret_word, letters_guessed): 

		available_letters = []

		for letter in secret_word : 
			if letter not in letters_guessed : 
				avilable_letters.append(letter)

		return random.choice(avialble_letters)


def get_score(guesses, secret_word):

	num_of_unique_letters = len(set(secret_word))
	guesses_remaining = 10 - guesses
    return (guesses_remaining + 4 * num_of_unique_letters )	+ ( 3 * len(secret_word) ) 
	

def hangman(secret_word, with_help):
	"""
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '!'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol !, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
	"""
	#TODO Shenouda
	print("Welecome to Hangman!")
	print(f"I am thinking of a word that is {len(secret_word)} letters long")
	print("----------")
	
	guesses = 10
	letters_guessed = [] 

	while guesses > 0 : 
		print(f"You currently have {guesses} left")
		print(f"Available letters: {get_available_letters(letters_guessed)}")

		letter = input("Please guess a letter: ").lower()

		if letter not in string.ascii_lowercase :
			if with_help and letter == '!' :
				if guessed >= 3 :  
					letter_revealed = reveal_a_leater(secret_word, letters_guessed)
					letters_guessed.append(letter_revealed)
					print(f"Letter revealed: {letter_revealed}")
					letters_guessed.append(letter_revealed)	
					print(f"{get_word_progress(secret_word, letter_guessed)}")
					guesses -= 3

				else : 
					print(f"Opps! Not engough guesses: {get_word_progress(secret_word, letters_guessed)}")

			else : 
				print(f"Opps! That is not a valid letter. Please input a letter from\
the alphabet: {get_word_progress(secret_word, letters_guessed)}")

		else : 
			if letter in letters_guessed : 
				print(f"Opps! You have guessed this letter before: {get_word_progress(secret_word, letters_guessed)}")

			else : 
				if letter in secret_word : 
					print(f"Good Guess: {get_word_progress(secret_word, letters_guessed)}")
					letters_guessed.append(letter)

				else : 
					print(f"Opps! That letter is not in my word: {get_word_progress(secret_word, letters_guessed)}")
					letters_guessed.append(letter)

					if letter in "aeoui" : 
						guesses -= 2

					else : 
						guesses -= 1

	if has_player_won() : 
		print("Congratulations, you won!")	
		print(f"Your total score for this game is: {get_score(guesses, secret_word)}")	
					
										
if __name__ == "__main__":
    # To test your game, uncomment the following three lines.

    # secret_word = choose_word(wordlist)
    # with_help = False
    # hangman(secret_word, with_help)
	#TODO Leave it
    pass

