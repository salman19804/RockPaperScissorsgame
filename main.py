import random


from imagetotext import imgToText

print(imgToText("rock.jpeg"))

def robotchoice():
  return random.randrange(0,2)

def playerschoice():
  player = input("Pick rock, paper, or scissors.")
  return player.lower()

def wincheck(player, robot):
  dict = {"rock": 0, "paper": 1, "scissors": 2}
  translationdict = {"rock": 0, "paper": 1, "scissors": 2}
  numplayerchoice = translationdict[player]
  alg = (3 + numplayerchoice - robot)%3
  print(alg)
  if alg == 0:
    print("tie")
    return False
  if alg == 2:
    print("robot wins")
    return False
  if alg == 1:
    print("You win")
    return True
    
def main():
  win = False
  while win == False:
    player = playerschoice()
    robot = robotchoice() 
    win = wincheck(player, robot) 


#main()