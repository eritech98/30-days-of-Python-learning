#!usr/bin/env python3

'''
Use rindex to find the position of the last occurrence of the word because in the following sentence:

'You cannot end a sentence with because because because is a conjunction'

'''

def Erick():
    string = "You cannot end a sentence with because because because is a conjunction"
    a = string.rindex("because")
    print(a)
Erick()
