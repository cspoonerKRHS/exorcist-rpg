# NPC's #


## Description ##

These are people that you as the player can interact with. They can sell you things, but, occasionally, some of them will turn into demons.

## Fucntions ##

NPC(images, location, screenSize, waitMax = 100)
  1. images-all of the images for animations
  1. location-where the NPC is in the screen/game
  1. screenSize-the size of the screen
  1. waitMax-the time in-between each animation
  * Functions:
    1. playerLocation-detection field to detect if the player is closen to them
    1. animate-the animation function; it causes the NPC to do the animation
    1. interact-if the player is close enough, the player can interact with the NPC