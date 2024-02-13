"""
Напишите функцию is_valid(value: str) валидатор скобок. 
Функция принимает строку и проверяет 
что в ней всем открывающим скобкам есть 
соответствующие закрывающие скобки
"""


def is_valid(value: str) -> bool:
    """
    checking what number of open and closed brackets are equal
    """
    num_is_valid = (
        value.count("(") == value.count(")")
        and value.count("{") == value.count("}")
        and value.count("[") == value.count("]")
    )
    return num_is_valid


def is_valid2(value: str) -> bool:
    """
    checking every open bracket are closer propier way
    """
    acc = []
    brackets = ("()", "[]", "{}")
    for ch in value:
        for br in brackets:
            if ch == br[0]:
                acc.append(br[0])
            elif ch == br[1]:
                if not acc or acc[-1] != br[0]:
                    return False
                acc.pop()
    return len(acc) == 0

    # print(is_valid("((x) + 1 / (x - 2)"))
    # to_chek = ('()', '[]', '{}',
    #            '(text) [123] {___} ({[]})',
    #            '({[(())]})',
    #            '(sdfds{[sdf]sdfsd})',
    #            '({[]}',
    #            '(]',
    #            '(', '{{{{ ))))')

    # for string in to_chek:
    # print(string, is_valid(string), is_valid2(string))


# assert is_valid('()')
