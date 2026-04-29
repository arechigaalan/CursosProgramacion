"""Día 7 - 9/12/2025 - Hangman"""
import random as r

word_list = ['aardvark', 'baboon', 'camel']
chosen_word = r.choice(word_list)
placeholder = '_' * len(chosen_word)
aux = list(placeholder)
lives = 5
while lives > 0 and "".join(aux) != chosen_word:
    guess = input('Guess a letter: ')
    if guess not in chosen_word or guess in aux:
        lives -= 1
    else:
        count = 0
        for letter in chosen_word:
            if letter == guess:
                aux[count] = guess
            count += 1
        print(str(aux))
