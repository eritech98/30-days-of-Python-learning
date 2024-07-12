#!usr/bin/env python3

'''
Declare a list variable named it_companies and assign initial values

Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon

'''

it_companies = ['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(it_companies)

#Print the number of companies in the list
print(len(it_companies))

#Print the first, middle and last company

print("\nFirst company:",it_companies[0],"\n","Middle company:",it_companies[3],"\n","Last Comapany:",it_companies[6])


#Print the list after modifying one of the companies

it_companies[0] = "NVIDIA"
print(it_companies)


#Add an IT company to it_companies
modified = it_companies.append("Helwett Packard")
print(it_companies)

#Insert an IT company in the middle of the companies list

it_companies.insert(4,"INTEL")

print(it_companies)



#Change one of the it_companies names to uppercase (IBM excluded!)

print(len(it_companies))
hello = it_companies[8].upper()
print(hello)

x = it_companies.remove("Helwett Packard")
print(it_companies)
y = it_companies.append(hello)
print(it_companies)


'''
Check if a certain company exists in the it_companies list
'''
def Checking():
    if it_companies[1] in it_companies:
        print('{} in list'.format(it_companies[1]))
    else:
        print('{} is not in the it_companies list'.format(it_companies[1]))
Checking()


'''
Sort the list using sort() method
'''
sortings = it_companies.sort()
print(it_companies)

'''
Reverse the list in descending order using reverse() method
'''
t = it_companies.reverse()
print(it_companies)

'''
Slice out the first 3 companies from the list
'''
slice = it_companies[0:3]
print(slice)



#Slice out the last 3 companies from the list
x,y,z = it_companies.remove(it_companies[-1]),it_companies.remove(it_companies[-2]),it_companies.remove(it_companies[-3])
print(it_companies)

#Slice out the middle IT company or companies from the list
def Remove():
    it_companies.remove("INTEL")
    it_companies.remove(it_companies[0])
    print(it_companies)
Remove()

#Remove all IT companies from the list
clearing = it_companies.clear()
print(clearing)

