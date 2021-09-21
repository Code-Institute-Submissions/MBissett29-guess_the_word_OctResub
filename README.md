# Guess the Word

Guess the word is a python terminal game that runs as a mock terminal app provided by Code Institute deployed on Heroku.

The game is based on the classic Hangman game, however instead of a image of a hangman every time you lose a life it just shows how many lives you have remaining.

// Input mock design image of terminal app here 


## How to play

Guess the word is a pretty simple game. It starts off by welcoming the player and asks if they are ready to play.

It will also show  the player how many lives remaining, so they understands how many guesses they have to beat the game.

The game starts of by showing the random word as spaced out underscores for the letters. This shows the player how long the word is.

The player then has the option of guessing a letter each time by typing a letter into the terminal and hitting the enter key.

The game ends either if the player guesses the word and beats the game or the player runs out of lives.

The player then has the option of playing again.

// Input screenshot of the start of the game

## Features

* Random word is generated as underscores.

// Input screen shot of random word

* Life tracker shows how lives are remaining.

// Input screenshot of life tracker

* Player inputs letter to guess in the word.

// Input screenshot of User input

* Input validation
    * Shows player which letters they have used.
    * Shows player if they have chosen the right letter.
    * Shows player if they have incorrectly input something that isnt a letter.
    * Shows player if they win with message.
    * Shows player if they lose with message.

// Input multiple screenshots of Input validation

* Play again feature, allows user to have the option of playing again. By pressing Y and enter they play again, by pressing N the game stops.

// Input screenshot of play again

## Data Model




## Testing

I have passed the code through a [PEP8 validator](http://pep8online.com/) and there are no problems.

// Input Screenshot of PEP8 Validator

Tested the code within local terminal 

// Input Screenshot of local terminal

The code works within the termonal app in Heroku

// Input Screenshot of heroku app terminal

## Deployment

This project was deployed using the Code Institutes mock terminal within Heroku.

* Deployment steps:
    * Used a cloned template for the repository
    * Created a new Heroku app
    * Set the buildpacks to Python and then Node.js in that order
    * Linked the Heroku app to my version of the cloned template
    * Clicked deploy