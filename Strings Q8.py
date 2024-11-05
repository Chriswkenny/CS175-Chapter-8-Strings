#Christopher Kenny
#CS 175
#Q8: Create a program that find the difference between two lists

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]

new_list_1 = list(set(list_1))
new_list_2 = list(set(list_2))

difference = set(new_list_1) - set(new_list_2)

difference = list(difference)

print(f"Difference of list1 - list2: {difference}")
