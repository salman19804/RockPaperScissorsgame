from collections import deque
# Rock
rock = """
   _______
---   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

def rotateHand():
    str = rock
    
    arr = str.split("\n")
    backwardstring
    for x in arr:
        og = list(x)
        backward = []
        length = len(og)

        for x in range(length -1, -1, -1):
            el = og[x]
            backward.append(el)
            
        
        

       