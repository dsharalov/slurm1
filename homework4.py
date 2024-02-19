"""
simple game
"""

import random



def main(i=1, tries=8, my_num: int = 10, target=None):
    """
    main func to run game
    """
    print("TRY TO GESS THE NUMBER FROM 0 TO 100")

    if target is None:
         target = get_random_target()
    while i <= tries:
        print("TRY", i, "OUT OF", tries)
        my_num = int(input())
        result = compare_answer(my_num, target)
        print(result)
        if result == "YOU WIN":
            break
        i += 1
    else:
        print("YOU LOSE, the target number was:", target)

def get_random_target(target_value: int = 10):
    """
    get random number
    """
    target_value = random.randint(0, 100)
    return target_value


def compare_answer(answer: int, target: int):
    """
    compare answer and tagget number
    """
    if answer < target:
        result = "TARGET IS MORE"
    elif answer > target:
        result = "TARGET IS LESS"
    else:
        result = "YOU WIN"
    return result


if __name__ == "__main__":
    main()
