#Christopher Kenny
#CS 175
#Strings Assignment 1

string_1 = input("Enter any word or words with the letter 't' in it: ")
count = 0

for ch in string_1:
  if ch.lower() == 't':
    count += 1

print(f"The letter T appears {count} times.")
