"""
print 5x5 matrix
"""


def make_matrix(x: int = 1) -> str:
    """
    create matrix values
    """
    y = x + 25
    string = ""
    while x < y:
        for i in range(x, x + 5, 5):
            string += " " + str(i)
            if i % 5 == 0 and i < 25:
                string += "\n"
        x += 1
    return string


print(make_matrix())
