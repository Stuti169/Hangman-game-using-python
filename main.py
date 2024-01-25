import random

# Import the word list from hangman_words.py
from hangman_words import word_list

# Choose a random word from the word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

# Create blanks for the display
display = []
for _ in range(word_length):
    display += "_"

# Main game loop
while not end_of_game:
    # Ask the user to guess a letter
    guess = input("Guess a letter: ").lower()

    # Check if the user has already guessed the letter
    if guess in display:
        print(f"You've already guessed {guess}")

    # Check each position in the chosen_word for the guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            # If the guessed letter matches a letter in the word, update the display
            display[position] = letter

    # Check if the user's guess is incorrect
    if guess not in chosen_word:
        # If the letter is not in the chosen_word, print it and deduct a life
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")

    # Display the current state of the word
    print(f"{' '.join(display)}")

    # Check if the user has guessed all letters in the word
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # Import the stages from hangman_art.py and print the current stage based on remaining lives.
    from hangman_art import stages
    print(stages[lives])
