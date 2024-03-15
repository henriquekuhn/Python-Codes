# Get a list of number as input and create a squared list as output using list cmprehension:
numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
squered_list = [number**2 for number in numbers_list]
print(squered_list)

# Convert a list of string to a list of integer
#string_list = input("Enter a list of numers: ").split(",")
string_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
int_list = [int(int_number) for int_number in string_list]
# Get a list of the even numbers
even_list = [even_number for even_number in int_list if even_number%2 == 0]
print(even_list)

# Check file1.txt and file2.txt and create a list with the repeated numbers
import os

DIRECTORY = os.getcwd() + "/List Comprehension"
os.chdir(DIRECTORY)

with open ("file1.txt") as file1:
    list_file1 = file1.readlines()

print(list_file1)


with open ("file2.txt") as file2:
    list_file2 = file2.readlines()

result = [int(n) for n in list_file1 if n in list_file2]
print(result)

