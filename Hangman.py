"""
Hangman Game

This module runs a command-line Hangman game where the player guesses letters
to reveal a hidden word. The program tracks statistics across multiple rounds,
including games played, won, and lost.
"""

# Import the random module to allow the program to choose a random word
import random

# Import the word list and hangman art from the other project files
from Word_List import word_list
from Hangman_Art import stages, logo


# -----------------------------
# GLOBAL STATISTICS COUNTERS
# These track the player's performance across multiple games
# -----------------------------
games_played = 0
games_won = 0
games_lost = 0


def choose_word():
    """
    Select and return a random word from the word list.

    Returns:
        str: A randomly chosen word from the imported word_list.
    """
    return random.choice(word_list)


def display_word(secret_word, guessed_letters):
    """
    Generate the current visible version of the word.

    Letters that have been guessed correctly are displayed,
    while unguessed letters are replaced with underscores.

    Args:
        secret_word (str): The word the player is trying to guess.
        guessed_letters (list): Letters the player has guessed correctly.

    Returns:
        str: The formatted word display showing guessed letters and underscores.
    """

    display = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"

    return display


def play_game():
    """
    Run a single round of the Hangman game.

    The function selects a random word, manages player guesses,
    tracks remaining lives, and determines win or loss conditions.
    It also updates the global statistics for games played,
    games won, and games lost.
    """

    global games_played
    global games_won
    global games_lost

    # Increase the number of games played
    games_played += 1

    # The player starts with 6 lives
    lives = 6

    # Select a random word from the word list
    chosen_word = choose_word()

    # Lists to store guessed letters
    guessed_letters = []
    wrong_letters = []

    # Display the game logo and welcome message
    print(logo)
    print("Welcome to Hangman! You have 6 lives, tread carefully!")

    # Create the starting blank placeholder
    placeholder = ""
    for letter in chosen_word:
        placeholder += "_"

    print("Word to guess:", placeholder)

    game_over = False

    # -----------------------------
    # MAIN GAME LOOP
    # Continues until the player wins or loses
    # -----------------------------
    while not game_over:

        print(f"\nLives remaining: {lives}/6")

        # Ask the player to guess a letter
        guess = input("Guess a letter:\n").lower()

        # -----------------------------
        # INPUT VALIDATION
        # Ensures the player enters only one letter
        # -----------------------------
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue

        # Prevent the player from guessing the same letter again
        if guess in guessed_letters or guess in wrong_letters:
            print("You have already guessed that letter. Try again.")
            continue

        # Check if the guessed letter is in the chosen word
        if guess in chosen_word:
            guessed_letters.append(guess)
        else:
            wrong_letters.append(guess)
            lives -= 1
            print(f"You guessed '{guess}', that's not in the word. You lose a life.")

        # Update the displayed word
        current_display = display_word(chosen_word, guessed_letters)

        print("Word to guess:", current_display)

        # -----------------------------
        # LOSE CONDITION
        # Player runs out of lives
        # -----------------------------
        if lives == 0:
            games_lost += 1
            game_over = True
            print(f"\nGame Over! The word was '{chosen_word}'.")

        # -----------------------------
        # WIN CONDITION
        # Player has guessed the entire word
        # -----------------------------
        if "_" not in current_display:
            games_won += 1
            game_over = True
            print("\nCongratulations! You guessed the word!")

        # Display the hangman stage based on remaining lives
        print(stages[lives])


def show_statistics():
    """
    Display the player's overall game statistics.

    Shows the total number of games played, won, and lost
    during the current program session.
    """

    print("\n------ Game Statistics ------")
    print(f"Games Played: {games_played}")
    print(f"Games Won: {games_won}")
    print(f"Games Lost: {games_lost}")
    print("-----------------------------")


# -----------------------------
# MAIN PROGRAM LOOP
# Allows the player to play multiple rounds
# -----------------------------
while True:

    # Run one game round
    play_game()

    # Ask if the player wants to play another round
    again = input("\nDo you want to play again? (y/n): ").lower()

    # If the player enters anything other than 'y', exit the loop
    if again != "y":
        break


# After the player finishes playing, show overall statistics
show_statistics()