#Christopher Kenny
#CS 175
#Q7: Create a program that merges two lists, removes duplicates, and sorts the results

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]

new_list = list_1 + list_2

new_list = list(set(new_list))
new_list.sort()

print(f"Merged and unique list: {new_list}")
