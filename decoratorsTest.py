import time
import math

def calculate_time(func):

    def inner(*args,**kwargs):
        begin = time.time()
        returned_value = func(*args,**kwargs)
        print(returned_value)
        end =  time.time()
        print("Total time taken in : ", func.__name__, end - begin)
    return  inner


@calculate_time
def fact(num):
    time.sleep(1)
    print(math.factorial(num))
    return 1

fact(4)


def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1

    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b


# Create a generator object
x = fib(5)

# Iterating over the generator object using next
for i in range(5):
    print(x.__next__())  # In Python 3, __next__()