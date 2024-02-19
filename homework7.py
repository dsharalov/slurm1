"""
TASK 7
my_range(stop: float, start = 0.0, step = 1.0) -> Generator[float]:

"""

#Generator=[]
def my_range(stop: float, start = 0.0, step = 0.5):
#    i=1
    while stop > start:
        start += step
        yield start

for i in my_range(10):
    print(i)

