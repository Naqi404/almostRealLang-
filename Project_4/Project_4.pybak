#######################
#Naqi Nadeem
#Note: I hold rights to the image used in this game, and I have permission from the creators to use it for small private games.
#######################
import random
#######################################
##Global Variables
name = "????"
health = 100
weapon = 'Fists'
score = 0
gold = 0
memory1 = 0
memory2 = 0
memory3 = 0
memory4 = 0
monster = 0
enemyHealth = 250
visit = 0
rest = 0
map = makeEmptyPicture(592,505)
finalScore = 0
#######################################

#######################################
#Saving scores to a text file And reading Saved Scores
#######################################
def saveFile():
  global name
  global finalScore
  file = open(getMediaPath('scores.txt'), 'a')
  file.write(name + " -- " + str(finalScore) + ' \n')
  file.close()
def seeScores():
  reqS = requestString("If you would like to see old scores enter Y, if not enter N.")
  if reqS == 'Y':
    readScores()
  else:
    printNow("You chose not to see old scores this time.")


########################################
def readScores():
  inFile = open(getMediaPath('scores.txt'), 'rt')
  PastScores = inFile.read()
  inFile.close()
  print(PastScores)
########################################

def adventure(): #tests cleared
  location = "Front Gate"
  seeScores()
  showIntro()
  memory = 0
  while not (location == "Exit")or(location == "Finish"):
    showRoom(location)
    reallyShowRoom(location)
    if location != "Finish":
      direction = requestString("Where do you want to go next?")
      printNow("You entered: " + direction)
      location = pickRoom(direction, location)


def showIntro():
  raw_input("Anytime there is a pause in the dialogue, just press Enter to continue.")
  printNow("This is a text based exploration game.")
  raw_input()
  printNow("The objective of this game is to find your lost memories, you may go across the map looking for them.")
  raw_input()
  printNow("The basic controls of the game will be to use compass directions to explore the map.")
  raw_input()
  printNow("The basic directions: North(N) West(W) East(E) South(S). Combined directions such as NorthEast(NE) and NorthWest(NW) may also be used.")
  raw_input()
  printNow("For help: Type 'help' when necessary. To view past scores type: ")
  printNow("To uncover the ending, find all your memories but beware... you are warned.")
  
###################
#Show Inventory and stats/code the weapon damage functions using the random import
###################
def showStats():
  global name
  global weapon
  global health
  global score
  global finalScore
  printNow("Name: " + name)
  printNow("Weapon: " + weapon)
  printNow("Health: " + str(health) +"/100")
  printNow("Score: "+ str(score))
  raw_input()
  if health >=0:
    finalScore = (health*20)+(gold*10)+score
  else:
    finalScore = (gold*10)+score
  printNow("Your Final Score for this game was: " + str(finalScore))
###################
#STATS AND INVENTORY END
###################

def showRoom(room): #tests cleared
  printNow("======================================")
  raw_input()
  if room == "Front Gate":
    showFrontGate()
  if room == "Main Hall":
    showMainHall()
  if room == "Main Hall(revisited)":
    showMainHall2()
  if room == "Joint Bedroom":
    showJB()
  if room == "Kitchen Hall":
    showKitchenHall()  
  if room == "Kitchen":
    showKitchen()
  if room == "Break Room":
    showBreakRoom()
  if room == "Study":
    showStudy()
  if room == "Private Rooms":
    showPrivateRooms()
  if room == "EastHall":
    showEastHall()
  if room == "Master Bedroom":
    showMasterBR()
  if room == "War room":
    showWR()
  if room == "Stage":
    showStage()
  if room == "Southeastern Hallway":
    showSEHall()
  if room == "Finish":
    showExitSequence()
    
##########################
#Room Picker
##########################
def pickRoom(direction, room):
  global health
  global visit
  global name
  if health <= 0:
    showStats()
    printNow("Unfortunately... or fortunately. Dead people can't go anywhere. GAME OVER: YOU LOSE Please Restart.")
    name = requestString("But.. before the light go out. Can I get your name? ")
    saveFile()
    return "Exit"
  if (direction == "quit") or (direction == "exit"):
    printNow("Goodbye... Coward~~ GAME OVER: YOU LOSE")
    saveFile() #Yes, this game you can lose by not playing
    return "Exit"
  if direction == "help":
    showIntro()
    return room
  if room == "Front Gate":
    if visit == 0:
      if direction == "N":
        return "Main Hall"
    if visit == 1:
      return "Main Hall(revisited)"
  #Main room, it has six possible directions.
  elif room == "Main Hall":
    if direction == "N":
      return "Stage"
    if direction == "S":
      return "Front Gate"
    if direction == "SW":
      return "Joint Bedroom"
    if direction == "SE":
      return "Study"
    if direction == "NW":
      return "Kitchen Hall"
    if direction == "NE":
      return "Private Rooms"
  elif room == "Main Hall(revisited)":
    if direction == "N":
      return "Stage"
    if direction == "S":
      return "Front Gate"
    if direction == "SW":
      return "Joint Bedroom"
    if direction == "SE":
      return "Study"
    if direction == "NW":
      return "Kitchen Hall"
    if direction == "NE":
      return "Private Rooms"
  #Sub rooms, i.e single entrance/single exits looping back to the main hall
  elif room == "Stage":
    if direction == "S":
      return "Main Hall(revisited)"
  elif room == "Joint Bedroom":
    if direction == "E":
      return "Main Hall(revisited)"
  elif room == "Study":
    if direction == "W":
      return "Main Hall(revisited)"
  #Western Branch for rooms
  elif room == "Kitchen Hall":
    if direction == "N":
      return "Break Room"
    if direction == "S":
      return "Kitchen"
    if direction == "E":
      return "Main Hall(revisited)"
  elif room == "Kitchen":
    if direction == "N":
      return "Kitchen Hall"
  elif room == "Break Room":
    if direction == "S":
      return "Kitchen Hall"
  #Eastern Branch for rooms
  elif room == "Private Rooms":
    if direction == "W":
      return "Main Hall(revisited)"
    if direction == "E":
      return "EastHall"
      
  elif room == "EastHall":
    if direction == "W":
      return "Private Rooms"
    if direction == "N":
      return "Master Bedroom"
    if direction == "S":
      return "Southeastern Hallway"
  elif room == "Master Bedroom":
    if direction == "S" or "s":
      return "Southeastern Hallway"
  elif room == "Southeastern Hallway":
    if direction == "N":
      return "EastHall"
    if direction == "SE" or "se":
      return "War room"
  elif room == "War room":
    if direction == "W":
      return "Southeastern Hallway"
    if direction == "dive" or "DIVE":
      return "Finish"
  printNow("Something went wrong. Unexpected input error.")
  return room
#####################################################
#The section of the code where I type the descriptions of each location.
#####################################################
def showFrontGate():
  printNow("Your eyes open.")
  raw_input()
  printNow("You are in an unfamiliar place, the sound of rain and thunder surrounds you.")
  raw_input()
  printNow("You have no memory of what last happened, you simply remember you were walking down the street one moment.")
  raw_input()
  printNow("And now you are here. On this dark, secluded dirt road.")
  raw_input()
  printNow("In front of you stands a manor. One which by the looks of things, is as old as it is large.")
  raw_input()
  printNow("It is freezing cold. You can think about what happened later. First you decide to find some cover from the rain.")
  raw_input()
  printNow("You sit yourself down on the entryway of this manor, in front of the door.")
  raw_input()
  printNow("Before you get a chance to gather your thoughts. *Fwip* The lanterns on either side of the door light up, and the doors swing open.")
  raw_input()
  printNow("As the doors open, you are greeted with a warm breeze, a welcome feeling as opposed to standing out in the rain.")
  raw_input()
  printNow("To begin the game, type a direction. Directions are single letter directions such as N W E S. Start by typing N to go in.")
  raw_input()
  printNow("Or... if you're a coward who wants to stay out in the cold rain, type quit or exit")

#########################
#MAIN HALL DIALOGUE + MAIN HALL MEMORY FUNCTION + MAIN HALL REVISITED
###################
def showMainHall():
  global memory1
  global visit
  global score
  if visit == 0:
    thunder = makeSound(getMediaPath("Thunder.wav"))
    blockingPlay(thunder)
    visit = 1
  printNow("You enter inside. The place is well lit, warm. You can hear the comforting crackling of wood as your body now feels better.")
  raw_input()
  printNow("Your eyes widen, as you see before you a massive hall, which houses the largest table you have ever seen.")
  raw_input()
  printNow("On the table you see a feast. Fresh food of all sorts, aromatic and crisp.")
  raw_input()
  while memory1 == 0:
    food = requestString("Do you want to sit down and eat? Y/N...")
    while food == "Y" or "N":
      if food == "Y":
        printNow("The food tasted delicious. But not only that, you recovered your first memory from eating the food.")
        raw_input()
        printNow("You were at your favorite restaurant a few hours ago, you had just had lunch with a dear friend.")
        raw_input()
        printNow("Memory acquired!")
        memory1 = 1
        break
        score = score + 50
      elif food == "N":
        printNow("Yeah maybe later, this isn't even your house afterall.")
        break
      else:
        food = requestString("That is not an option, enter Y/N...")    
  raw_input()
  printNow("You are presented with a few choices on where to go next.")
  printNow("To the N is a stage with the fireplace.\n"+ "To the SW and NW there is a room and a hallway.")
  printNow("To the NE/NW there is another room and another hallway,")
  printNow("S is where you came from")

def showMainHall2():
  printNow("You're back in the Main Hall. Where so you want to go now?")
  raw_input()
  printNow("To the N is a stage with the fireplace.\n"+ "To the SW and NW there is a room and a hallway.\n" + "To the NE/NW there is another room and another hallway,\n"+"S is where you came from")

##################
#Stage Dialogue
##################
def showStage():
  global score
  global rest
  global gold
  printNow("You move up, getting closer to the place that houses the fireplace.")
  raw_input()
  printNow("Before you is a magnificently lit flame, of top of which is hung the large head of some animal you've never seen before.")
  raw_input()
  if rest == 0:
    fire = requestString("Would you like to sit down next to the fire for a bit? Y/N...")
    while fire == "Y" or "N":
      if fire == "Y":
        printNow("The warmth of the fire soothes you. Plus you found a small coin pouch under a pillow!")
        score = score + 100
        gold = gold +20
        break
      elif fire == "N":
        printNow("I should really get back to finding out what is going on.")
        break
      else:
        fire = requestString("That wasn't an option. Do you wanna sit next to the fire? Y/N...")
  printNow("Want to go back to roaming now? Press S to go back.")
##################
#Southern single rooms
##################
def showStudy():
  global score
  printNow("You enter into what seems to be a study. It seems fairly well organized actually.")
  raw_input()
  notes = requestString("There are some notes left on the table would you like to try and read them? Y/N...")
  while notes == "Y" or "N":
    if notes == "Y":
      printNow("You don't understand anything that these notes say... however there are ominous drawings on the pages. They give you a strange feeling.")
      score = score -50
      break
    elif notes == "N":
      printNow("It would be rude to look at other people's notes.")
      score = score + 50
      break
    else:
      notes = requestString("That wasn't an option. Do you want to read the notes? Y/N...")
  printNow("Okay lets head back. Enter W to continue...")

def showJB():
  printNow("This seems like some sort of joined bedroom, there isn't really much here except for a bunch of empty beds.")
  raw_input()
  printNow("Perhaps this is where the people who work here sleep. Let's go back.")
  raw_input()
  printNow("Enter E to return to the main room")
  
#################
#North Western kitchen side branch
#################
def showKitchenHall():
  printNow("You enter into a hallway where you are presented with three choices.")
  raw_input()
  printNow("To your N, there is a room. And to your S, there seems to be a kitchen. And to your E is back to the main hall.")
  raw_input()
  printNow("Which way will you go?")
  
def showBreakRoom():
  global score
  global memory2
  printNow("You enter into what seems to be some sort of break room.")
  raw_input()
  printNow("On the table you see a vase, and in that vase is a bouquet of flowers.")
  raw_input()
  while memory2 == 0:
    flower = requestString("Do you want to try taking one of those flowers? Y/N...")
    while flower == "Y" or "N":
      if flower == "Y":
        printNow("Flowers... Flowers? Flowers! Another memory! After you finished up with lunch, you stopped at a small flower shop and purchased some flowers!")
        raw_input()
        printNow("You remember now! You bought those flowers for your mother's birthday!")
        score = score + 100
        memory2 = 1
        break
      elif flower == "N":
        printNow("Calm down, they're just some flowers.")
        score = score - 50
        break
      else:
        flower = requestString("That wasn't an option. Do you want to try taking one of those flowers? Y/N...")
  printNow("Want to head back and look around some more? Press S to return to the hallway.")
  raw_input()
  
def showKitchen():
  global monster
  global weapon
  monSound = makeSound(getMediaPath("Monster.wav"))
  printNow("You enter into the kitchen... this must be where they made all the food.")
  raw_input()
  printNow("Wait...")
  raw_input()
  printNow("All this food? But there is no one... anywhere...")
  raw_input()
  printNow("Suddenly a chill runs through your spine. You feel as though there are suddenly eyes on you. Watching your every move.")
  raw_input()
  knife = requestString("You see a knife in front of you. It seems like it was being used to cut vegetables. Do you want to grab it for protection? Y/N...")
  while knife == "Y" or "N":
    if knife == "Y":
      printNow("You quickly pick up the knife and hold is firmly in your hand.")
      weapon = "Knife"
      break
    elif notes == "N":
      printNow("What am I thinking? a kitchen knife? are my enemies vegetables?")
      break
    else:
      knife = printNow("That was not an option. Again, Do you want to grab it for protection? Y/N")
    printNow("You now quickly turn around")
    raw_input()
  if monster == 1:
    printNow("Okay... I don't think it's here any more. Thank God!")
  elif monster == 0:
    blockingPlay(monSound)
    printNow("You see two floating dark eyes at the end of the kitchen.")
    printNow("Blood drips from them, even though there seems to be no head attached to them.")
    monster = 1
    raw_input()
    printNow("Quickly! You must run out of here! You can head back N to return to the Hallway.")
  
#################
#North eastern side branch
#################
def showPrivateRooms():
  global monster
  if monster == 1:
    printNow("You enter this new hallway, distraught and in terror. You calm yourself down for the moment and try to take note of your surroundings.")
    raw_input()
  printNow("This seems to be a bedroom area. There seem to be small individual beds in each of these rooms. It's nothing fancy but to some this could be considered a luxury.")
  raw_input()
  printNow("Continuing forward there is a branching hallway to the E. And back to the mainhall going W.")

def showEastHall():
  printNow("You enter into another hallway. The more you go through this house, the more you become suspicious of it's contents.")
  raw_input()
  printNow("You are presented with two choices for where to go next. To the N, there seems to be a larger bedroom. And to the S, there are a number of other rooms that you can't make out from here.")

def showMasterBR():
  global weapon
  global monster
  global score
  global gold
  printNow("You enter into what seems to be the master bedroom of this manor. It seems very spacious, and seems like it might even have something that could help you figure something out.")
  raw_input()
  printNow("There is a large bed, a dresser, and a chest in this room.")
  if monster == 0 or 1:
    search = requestString("Oh no... you hear something coming towards the room. Look around quick to see if you can find something that might help! Choose between the bed, chest, and dresser...")
    while search == "bed" or "chest" or "dresser":
      if search == "bed":
        printNow("WOAH! Someone hid a sword under the mattress of the bed. Not only that, the blade is made of real silver!")
        raw_input()
        weapon = "Silver Sword"
        break
      elif search == "chest":
        printNow("Oh wow, that is a lot of gold! I wonder if I can pay the monster off...")
        gold = gold + 500
        break
      elif search == "dresser":
        printNow("There is... some sort of book in here? Wait!? This is a magic casting book! I can use this!")
        weapon = "Magic Tome"
        break
      else:
        search = requestString("That was not an option. Choose between the bed, chest, and dresser...")
    raw_input()
    printNow("Well ready or not, here it comes!")
    result = fightSequence()
    if result == "win":
      printNow("Wow that was crazy. But you begin to remember more... right before you woke up here... there was carnage everywhere... people were dying... your friends were dying... What happened...?")
      raw_input()
      printNow("I have to keep moving forward... I need to find my last memory...")
      raw_input()
      monster = 2
      printNow("Continue down the hallway to the S... hopefully there isn't another monster lurking around.") #truthfully there were going to be 4 but I'm at almost 500 lines of code right now
    if result == "loss":
      printNow("Press any key to continue.")
  if monster == 2:
    printNow("Well, I already killed the monster that was in here, I don't really need to worry about anything...")
    
    
###########
#THE FIGHT SEQUENCE FUNCTION
#THIS COMBAT SEQUENCE IS BUILT TO RESEMBLE A SIMPLIFIED VERSION OF DUNGEONS AND DRAGONS COMBAT
#ACCURACY AND DAMAGE CORESPOND TO THE D20 DICE SYSTEM, HOWEVER IF YOU ONLY FIGHT WITH YOUR FISTS, YOU CAN ONLY DO 1 DAMAGE.
###########  
def fightSequence():
  global health
  global weapon
  global enemyHealth
  global memory3
  global gold
  global score
  weaponAttack = 1
  accuracy = 15
  while (enemyHealth > 0) and (health > 0):
    printNow("===========================")
    if weapon == "Knife":
      weaponAttack = random.randint(5, 10)
      accuracy = random.randint(1,20)+3
    if weapon == "Silver Sword":
      weaponAttack = random.randint(30, 60)
      accuracy = random.randint(1,20)+5
    if weapon == "Magic Tome":
      weaponAttack = random.randint(20, 50)
      accuracy = random.randint(1,20)+7
    enemyAttack = random.randint(10, 20)
    enemyAccuracy = random.randint(1,20)+3
    command = requestString("Press (a) to attack")    
    if command == "a":
      if accuracy >= 15:
        damage = weaponAttack
        printNow("You just attacked the monster, dealing " + str(damage) + " damage.")
        enemyHealth = enemyHealth - damage
      else:
        printNow("Oh no you missed!")
      if enemyAccuracy >= 13:
        printNow("The enemy attacks you! You take "+str(enemyAttack)+" damage")
        health = health - enemyAttack
      else:
        printNow("You dodged the attack")
      printNow("You have: "+str(health)+"HP")
      printNow("Enemy has: "+str(enemyHealth)+"HP")
      raw_input()
    else:
      command = requestString("You have no choice but to attack")
  if health <= 0:
    printNow("You have been defeated by the monster!")
    direction = 'exit'
    fightOutcome = 'loss'
    quit()
  if enemyHealth <= 0:
    printNow("You have defeated the enemy!")
    fightOutcome = 'win'
    score = score + 1000
    gold = gold + 100
    memory3 = 1
  return (fightOutcome)

#################
#Time for the final part of the project
#################
def showSEHall():
  global memory1
  global memory2
  global memory3
  global memory4
  global name
  while memory4 == 0:
    if ((memory1 == 1) and (memory2==1) and (memory3 == 1)): 
      printNow("As you walk through this part of the house, your mind is both filled with anxiety, and a sense of melancholy...")
      raw_input()
      printNow("You stop walking for the moment... think to yourself... Wait... Who am I?")
      name = requestString("What was my name...? ")
      printNow("Ah... that's right. How could I forget even my own name? I am " + name + ". Alright, let's finish this.")
      raw_input()
      memory4 = 1
      printNow("Memory number 4: 'Name' acquired!")
      raw_input()
      printNow("Okay enter SE to go to The War room. Press N to go back to the hall.")
    else:
      printNow("You can not go to that part of the map yet! Finish the other parts of the map first.")
      direction = "N"
    printNow("You're just walking down the hall")
    
def showWR():
  printNow("As you walk down the hall, all your memories come flooding back in.")
  raw_input()
  printNow("Every single step you take feels like decade passing by.")
  raw_input()
  printNow("And now you finally remember... you remember who you are. You remember where you were. And most importantly given the current circumstances.")
  raw_input()
  printNow("You know where you are.")
  raw_input()
  printNow("You are Dr. "+name+". The only person who can restore the world to what it once was.")
  raw_input()
  printNow("And this is, the castle of the time lord.")
  raw_input()
  printNow("You are the only one who survived when beasts much like the one you just fought invaded the world.")
  raw_input()
  printNow("You know what you have to do now.")
  raw_input()
  printNow("You must now go back in time, and prevent the world from falling into the hands of these creatures.")
  raw_input()
  printNow("You stand next to the map in the room, the map begins to ripple. What do you do? Type dive to dive back in time.")



def showExitSequence():
  global finalScore
  printNow("Good luck hero...")
  raw_input()
  printNow("We're all counting on you!")
  raw_input()
  printNow("GAME OVER: YOU WIN")
  raw_input()
  showStats()
  saveFile()

##############
#Multimedia Functions
##############
def reallyShowRoom(room):
  global map
  img1 = makePicture(getMediaPath('img1.jpg'))
  img2 = makePicture(getMediaPath('img2.jpg'))
  img3 = makePicture(getMediaPath('img3.jpg'))
  img3Up = makePicture(getMediaPath('img3up.jpg'))
  img3Down = makePicture(getMediaPath('img3Down.jpg'))
  img4 = makePicture(getMediaPath('img4.jpg'))
  img5 = makePicture(getMediaPath('img5.jpg'))
  img6 = makePicture(getMediaPath('img6.jpg'))
  img7 = makePicture(getMediaPath('img7.jpg'))
  img8 = makePicture(getMediaPath('img8.jpg'))
  img9 = makePicture(getMediaPath('img9.jpg'))
  img10 = makePicture(getMediaPath('img10.jpg'))
  img11 = makePicture(getMediaPath('img11.jpg'))
  if room == "Front Gate":
    front = mapper(img1, map)
  if room == "Main Hall":
    main = mapper(img2, map)
  if room == "Main Hall(revisited)":
    mapper(img2, map)
  if room == "Kitchen Hall":
    mapper(img3, map)
  if room == "Break Room":
    mapper(img3Up, map)
  if room == "Kitchen":
    mapper(img3Down, map)
  if room == "Private Rooms":
    mapper(img4, map)
  if room == "Master Bedroom":
    mapper(img5, map)
  if room == "War room":
    mapper(img6, map)
  if room == "Joint Bedroom":
    mapper(img7, map)
  if room == "Stage":
    mapper(img8, map)
  if room == "Study":
    mapper(img9, map)
  if room == "EastHall":
    mapper(img10, map)
  if room == "Southeastern Hallway":
    mapper(img11, map)

def mapper(pic, map):
  hei = 505
  wid = 592
  for x in range(0,wid):
    for y in range(0, hei):
      sourcePX = getPixel(pic, x, y)
      color = getColor(sourcePX)
      tarPX = (getPixel(map, x, y))
      setColor(tarPX, color)
  repaint(map)
