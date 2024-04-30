import time

current_time = time.time()
print(current_time) #seconds sice Jan 1st, 1970

def speed_calc_decorator(function):
    def wrapper_function():
        first_time = time.time()
        function()
        secont_time = time.time()
        print(f"{function.__name__} run speed: {(secont_time - first_time)}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()