#!usr/bin/env python3
#Create an empty dictionary called dog

dog = dict()
print(dog)

#Add name, color, breed, legs, age to the dog dictionary

dog = {
        "name" : "Rufus",
        "Color": "Black",
        "Breed": "German shephard",
        "legs" : 4,
        "age" : 20
        }
print(dog)
'''
Create a student dictionary and add first_name, 

last_name, gender, age, marital status, skills,

country, city and address as keys for the dictionary

'''
student = {
        "First name: ": "Erick",
        "Last name: " : "Olando",
        "Gender :" : "Male",
        "Age :": 20,
        "Marital status:":"Single",
        "skills:": ["Python","Mongodb","XLS","C programming","CSS","Software development","Meteorology","Guitar"],
        "Country:" : "Kenya",
        "City :" : "Nairobi",
        "Adress" : {
            "Po.Box :": 30197,
            "Town :" :"Eldoret",
            "Work place" :"JKIA"
            }
        }

print('This is the dictionary I have created {}\n\nThe length of the dictionary is {}'.format(student,len(student)))
#Get the value of skills and check the data type, it should be a list
print(student['skills:'])

#Modify the skills values by adding one or two skills
two = "R programming","C#"
more = student["skills:"].append(two)
print('\n\nHere is the list-{}'.format(student["skills:"]))
#Get the dictionary values as a keys
getting = student.keys()
print(getting)

#Get the dictionary values as a list
getting2 = student.values()
print('\n\nThis are the values of the dictionary: {}'.format(getting2))
'''
Change the dictionary to a list of tuples using items() method
'''
changing = student.items()
print("\n\n",changing)

'''
Delete one of the items in the dictionary
'''
times = student.pop('Adress')
print("\n\n",student)
#Delete the dictonary
#del student
#print(student)
