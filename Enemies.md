# Enemies #

## Description ##
These are demons that you as the player will fight.  They were NPC's, but now they are one of two different kinds of demons, one that melee, the other shoots.


## Functions ##

Enemy(images, location, speed, screenSize, health)
  1. images- a list with the images for walking, attack, death
  1. place- the place where it is
  1. speed- the speed at which it moves
  1. screenSize- the size of the screen
  1. health- the amount of health that a demon has
  1. detectRadius- the distance at which the enemies detect the player
  1. waitCount- tells frame which image to use
  1. waitMax- prevents the animations from bugging out and resets them
  1. surfaces- the function that holds all of the loaded images
  1. frame- loads the image
  1. rect- tells the rest of the game how large the enemy is
  1. living- whether the enemy is living or not
  * Functions:
    1. playerDetect- detects if the player is close to them.
    1. move- Exactly what it sounds like, causes an animation
    1. bounce- takes information from Block.py and causes enemies to bounce when they hit blocks.
    1. dir- which direction the enemy is facing
    1. distToPoint- the distance from the center of the enemy to an inputed other
    1. collideWall- tries to collide with the sides, top, and bottom of the screen
    1. enemyCollide- collides with other enemies

**Notes**
**enemy.py is inherited to two other enemies, a black one and a laser-shooting one.**The only difference between these enemies is that the white one shoots lasers, and the black one is bigger.