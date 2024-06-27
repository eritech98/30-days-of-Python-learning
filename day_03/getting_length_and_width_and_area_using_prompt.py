#!/usr/bin/env python3

"""
Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

"""

length = input("Enter length: ")
width = input("Enter width: ")

area = int(length) * int(width)
perimeter = 2 * (int(length) * int(width))

print("The Area is :", area,"\n","The perimeter is",perimeter)


