"""
homework test 3
"""


def pyramid(pyr_hight: int = 4, i=1, x=1, max_val=0):
    """
    build opposite pyramid
    """

    while i <= pyr_hight:  # get maximum value
        max_val += i
        i += 1

    i = 1
    row = ""
    while i <= pyr_hight:  # BUILD THE PYRAMID
        row += " ".join(str(x) for x in range(max_val, max_val - i, -1)) + "\n"
        max_val -= i
        i += 1
    return row


def main():
    """
    run program
    """
    print("Enter value")
    high = int(input())
    print(pyramid(high))


if __name__ == "__main__":
    main()
