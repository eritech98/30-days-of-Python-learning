#!/usr/bin/env python3

"""
The radius of a circle is 30 meters.

1.Calculate the area of a circle and assign the value to a variable name of area_of_circle

2.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

3.Take radius as user input and calculate the area.

"""
radius = int(30) 
area_of_circle = 3.142 *  radius *  radius
print("Area of Cicle is ", area_of_circle, "meters")

#2.Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle

diameter = radius * 2
circum_of_circle = 3.142 * diameter
print(circum_of_circle)

"""
Use the built-in input function to get first name, last name, country and age from a user and store the value to their

corresponding variable names

"""

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = input("Enter your age: ")
country = input("Enter your country: ")

print(first_name, last_name, age, country)

#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords
help('keywords')


