#Christopher Kenny
#CS 175
#Q2: Create a Python program to count the number of vowels in a string

string_2 = input("Enter a string: ")

def vowel_count(string_2):
  vowels = 'AEIOUaeiou'
  count = 0
  for ch in string_2:
    if ch in vowels:
      new_count = count + 1
      count = new_count
  print(f"{count}")

vowel_count(string_2)
