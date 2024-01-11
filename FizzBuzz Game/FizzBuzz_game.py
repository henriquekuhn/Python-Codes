for buzzFizz in range(1, 101):
    if buzzFizz%3 == 0 and buzzFizz%5 == 0:
        print("FizzBuzz")
    elif buzzFizz%3 == 0:
        print("Fizz")
    elif buzzFizz%5==0:
        print("Buzz")
    else:
        print(buzzFizz)
