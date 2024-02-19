"""
Напишите функцию перевода словаря в строку. to_string(value) -> str. Ключами словаря могут быть строки, значением числа (value=), листы(array=) и словари. Может быть до 100 вложенных словарей. 

Пример словаря:

{
    'key': [1, 2, 3],
    'key2': {
        'key1': 56,
        'key2': [1, 2, 3, 4, 5],
        'key3': {
            'key1': 56,
            'key2': []
        }
    },
}
"""
def to_string(value, i=1):
#    if isinstance(value, dict):
#        print(key)
        result = []
        for key in value.keys():
#            print(type(value[key]))
#            print(' ' * i, key, ': ', end='')
#            print(f'\n {" " * i} {key}:')
            result.append(f'\n {" " * i} {key}:')
            if type(value[key]) == list:
                result.append(f'Array = {value[key]}')
#                print("Array = ", value[key])
            elif isinstance(value[key], int | float | str):
                #print("Value = ", value[key])
                result.append(f'Value = {value[key]}')
            elif type(value[key]) == dict:
#                print(f'')
                result.append(to_string(value[key], i+1))
        return ''.join(result)
#    for key in value.keys():
#        print(key, value[key])


dict_example = { 'key': [1, 2, 3],
                 'key2': {
                  'key1': 56,
                  'key2': [1, 2, 3, 4, 5],
                  'key3': {
                   'key1': 56,
                   'key2': []
                  }
                 },
                 'key3': 'WOW'
               }

print(to_string(dict_example))
#print(dict_example)
#print(isinstance(dict_example, dict))
#print(result)
