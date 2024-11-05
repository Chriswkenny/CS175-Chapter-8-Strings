#Christopher Kenny
#CS 175
#Q3: Create a program that finds the longest word in a sentence

def longest_word():
  string_3 = input("Enter a sentence: ")
  words = string_3.split()
  longest = max(words, key=len)
  return longest

  print(f"'{longest}'")

longest_word()
