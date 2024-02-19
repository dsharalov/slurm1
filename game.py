"""
TEST GAME
"""

import random

a = random.randint(1,3)

print("Put the number from 1 to 3")
#b = int(input())
b = 0

for i in range (1, 4):
    print("try number: ", i)
    b = int(input())
    if a == b:
        print("GOTCHA")
        break
