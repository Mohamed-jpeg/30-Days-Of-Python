# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

##Level 1
print( len(it_companies) )  # length of the set
it_companies.add('Twitter')  # add an item to the set
it_companies.update(['LinkedIn', 'Snapchat'])  # add multiple items to the set
it_companies.remove('IBM')  # remove an item from the set
# if the item we want to remove doesnt exist 'remove' will throw an error yet discard wont

##Level 2
C = A.union(B)  # join A and B
C=A.intersection(B)  # find A and B intersection
print (C)
