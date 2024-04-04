print("Example init...")

students_score = input().split() #input = 75 84 72 90 88 96 

for n in range(len(students_score)):
    students_score[n] = int(students_score[n])

highest_score = 0
for highest in students_score:
    if highest > highest_score:
        highest_score = highest

print(f'The highest score in the class is:  {highest_score}')
