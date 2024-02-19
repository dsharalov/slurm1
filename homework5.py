"""
SIMPLE GAME
"""

from random import randint

i = 1
tries = 8
print("ENTER THE NUMBER")
target = int(input())
min = 0
max = 100
#print(target)
guess = randint(min, max)
new_try = guess

while i <= tries:
    print("TRY", i, "OUT OF", tries)
    print("PC BET:", guess)
    if guess > target:
        print(" - ")
        max = guess
    elif guess < target:
        print(" + ")
        min = guess
    else:
        print("PC WIN")
        break
    while new_try == guess:
        new_try = randint(min + 1, max - 1)
    else:
        guess = new_try
#    print(guess)
    i += 1
else:
    print("PC LOSE")
