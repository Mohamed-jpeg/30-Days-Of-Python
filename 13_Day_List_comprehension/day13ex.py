#1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
lst=[i for i in numbers if (i<=0)]

#2
list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lst = [ i for row in list_of_lists for i in row ]

#3
lst = [
    (a, 1, a, a**2, a**3, a**4, a**5)
    for a in range(11)
]

#4
countries = [
    [('Finland', 'Helsinki')], 
    [('Sweden', 'Stockholm')], 
    [('Norway', 'Oslo')]
]


output = [
    [name.upper() , name[0:3].upper() ,capital]
    for row in countries
    for name , capital in row   
]

#print(output) #after 3 days aka 2h

#5
countries = [
    [('Finland', 'Helsinki')], 
    [('Sweden', 'Stockholm')], 
    [('Norway', 'Oslo')]
]

output=[
    {
        "country:" : country ,
        "capital"  : capital 
    } 
    for row in countries
    for country , capital in row
]

#print(output) #easy 

#6
names = [
    [('Asabeneh', 'Yetayeh')], 
    [('David', 'Smith')], 
    [('Donald', 'Trump')], 
    [('Bill', 'Gates')]
]

output=[
    name+" "+surname
    for row in names
    for name , surname in row
]

slope=lambda  x1 , x2 ,y1 , y2 : (y1 - y2)/(x1 - x2)

print (output)