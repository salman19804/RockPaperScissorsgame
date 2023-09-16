import numpy as np
import os
# Rock
revRock = """
  _______   
 (____   ---
(_____)      
(_____)     
 (____)      
  (___)__.---
"""

rock = """
   _______
---   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""



# Paper
revPaper = """
       _______    
 ____(____    '---
(______           
(_______          
 (_______         
   (__________.---
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""



# Scissors
revScissors = """
        _______    
  ____(____   '---
 (______          
(__________       
      (____)      
       (___)__.---
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def rotateHand(rocktype):
    if(rocktype == "rock"):
          str = revRock
    if(rocktype == "scissors"):
          str = revScissors
    if(rocktype == "paper"):
          str = revPaper
    arr = str.split("\n")
    output = []
    columns, lines = os.get_terminal_size()
    for line in arr:
        numspaces = columns - len(line)
        spaces = " " * numspaces
        output .append(spaces + line)
    out = "\n".join(output) 
    print(out)
    return out

        
    
    
        

       