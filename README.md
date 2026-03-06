# Hangman Game – Python Project

## Project Overview
This project is a command-line implementation of the classic Hangman word guessing game developed using Python. The game randomly selects a word from a predefined word list and challenges the player to guess the letters of the word before running out of lives.

The purpose of this project is to demonstrate fundamental programming concepts such as functions, loops, conditional statements, input validation, modular code design, and basic game logic.

The player attempts to reveal a hidden word by guessing one letter at a time. Each incorrect guess reduces the player's remaining lives. The player wins if they successfully guess the word before running out of lives.

## Game Features
- Random word selection from a predefined word list
- Interactive command-line gameplay
- Hangman ASCII art showing remaining lives
- Input validation to prevent invalid user entries
- Detection of repeated guesses
- Modular code using multiple functions
- Game statistics tracking wins and losses
- Ability to play multiple rounds in one session

## Programming Concepts Demonstrated

### Modular Programming
The program uses multiple functions to organise the game logic and make the code easier to read and maintain.

Functions used include:
- choose_word() – randomly selects a word from the word list
- display_word() – generates the visible word display for the player
- play_game() – contains the main gameplay logic
- show_statistics() – displays overall game statistics

### Input Validation and Error Handling
The program validates all player inputs to prevent unexpected behaviour or program crashes.

The game ensures that:
- The player enters only one letter
- The input contains alphabetical characters only
- Previously guessed letters cannot be guessed again

This ensures the program runs smoothly and provides helpful feedback to the user.

### Global Counters and Game Statistics
Global variables are used to track the player's performance across multiple rounds.

The statistics recorded include:
- Total games played
- Number of games won
- Number of games lost

These statistics are displayed after the player finishes playing.

## Project Structure
Hangman_Project
│
├── Hangman.py        - Main game script
├── Word_List.py      - Word bank used in the game
├── Hangman_Art.py    - ASCII art representing hangman stages
├── FlowChart_Hangman.png  - Flowchart showing the game logic
├── README.md         - Project documentation

## How to Run the Game
1. Ensure Python 3 is installed on your computer.
2. Download or clone the project repository.
3. Open a terminal or command prompt.
4. Navigate to the project folder.
5. Run the game using the following command:

python Hangman.py

## How to Play
1. The program randomly selects a hidden word.
2. The player guesses one letter at a time.
3. Correct guesses reveal the letter in the word.
4. Incorrect guesses reduce the number of remaining lives.
5. The game ends when:
   - the player successfully guesses the entire word, or
   - the player runs out of lives.

After each round, the player can choose to play another game.

## Flowchart
A flowchart was created during the design phase of this project to illustrate the structure and logic of the game. The flowchart outlines the process of word selection, player input, guess validation, and the conditions that determine whether the player wins or loses the game.

## Possible Future Improvements
Potential improvements that could be implemented in future versions include:
- Adding a graphical user interface (GUI) using Tkinter or Pygame
- Adding difficulty levels with different word banks
- Implementing a scoring system
- Adding sound effects or animations
- Creating timed gameplay modes

## Author
Developed as part of a Python programming project focused on learning core programming concepts through game development.