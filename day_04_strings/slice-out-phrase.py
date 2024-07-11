#!usr/bin/env python3

'''

Slice out the phrase 'because because because' in the following sentence:

'You cannot end a sentence with because because because is a conjunction'

'''

string = "You cannot end a sentence with because because because is a conjunction"

a = string.replace("because","")

print(a)
