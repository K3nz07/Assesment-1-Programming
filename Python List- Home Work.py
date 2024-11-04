# 1. Create a list of 5 of your favorite fruits. Print the list.
list = ['apple', 'banana', 'grapefruit', 'orange', 'dragonfruit']
print (list)

# 2.Exercise: Given the list colors = ['red', 'blue', 'green', 'yellow', 'purple'], print the first, third, and last color in the list.

list = ['red', 'blue', 'green', 'yellow', 'purple']
print (list[0])
print (list[2])
print (list[4])

# 3 Exercise: Create a list numbers with values [10, 20, 30, 40, 50]. Change the second item to 25 and add 60 to the end of the list. Print the modified list.
list = [10,20,30,40,50]
list[1] = 25
list.append(60)
print (list)
 
#4 Exercise: Using the list names = ['Alice', 'Bob', 'Charlie', 'David', 'Emma'], create a new list subset containing only the first three names. Print subset.
list = ['Alice', 'Bob', 'Charlie', 'David', 'Emma']
subset = [list[0] ,list[1] , list[2]] 
print (subset)

# 5 Exercise: Create a list of numbers from 1 to 10 and use a loop to print each number squared.

x = [a**2 for a in range (1,11)]
print(x)


 # 6 Exercise: Create an empty list called shopping_cart. Add the items 'milk', 'bread', and 'eggs' to it using the .append() method. Then use .extend() to add ['butter', 'cheese'] to the list. Print the final list.

shopping_cart = []
shopping_cart.append('milk')
shopping_cart.append('bread')
shopping_cart.append('egg')
shopping_cart.extend(['butter', 'cheese'])
print(shopping_cart)

# 7 Exercise: Write a program to find the maximum and minimum values in the list numbers = [45, 22, 88, 56, 92, 33].
list =  ["45", "22", "88", "56", "92", "33"]
print ("maximum age:", max(list))
print ("minimum age:", min(list))

# 8 Exercise: Given the list letters = ['a', 'b', 'a', 'c', 'b', 'a', 'd'], count how many times the letter 'a' appears in the list.
list = ['a', 'b', 'a', 'c', 'b', 'a', 'd']
count_of_a = list.count('a')
print (f"the amount of times a appears in the list is {count_of_a}")

# 9 Use list comprehension to create a new list containing the squares of all even numbers from 0 to 10. Print the resulting list.

x = [x**2 for x in range(2, 21, 2)]
print(x)


# 10 Exercise: Given the list nums = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7], write a program to remove duplicates and print the unique elements only.
old_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
new_list = (set(old_list))
print(new_list)
