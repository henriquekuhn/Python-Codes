import os

DIRECTORY = os.getcwd() + "/Day 25 - Panda Introduction"
os.chdir(DIRECTORY)

DATA = []
TEMP = []
CONDITION = []
    
with open("weather_data.csv") as file:
    next(file)
    for line in file:
        print()
        DATA.append(line.strip().split(",")[0])
        TEMP.append(line.strip().split(",")[1])
        CONDITION.append(line.strip().split(",")[2])

    print(DATA)
    print(TEMP)
    print(CONDITION)
