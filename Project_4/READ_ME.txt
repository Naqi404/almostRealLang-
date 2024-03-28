

For the purpose of documentation and efficiency, this file contains:
1. The optimal route for the game if needed.
2. Additional features added to the program.
3. The pieces of the rubric that were attempted, and the pieces that were not.




1. The optimal Route:
	Starting from Main Hallway, the fastest way to clear the game is to go to:
		1. Eat the food on the table in Main.
		2. Take a flower from the table in NW -> N (Break Room)
		3. Returning to the Main Area and then heading NE, then heading E, then N.
		4. Selecting the option "bed" as it contains the strongest weapon.
		5. Heading S, until you get the prompt for the War Room.
		6. Typing "dive" once prompted.
2. The Combat Mechanics:
	This game will include one combat sequence:
		1. The combat sequence used the random import to simulate dice throws.
		2. The mechanics loosely resemble Dungeons and Dragons mechanics.
		3. You can get hit, you can dodge, you can die. Same goes for the opponent. RNG can be lethal if die rolls are bad.


3. The Rubric(Short version):
		The full overview is under this section, but for the sake of not having to read through everything.
		
		Attemped/Done: (1 - 17), (21,22a,22c) All others not done.



















	
3. The Rubric:
	Since this is a very large program, I wanted to make things easier and list the things I did and did not attempt.

1. (D) ALL of your files for the project are placed into a single folder named project4. Don’t forget the reflection paper, etc. Compress (zip) this folder, creating project4.zip. 
	Submit this compressed folder.
	
	Done

2. (D) Reflection paper. See Canvas for a description of its content.

	Done

3. (D) All needed files are submitted, including the required image and sound files, and library files, if used.
	
	Done

4. (D) All images and sounds used in your game must satisfy one or more of the following: (see the long description)
a. You own the image or sound, or you have documented permission from the copyright holder to use it.
b. The image is included in the “JPG Images.zip” or the sound is included in the “WAV sounds.zip” file provided in the CS 120 area of Canvas.
c. The image or sound is available royalty-free in the public domain.

	The resources I used satisfy all these conditions.

5a. (D) Submitted program will load in JES.

	Done

5b. (D) Submitted program will run in JES.
	
	Done

7a. (C) Submitted program has a main function named adventure() which starts the game.

	Done

7b. (C) Submitted program does not prompt for any media input, but rather has all image and sound files specified in your code, and makes use of the getMediaPath() function.

	Done

7c. (C) Submitted program includes reasonable documentation comments, as appropriate. At a minimum, include comments at the start of the code file that includes your name and 
	the date. Additional comments may be included in your code similar to those used by the author in the text book.

	Done, at least in my opinion it contains good documentation.

7d. (C) Submited program is formatted/indented, similar to the text book authors’ examples.

	Done

8. (C) After the game has started a floor plan or map is displayed.

	Done; A full map that I purchased for Dungeons and Dragons is used for this game.

9a. (C) As the player enters a room or area a related sound plays.
	
	Done

9b. (C) As the player enters a room or area possible valid movements are described.

	Done; movements are based on a compass scale.

9c. (C) As the player enters a room or area attempts to make an invalid move are described as invalid.

	Done; appropriate Error messages are set in place.

10a. (C) At the end of the game there is a way to win or lose.

	Done. To win: Find all memories and unlock the ending. Lose: If you die or quit.

10b. (C) At the end of the game the player is told if they won or lost.
	
	Done

10c. (C) At the end of the game a score is calculated and displayed. How the score is calculated is left up to you.

	Done

12a. (B) Submitted program uses descriptive function and variable names.

	Done; All function and variable names are correspondant and appropriate.

12b. (B) Submitted program is appropriately hierarchically decomposed.

	Done

13. (B) As the player enters a room or area an image of the room or area is displayed on the floor plan or map.

	(Optional) Display a “you are here” symbol (such as an “X”) on the floor plan/map. This symbol “moves” as the player moves.

	NOTE: since I used an image that essentially was it's own image, I went with the additional Optional objective and used variable images of the same one.
	This was done to show I know how to do this, and I used the process. While still maintaining the Aesthetic of the game I wanted.

14. (B) Upon re-entering the same room/area later the sound does not automatically play.

	Done; Using global variables I used the appropriate logic to determine if it was the first time entering or not.
	
	This can be displayed in the following rooms:
		1. Main Hallway
		2. Kitchen

	This can also be displayed at a different scale in all the memory functions are they use the same process to prevent score farming.

15. (B) Multiple image windows are not open at the same time. Use the repaint() function to redisplay the same image name each time.

	Done; Repaint is used to not open more than one instance.

16. (B) At the end of the game the player’s score is stored in a file, along with the player’s name. Previous entries in the file are not changed.
	Hint: read the data from the file and store it in a list, then write it from the list to the file, as needed.
	
	Done; scores are stored in the file scores.txt in the media folder.

17. (B) There are at least two items scattered around the house/world. The player has a way to know an item is available to them.
	a. The items may be mentioned in the text provided when entering a room/area.
	b. The items may be shown in the image provided when entering a room/area.
	
	DONE: Items present in on the map; 4 memories, 3 weapons.

	a/b: Done (Some items are based off the map environment. Such as Flowers in Break Room. All items have text notifications.)

19. (A) Submitted program utilizes the provided SoundLib.py library file and its functions, where appropriate. Functions included in this library file should not be duplicated in your code file.

	It does not, I didn't need them in my program and did not use them or import them.

20. (A) At the end of the game, if the player has played before, and they earned a better score this time, then the file is updated, rather than adding the player a second time. If their current score is the same or worse, 
	nothing is changed in the file. Hint: read the data in from the file and store it in a list, then write it from the list back to the file, as needed.

	Did not attempt.

21a. (A) During the game the player can display their current score.

	Done

22a. (A) There are at least two items scattered around the house/world and there is a way to pick up an item.

	Done

22b. (A) There are at least two items scattered around the house/world and there is a way to put down an item (and then the game needs to remember where it was left).

	Did not attempt

22c. (A) There are at least two items scattered around the house/world and there is a way to use at least one item. For example, a key found in one room may unlock a door elsewhere.

	Done: Memories are required items to get to the final point. Memories are the items in this case that do this.
