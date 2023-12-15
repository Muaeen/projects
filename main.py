# Importing Necessarylibraries
import random
import yaml

from wordsGenerater import createName

def load_config():
    with open("config.yaml", "r") as f:
        return yaml.safe_load(f)

def main():

    createName()
    config = load_config()

    # Opening the 'names.txt' file in read mode
    with open("names.txt", 'r') as f:
        words = f.readlines() # Reading all lines in the file into a list

    # Choosing a random word from the list and removing the trailing newline character
    word = random.choice(words)[:-1]

    # Setting the number of allowed errors
    allowed_errors = config['rolls']['allowed_errors']
    # Initializing an empty list to keep track of guesses
    guesses = []
    # Flag to indicate whether the game is done or not
    done = False 

    # Starting the main game loop
    while not done:
        # Printing the word with guessed letters revealed and unguessed as underscores
        for letter in word :
            if letter.lower() in guesses:
                print(letter, end=' ')
            else:
                print("_", end=" ")
        print("")

        # Asking the user for their next guess
        guess = input(f"Allowed Errors Left {allowed_errors}, Next Guess: ")
        # Adding the guessed letter to the list of guesses
        guesses.append(guess.lower())

        # Reducing the number of allowed errors if the guess is incorrect
        if guess.lower() not in word.lower():
            allowed_errors -= 1
            # Ending the game if no errors are left
            if allowed_errors == 0:
                break

        # Checking if all letters in the word have been guessed
        done = True
        for letter in word:
            if letter.lower() not in guesses:
                done = False 

    # Printing the result at the end of the game
    if done:
        print(f"You found the word! It was {word}")
    else:
        print(f" Game Over! the word was {word} and you got {guesses}")


if __name__ == "__main__":
    main()