#Christopher Kenny
#CS 175
#Q12: Create a program that removes non-alphabetic characters from a string

input_string = 'Hello, World! 123'

new_string = ''.join(char for char in input_string if char.isalpha())

print(f"String without non-alphabetic characters: {new_string}")
