import random
import string
from words import words #importing words from another file which has a lot of words in it

#We want to get a single word from that file, it shouldn't have a space or - in it
def validword():
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)
    return word.upper()

def game():
    word = validword() 
    word_letters = set(word) #The letters in the word
    alphabet = set(string.ascii_uppercase) 
    used_letters = set() #The letters user will write
    
    lives = 8
    
    #Main game loop
    while lives > 0:
        string_used_letters = ", ".join(used_letters)
        print(f"You have {lives} lives.\nUsed letters: {string_used_letters}")
        
        #Making a list which will show _ if user haven't guessed the letter yet, it will also show the letter if user has guessed it.
        word_list = [letter if letter in used_letters else "_" for letter in word]
        
        #Turning the list into a string so it appears nicely for the user
        display = "".join(word_list)
        print("Current word:", display)
        
        if display == word:
            print(f"You've guessed the word {word}, correctly!")
            break
             
        request = input("Enter a letter: ").upper()
        
        if request in used_letters:
            print("You've used that letter.\n")
            continue
        
        if request not in alphabet:
            print("That is not a letter...\n")
            continue
        
        used_letters.add(request) 
           
        if request in alphabet - word_letters:
            print(f"{request} isn't in the word.")
            lives = lives - 1
        
        print(" ")
            
    else:
        print(f"You ran out of lives, the word was {word}")

if __name__ == '__main__':
    game()                                        