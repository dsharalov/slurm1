"""
TASK8
Напишите функцию chain_sum(value: int = None)
chain_sum()  # 0
chain_sum(5)()  # 5
chain_sum(5)(10)()  # 15
chain_sum(5)(10)(72)()  # 87  
"""

def chain_sum(value: int = None):
    result = getattr(chain_sum, 'result', 0)
    if value is None:
        chain_sum.result = 0
        return result
    chain_sum.result = value + result
    return chain_sum

print(chain_sum(5)(5)())
