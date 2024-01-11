global n
n = 0

def soma():
    global n
    n+=1
    return n

while soma() < 5:
    current_value = soma()
    print("conta mais")
    print(current_value)