#Christopher Kenny
#CS 175
# Q1: Create a program to check if a strong is a palindrome

string_1 = input("Input any palindrome: ")

def palindrom_check(string_1):
  string_1 = string_1.replace(' ', '')
  string_lower = string_1.lower()
  string_reverse = string_lower[::-1]
  if string_reverse == string_lower:
    print("This string is a palindrome.")
  else:
    print("This string is not a palindrome.")

palindrom_check(string_1)
