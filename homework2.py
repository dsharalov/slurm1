"""
homework task 2
"""
def pyramid(pyr_hight: int = 4, i=1, y=1):
    """
    building the pyramid
    """
    row = ''
    while i <= pyr_hight:
        row += ' '.join(str(i) for i in range(y,y+i)) + '\n'
        y += i
        i += 1
    return row

def main():
    """
    run program
    """
    print("Enter the pyramid height:")
    height = int(input())
    print(pyramid(height))

if __name__ == "__main__":
    main()
