#Calculates the sum of all the even numbers from 1 to input
print("Enter the target: ")
target = int(input())

sum = 0
for n in range(1, target+1):
    if n%2 == 0:
        sum += n

#Different way
sum2 = 0
for n in range(2, target+1, 2): #Start from 2 (first even) and forward 2 by 2
    sum2 += n

print(f'the sum of all even numers from 1 to {target} is: {sum}')
print(f'the sum of all even numers from 1 to {target} is: {sum2}')