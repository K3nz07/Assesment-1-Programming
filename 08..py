# Write a program that searches for a specific string within a list of strings.
# The list is initialized with specific names ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave"). , and your task is to search for "Sam".

list  = ("Jake" "Zac", "Ian", "Ron", "Sam", "Dave")

find = input("input the name you want to serach for in the list: ")
if find in list:
    print(f' found {find}!')
else: 
    print(' not found')


