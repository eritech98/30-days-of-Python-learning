#!usr/bin/env python3

'''
Here we have a person dictionary. Feel free to modify it!

        person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }
 * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 
 * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 
 * If a person skills has only JavaScript and React, print('He is a front end developer'), if the person skills has Node, Python, MongoDB, print('He is a backend developer'), if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') - for more accurate results more conditions can be nested!
 
 * If the person is married and if he lives in Finland, print the information in the following format:

 Asabeneh Yetayeh lives in Finland. He is married.

 '''

def Erick():
    person = {
    'first_name': 'Erick',
    'last_name': 'Olando',
    'age': 250,
    'country': 'Kenya',
    'is_marred': False,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

    if 'skills' in person:
        print('The middle item in the list is {}\n'.format(person['skills'][2]))

Erick()

#Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.


person = {
    'first_name': 'Erick',
    'last_name': 'Olando',
    'age': 250,
    'country': 'Kenya',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

if 'skills' in person:
    if 'Python' in person['skills']:
        print("Python is in the list")
    else:
          print("Python is not in the list")
else:
    print("No skills key in person dictionary")

'''
If a person skills has only JavaScript and React, print('He is a front end developer'),

if the person skills has Node, Python, MongoDB, print('He is a backend developer'),

if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'),

else print('unknown title') - for more accurate results more conditions can be nested!
 
 * If the person is married and if he lives in Finland, print the information in the following format:
'''

if 'Javascript' and 'React' in person['skills']:
    print("\nHe is a front end developer")
    if 'Node' and 'Python' and 'MongoDB' in person['skills']:
        print("He is a backend developer")
        if 'React' and 'Node' and 'MongoDB' in person['skills']:
            print("He is a fullstack developer")
else:
    print('unknown title')
if person['is_married'] == True and person['country'] == 'Kenya':
    print('\n{} {} lives in {} and its {} he is married'.format(person['first_name'],person['last_name'],person['country'],person['is_married']))
