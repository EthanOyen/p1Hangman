'''
Created on Dec 7, 2019

@author: ITAUser
'''
import random

def pick_random_word():
    f = open("words.txt", "r")
    words = f.readlines()
    index = random.randint(0, len(words) - 1)
    word = words[index].strip()
    return word

def ask_user_for_next_letter():
    letter = input("Guess a letter:")
    return letter.strip().upper()

def generate_word_string(word, letters_guessed):
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else:
            output.append("_")
    return " ".join(output)
    
if __name__ == '__main__':
    WORD = pick_random_word()
    letters_to_guess = set(WORD)
    correct_letters_guessed = set()
    incorrect_letters_guessed = set()
    num_guesses = 0
    
    print("Welcome to Hangman!")
    while(len(letters_to_guess) > 0 and num_guesses < 6):
        guess = ask_user_for_next_letter()
        guess = guess.lower()
        
        if guess in correct_letters_guessed or guess in incorrect_letters_guessed:
            print("You already guessed that letter.")
            continue
        
        if guess in letters_to_guess:
            letters_to_guess.remove(guess)
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            num_guesses += 1
        
        word_string = generate_word_string(WORD, correct_letters_guessed)
        print(word_string)
        print("You have {} guesses left".format(6 - num_guesses))
    
    if num_guesses < 6:
        print("You win! The word was {}".format(WORD))
    else:
        print("You lose, the word was {}".format(WORD))