#Christopher Kenny
#CS 175
#Q6: Create a program that finds even and odd numbers in a list

numbers = [3, 5, 2, 9, 6, 10, 11, 24, 81]

number_even = [num for num in numbers if num % 2 == 0] #List comprehension
number_odd = [num for num in numbers if num % 2 != 0] #List Comprehension

print(f'Even numbers: {number_even}')
print(f'Odd numbers: {number_odd}')
