# Step it Up!


## Demo
Demo Video: <https://youtu.be/m13xUGVz6Z4>

## GitHub Repository
GitHub Repo: <https://github.com/Valeo0/pfda_FinalProject_StepItUP.git>

## Description
This project is called “Step it Up!”
It is a fun easy going arrow rhythm game that brings the player into the display where arrows show the cardinal directions Up, Down, Left, Right. 
The player must hit the arrows at the correct timing indicated on the red line to receive a point. 
This is shown on the right hand corner labeled “Player Score”. If the player does not time the input of the arrow keys correctly, or inputs the incorrect arrow key direction the player will receive one STRIKE. Shown in the center top of the window labeled “Strikes”.
 Strikes are shown as red X’s. If the player received in total 3 strikes then a “game over” window will appear on screen. The game over window of the screen indicates that the game event is over, and will also display the final score that the player received while playing the game. 

To further explain the inner workings of the game let's talk about the main file, the “game.py” file. In the game.py file is where the meat and potatoes of the Step It Up! Game begins. Here we have all the screen dimensions, properties of the arrows including, speed, size and a class Arrow that sets the path and positioning. Most notably is the variable arrow_directions which holds our png files for the arrow images.

For the arrow images you will see in the src folder depository I included png files of the up, down,left, and right arrow directions, with a transparent background. Using these images I was able to effectively match the correct directions with the appropriate key inputs which will come into play later on. 

Some design considerations I made sure to include was the framerate and flow of the arrows on screen. I wanted to make sure that there were no dead pixels that would eat up frame rate, and also made sure to delete unused arrows when not needed. This was later utilized in my update features in the Arrow class. 
Also using the dt variable to correctly update the frame rate of my arrows as they traveled down so there would be no further lag as the game progressed. 
In the main function here is where much of the main game functionality is stored. I kept the score and strike variables as well as their surfaces using pygame.font attributes and would then use .blit to display them on the screen surface. 

One of the key new features I had to learn when working on this project was the event.key feature. This feature was crucial to the fundamentals of the game, and making sure that the character's input needed to match the direction of the arrows to receive a point. Also new was the .render feature from pygame fonts features which I utilized for the display and making sure they were in proper position. 

Lastly, one of the design features I most liked for the aesthetics is the game_over_screen png, which I made separately but used pixel brushes to make graffiti style arrows in theme with the arrow rhythm game motif. 

In the future, if I were to improve some features I would’ve liked to implement are penalties for not inputting the arrows at all, so that if they pass the red line it would count as a strike against the player. Also more aesthetical choices like music, or faster arrow speeds as time passes to create more difficulties for the player. 
