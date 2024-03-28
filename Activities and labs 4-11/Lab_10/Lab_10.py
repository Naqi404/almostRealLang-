import random

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

def playGame():
  global dice1
  global dice2
  name = requestString("What is your name?")
  gameActive = true
  while gameActive == true:
    if (dice1 + dice2) == 7 or 11:
      printNow(str(dice1) + str(dice2)+ ' = ' + str(dice1+dice2))
      printNow("You insta win!")
      raw_input()
      goAgain = requestString("Would you like to play again? Y/N...")
      if goAgain == "Y":
        playGame()
      if goAgain == "N":
        printNow("Thanks for playing " + name + "!")
        gameActive = false
        return gameActive
    elif dice1 + dice2 == 2 or 3 or 12:
      printNow("You insta lose :(")
    
    point = dice1 + dice2
    game = true
    while game == true:
      if dice1 + dice2 == point:
        printNow("You win!")
        game = false
        return game
      if dice1 + dice2 == 11 or 7:
        printNow("Game over!")
        game = false
        return game
    while goAgain == "Y" or "N":
      goAgain = requestString("Would you like to play again? Y/N...")
      if goAgain == "Y":
        playGame()
      elif goAgain == "N":
        printNow("Thanks for playing " + name + "!")
        break
      else:
        goAgain = requestString("That was not an option. Y/N...?")