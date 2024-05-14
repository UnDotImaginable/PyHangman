# Hangman game creation
# 1st step: create a word bank


def display_word(word, desired_letter):
    indices = [i for i, letter in enumerate(word) if letter == desired_letter]

    for char in word:
        if desired_letter is char:
            print(desired_letter, end=' ')
        else:
            print('_', end=' ')

    

import random

word_bank = ['Camry', 'Accord', 'Altima', 'Malibu', 'Sonata', 'Corolla', 'Elantra', 'Civic', 'ES', 'Ioniq', 'Prius', 'IS', 'LS']

chosen_word = word_bank[random.randint(0, len(word_bank)) - 1].lower()

tries = len(chosen_word) + 2

count = 0
correct_count = 0


print("Hangman: Try to guess the word, letter-by-letter")
print("Hint: the length is " + str(len(chosen_word)) + " and it is the name of a sedan")

while count < tries:
    guess = input("Your guess?: ")


    if guess in chosen_word:
        print("Yes, that's correct! Keep going!")
        display_word(chosen_word, guess)
        correct_count += 1
    else:
        print("Incorrect guess. Keep trying!")
    

    if correct_count == len(chosen_word):
        break


    count += 1


print("The name of the sedan was " + chosen_word)





