"""
homework 6
"""

def my_range(stop: float, start = 0.0, step = 0.2) -> list[float]:
    result = []
    while start <= stop:
        result.append(round(start, 10))
        start += step
    return result

print(my_range(5.5, 2.9))
