# Flappy-Bird
We all our familiar with one of the most famous and one of the most difficult game to score *FLAPPY BIRD*. In this game there are multiple pipes through which we have to take our bird without touching the pipes. 
# Installation
Download the complete folder and save it anywhere on your desktop. Open the file named main.py in a any python IDE such as pycharm, anaconda etc.

Install pygame, sys and random libraries in your interpreter if they are not present. Once installed, you're ready to use the software.
# Basic Summary
Once you run the code, a new window will open up and software will be launched, you just need to tap on the screen to start the game. Tshe more you tap the more the bird goes up. Save the bird from colliding with the pipes, the more pipes you cross the more you score. Your score is displayed on the top of the screen.

The game will end one you hit any pipe or you close the window.
# Code Explanation
* Welcome Screen:- This functions sets up our welcome screen or the first window which opens up after running the project
* Main game :- This function sets up our whole game like positioning of base pipes bird etc. Also all the sounds used in the game is managed by this function.
* isCollide :- This function decides what to do after we collide with the pipe.
* getrandompipe :- This functions fetches the pipes of random length so as to make the game interesting and difficult.
* main function :- This functions compiles all the files and call our functions for the game to work.
