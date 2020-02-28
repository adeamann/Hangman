import random
import sys


def show_char(hidden_word, chars=None):
    chars = chars if chars else set()
    result = []
    for ch in hidden_word:
        if ch in chars:
            result.append(ch)
        else:
            result.append('-')
    return ''.join(result)


# Write your code here
print('H A N G M A N')
while True:
    do = input('Type "play" to play the game, "exit" to quit: ')
    if do == 'play':
        word_list = ['python', 'java', 'kotlin', 'javascript']
        hidden_word = random.choice(word_list)
        display = '-' * len(hidden_word)
        chars = all_chars = set()
        attempt = 8
        win = False

        while attempt > 0:
            print()
            print(display)
            char = input('Input a letter: ')
            if len(char) != 1:
                print('You should print a single letter')
            elif char.islower():
                if char in chars:
                    print('You already typed this letter')
                elif char in hidden_word:
                    chars.add(char)
                    display = show_char(hidden_word, chars)
                else:
                    print('No such letter in the word')
                    attempt -= 1
                all_chars.add(char)
                if '-' not in display:
                    win = True
                    break
            else:
                print('It is not an ASCII lowercase letter')

        print('You guessed the word!\nYou survived!' if win else 'You are hanged!')
        print()
    elif do == 'exit':
        break
