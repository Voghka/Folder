import random
import os

def run():

    IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    DB = [
        "C",
        "PYTHON",
        "JAVASCRIPT",
        "JAVA",
        "PHP"
    ]

    word = random.choice(DB)
    spaces = ["_"] * len(word)
    attemps = 6

    while True:
        os.system("class")
        for character in spaces:  
            print(character, end=" ")
        print(IMAGES[attemps])
        chosen = input ("Elige una letra").upper()

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                spaces[idx] = letter
                found = True

         if not found:
            attemps =- 1 

        if "_" not in spaces:
            os.system("class")
            print("Ganaste")
            break
            input() 

        if attemps == 0:
            os.system("class")
            print("Perdiste")
            break
            input()    

if __name__ == '__main__':
    run()
     
     list sorted    StopIteration  