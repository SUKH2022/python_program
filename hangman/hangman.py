import random
from words import words
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was', word)
    else:
        print('YAY! You guessed the word', word, '!!')


if __name__ == '__main__':
    hangman()

'''
You have 6 lives left and you have used these letters:  
Current word:  - - - - - - - - - - -
Guess a letter: k

Your letter, K is not in the word.
You have 5 lives left and you have used these letters:  K
Current word:  - - - - - - - - - - -
Guess a letter: a

Your letter, A is not in the word.
You have 4 lives left and you have used these letters:  K A
Current word:  - - - - - - - - - - -
Guess a letter: e

Your letter, E is not in the word.
You have 3 lives left and you have used these letters:  K E A
Current word:  - - - - - - - - - - -
Guess a letter: i

You have 3 lives left and you have used these letters:  K E A I
Current word:  I - - - - - - I - - -
Guess a letter: o

You have 3 lives left and you have used these letters:  E K O I A
Current word:  I - - - - - - I O - -
Guess a letter: u

You have 3 lives left and you have used these letters:  E K O I U A
Current word:  I - - U - - - I O U -
Guess a letter: a

You have already used that letter. Guess another letter.
You have 3 lives left and you have used these letters:  E K O I U A
Current word:  I - - U - - - I O U -
Guess a letter: s

You have 3 lives left and you have used these letters:  E K O S I U A
Current word:  I - - U S - - I O U S
Guess a letter: n

You have 3 lives left and you have used these letters:  E K N O S I U A
Current word:  I N - U S - - I O U S
Guess a letter: d

You have 3 lives left and you have used these letters:  D E K N O S I U A
Current word:  I N D U S - - I O U S
Guess a letter: t

You have 3 lives left and you have used these letters:  D E K T N O S I U A
Current word:  I N D U S T - I O U S
Guess a letter: r

YAY! You guessed the word INDUSTRIOUS !!
'''