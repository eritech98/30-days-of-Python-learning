#!usr/bin/env python3

'''
Create an empty tuple

'''
empty = tuple()

print(empty)

'''
Create a tuple containing names of your sisters and 

your brothers (imaginary siblings are fine)

'''

names =  ("Erick","Opiyo","Olando","Cate","Dina","Gorata")
brothers = ("Erick Olando","James","Peter","John")
sisters = ("Rose","Dina","Cynthia","Gorata","Phoebe")
parents = ("ParentA","ParentB")
siblings = brothers + sisters + parents

print(siblings)
#How many siblings do you have?
print('I have {} siblings'.format(len(siblings)))
#Modify the siblings tuple and add the name of your father and mother and assign it to family_members
print(siblings)

'''
Unpack siblings and parents from family_members

'''
a,b,c,d,e,f,g,h,i,j,k = ('Erick Olando', 'James', 'Peter', 'John', 'Rose', 'Dina', 'Cynthia', 'Gorata', 'Phoebe', 'ParentA', 'ParentB')

print('\n1st : {}'.format(a),'\n2nd : {}'.format(b),'\n3rd : {}'.format(c),'\n4th : {}\n5th : {}\n6th : {}\n7th : {}\n8th : {}\n9th : {}\n10th : {}\n11th : {}\n'.format(d,e,f,g,h,i,j,k))

'''
Create fruits, vegetables and animal products tuples. 

Join the three tuples and assign it to a variable called food_stuff_tp.

'''

fruits,vegetable,animal_products = ("mango","Passion fruits","grapes","Banana"),("Spinach","Brocolli","Cabbage","Carrots"),("Skin hides","Milk","animal fat","Fur")
food_stuff_tp = fruits + vegetable + animal_products
print(food_stuff_tp)
'''
Change the about food_stuff_tp tuple to a food_stuff_lt list
'''
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_tp,"\n",len(food_stuff_lt),'\n The middle items are  {} and {} which have an index of [5] and [6]\n'.format(food_stuff_lt[5],food_stuff_lt[6]))

'''
Slice out the first three items and the last three items from food_staff_lt list
'''
print('The first three  items in the food_stuff-tp  are {},{} and {}.\nThe last three items in the food_stuff_tp are {},{} and {}'.format(food_stuff_lt[0],food_stuff_lt[1],food_stuff_lt[2],food_stuff_lt[9],food_stuff_lt[10],food_stuff_lt[11]))
#Delete the food_staff_tp tuple completely
#del food_stuff_lt

def Erick():
    if "mango" in food_stuff_lt:
        print('There is an {} found in the food_stuff_lt list\n\n\n'.format("item"))
    else:
        print('There is no {} found in the food_stuff_lt list\nThe list is empty'.format("item"))
    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
    if "Estonia" and "Iceland" in nordic_countries:
        print('{} and {} coutries are in the list of Nordic countries'.format("Estonia","Iceland"))
    else:
        print('{} and {} are not in the list of Nordic countries'.format("Estonia","Estonia"))

Erick()
