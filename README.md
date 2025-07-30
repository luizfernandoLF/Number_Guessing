Number Guessing Game

About the Game

Welcome to the Number Guessing Game! This is a classic and fun CLI-based game where the computer thinks of a random number, and your goal is to guess what it is. 

The game features:

    A randomly generated number between 1 and 100.

    Three difficulty levels: Easy, Medium, and Hard, each giving you a different number of chances.

Game Rules

    The computer will choose a secret number between 1 and 100.

    You will be prompted to select a difficulty level:

        Easy: 10 chances

        Medium: 5 chances

        Hard: 3 chances

    After choosing the difficulty, you'll start guessing the number.

    The game will tell you if your guess is too high or too low.

    If you guess the correct number within your allotted chances, you win!

    If you run out of chances before guessing correctly, you lose.

 How to Play

    Clone the repository:

    git clone github.com/luizfernandoLF/Number_Guessing
    

Navigate to the project directory:
Bash

cd number-guessing-game

Run the game:
Bash

    python number_guessing_game.py

    Follow the on-screen instructions to play!

 Technologies Used

    Python 3

Future Improvements 

Here are some ideas for future enhancements:

    Allow the user to play multiple rounds of the game (i.e., keep playing until the user decides to quit). You can do this by asking the user if they want to play again after each round.
    Add a timer to see how long it takes the user to guess the number.
    Implement a hint system that provides clues to the user if they are stuck.
    Keep track of the user’s high score (i.e., the fewest number of attempts it took to guess the number under a specific difficulty level).
