

def add(*args):
    sum = 0
    for number in args:
        sum += number
    return sum

total = add(1, 2, 3, 4, 5)
print(total)