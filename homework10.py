"""
Напишите функцию is_substring(string: str, sub_string: str) -> bool 
принимающую две строки и определяющую является ли вторая строка подстрокой первой.
"""


def s_substring(string: str = "", sub_string: str = "") -> bool:
    return sub_string in string
#    if sub_string in string:
#        return True
#    else:
#        return False
#    print ("TEST")


print(s_substring("TEST", "ST"))
