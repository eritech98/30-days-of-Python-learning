#!usr/bin/env python3

'''
Which one of the following variables return True when we use the method isidentifier():

30DaysOfPython

thirty_days_of_python

'''

string1 = "30DaysOfPython"
string2 = "thirty_days_of_python"

a = string1.isidentifier()
b = string2.isidentifier()

print("\n",a,b,"\n","Therefore the string 'thirty_days_of_python' is",b)
