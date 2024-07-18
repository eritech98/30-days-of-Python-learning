#!usr/bin/env python3

'''
The following list contains some fruits:

fruits = ['banana', 'orange', 'mango', 'lemon']

If a fruit doesn't exist in the list add the fruit 

to the list and print the modified list.

If the fruit exists print('That fruit already exist in the list')

'''

fruits = ['banana', 'orange', 'mango', 'lemon']

user = str(input("Enter a fruit: "))

if user in fruits:
    print('That fruit already exist in the list')
else:
    fruits.append(user)
    print(fruits)

