#!usr/bin/env python3

'''
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}

B = {19, 22, 20, 25, 26, 24, 28, 27}

age = [22, 19, 24, 25, 26, 24, 25, 24]

Find the length of the set it_companies
'''
def set_1():
    it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    A = {19, 22, 24, 20, 25, 26}
    B = {19, 22, 20, 25, 26, 24, 28, 27}
    age = [22, 19, 24, 25, 26, 24, 25, 24]
    print('The length of the it_companies set is {}'.format(len(it_companies)))
    adding = it_companies.add("Twitter")
    print(it_companies)
    '''
    Insert multiple IT companies at once to the set it_companies
    '''
    
    items = "Windows","Hp","NVIDIA","open ai","Apple","Amazon"
    it_companies.add(items)
    print(it_companies)
    '''
    Remove one of the companies from the set it_companies
    '''
    it_companies.remove("Google")
    print(it_companies)
    it_companies.discard("Facebook")
    print(it_companies)
    joining = A.union(B)
    print(joining)
    '''
    Find A intersection B
    '''
    intersect = A.intersection(B)
    print(intersect)
    check = A.issubset(A)
    print('It is {} that A is ia a subset of B'.format(check))
    check1 = A.isdisjoint(B)
    print('it is {}'.format(check1))
    #Join A with B and B with A
    joining1,joining2 = A.union(B),B.union(A)
    print('If we join A with B,we get {} and if we join B with A we get {}'.format(joining1,joining2))
    '''
    What is the symmetric difference between A and B

    '''
    symetric = A.symmetric_difference(B)
    print(symetric)
    del it_companies,A,B
    '''
    Convert the ages to a set and compare the length 

    of the list and the set, which one is bigger?
    '''
    change2set = set(age)
    print('The age list has been converted to set {}'.format(change2set))
    if len(age) > len(change2set):
        print('The length of Age list which is {}, is greater than length of Age set which is {}'.format(len(age),len(change2set)))
    if len(change2set) > len(age):
        print('The length of Age set is {} abd its greater than the length of Age list which is {}'.format(len(change2set),len(age)))
    '''
    How many unique words have been used in the sentence?

    Use the split methods and set to get the unique words.
    '''
    string1 = "I am a teacher and I love to inspire and teach people."
    another = string1.split()
    print(another)
    another1 = set(another)
    print(another1,"\n",'Thefore the length of unique words is {}'.format(len(another1)))
    
set_1()

