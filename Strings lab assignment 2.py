#Christopher Kenny
#CS 175
#Strings Lab Assignment 2; May be useful for quiz

list_of_titles = [['Windtaker', 'Jones'], ['Godfather', 'Smith'], ['Winds of war', 'Brown']]

title_search = input('Enter a novel to look up (Keep in mind capitalization): ')

found = False

for title, author in list_of_titles:
  if title_search == title:
    found = True
    print(f'The author of {title_search} is {author}')

if not found:
    print(f'Title {title_search} is not in the list')
