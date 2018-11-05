#
# Author: Darren Giles
# Description: Hangman game
#
import random

#hangman drawings
HANGMAN = (
"""
-----
|   |
|
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
|  -+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|
|
|
|
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|   |
|   |
|
|
|
--------
""",

"""
-----
|   |
|   0
| /-+-\\
|   |
|   |
|  |
|  |
|
--------
""",
"""
-----
|   |
|   0
| /-+-\\
|   |
|   |
|  | |
|  | |
|
--------
""")
#start game
print("Welcome to Hangman! A word will be chosen randomly- it is your job to guess it!")
#word generator
words = ["gridiron","sinew","connive","verbose","caterwaul","shambles","multitudinous","pamphleteer"]
victory = False
gameOn = True
while gameOn:
    randomWord = words[random.randint(0,3)]
    word = list(randomWord)
    length = len(randomWord)
    under = "_ " * length
    under = list(under)
    #print(randomWord)
    round = 0
    right = 0
    guess = None
    wrong = []
    while round < len(HANGMAN) and right < len(randomWord):
        print("**** HANGMAN ****\n")
        print(HANGMAN[round])
        print(' '.join(wrong) + "\n")
        print(*under)

        guess = input("Take a guess...")
        correct = False
        for x in range(0,length):
            if guess == word[x]:
                under[x*2] = guess
                correct = True
                right = right + 1
        if correct == False:
            wrong.append(guess)
            round = round + 1
        for y in range(0,length):
            if under[y] == '_':
                victory = False
            else:
                victory = True
    print("**** HANGMAN ****\n")
    print(HANGMAN[round])
    if victory == True:
        print("You win!")
    else:
        print("You Lose...")
    playAgain = input('Play again? y / n')
    if playAgain == 'n':
        gameOn = False
