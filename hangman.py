from pickle import FALSE
from random import randint
from string import ascii_lowercase
from webbrowser import get # Do not delete this line
import random

def displayIntro():
    file = open('hangman-ascii.txt', 'r')
    lines = file.readlines()
    print("".join(lines[1: 24]))  
    file.close()
        
        

def displayEnd(result):
    
    file = open('hangman-ascii.txt', 'r')
    lines = file.readlines()
    if result:
        print("".join(lines[190: 203]))
    else:
        print("".join(lines[100: 112]))
    file.close()


            
def displayHangman(state):
    file = open('hangman-ascii.txt', 'r')
    lines = file.readlines() 
    if state == 5:
        print("".join(lines[24: 32]))
    elif state == 4:
        print("".join(lines[37: 45]))
    elif state == 3:
        print("".join(lines[50: 58]))
    elif state == 2:
        print("".join(lines[63: 71]))
    elif state == 1:
        print("".join(lines[76: 84]))
    elif state == 0:
        print("".join(lines[89: 97]))
    file.close() 



def getWord():  
    fl = open('hangman-words.txt', 'r')
    file = random.choice(fl.readlines())
    new_string = file.replace('\n', '')
    fl.close()
    return new_string
    

def valid(c):
    if c in ascii_lowercase:
        if len(c) == 1:
            return True
        else:
            return False

def play():
    word = getWord()
    Char_ = len(word) * '_'
    list1 = list(Char_) # list of  Char_
    listOfWord = list(word)
    print(word)
    print(Char_)
    attempt = 5
    Word1 = ''
    displayHangman(attempt) 
    
    while True:       
        UserInput = input('please enter a character or word: ')
        if UserInput in Word1:
            print('you already entered this character')
            continue
        if UserInput == word:
            return True
        if valid(UserInput) == False:
            print('invalid input')
            continue
        if not valid(UserInput) or len(UserInput) == 0:
            print("Invalid Input")
            continue
        if valid(UserInput) and UserInput in word:
            displayHangman(attempt)
            for i in range(len(listOfWord)):
                if listOfWord[i] == UserInput:
                    list1[i] = UserInput
                Word1 = ''.join(list1)
            print(Word1)
        else:
            attempt -= 1
            displayHangman(attempt)
            print(Word1)
        if attempt == 0:
            print(f"the word was '{word}'")
            print('')
            return False
        if Word1 == word:
            return True
        
    

def hangman():
     while True:
        displayIntro()
        result = play()
        displayEnd(result)
        if(input("Do you want to continue ? (yes/no): ") == "no"):
            break
        else:
            continue

  

if __name__ == "__main__":
    hangman()

