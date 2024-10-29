#Christopher Kenny
#CS 175
#String Assignment 4

correct_length = False
has_uppercase = False
has_lowercase = False
has_digit = False


password = input("Please enter your password: ")

if len(password) >= 7:
  correct_length = True

if correct_length == True:
  for ch in password:
    if ch.isupper():
      has_uppercase = True
    if ch.islower():
      has_lowercase = True
    if ch.isdigit():
      has_digit = True

  if has_uppercase and has_lowercase and has_digit:
    print('True')
  else:
    print('False')

else:
  print('False')
