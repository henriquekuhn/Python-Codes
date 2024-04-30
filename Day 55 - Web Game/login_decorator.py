# TODO: Create the logging_decorator() function

def logging_decorator(function):
    def wrapper(*args):
        print(f"You called {function.__name__}{args}")
        result = function(args[0], args[1], args[2])    
        print(f"It's returned: {result}")
        return result
    return wrapper

# TODO: Use the decorator

@logging_decorator
def a_function(a, b, c):
    return a * b * c

assert a_function(1, 2, 3) == (1*2*3)
assert a_function(3, 5, 2) == (3*5*2)