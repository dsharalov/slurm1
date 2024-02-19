"""
Напишите функцию to_snake_case(value: str) принимающую строку с текстом и возвращающую строку со склеиными через _ словами. 
"""


def to_snake_case(string: str):
    string = string.replace(" ", "_")
    string = string.lower()
    return string


print(to_snake_case("E БАТЬ ТВОЙ РОТ"))
