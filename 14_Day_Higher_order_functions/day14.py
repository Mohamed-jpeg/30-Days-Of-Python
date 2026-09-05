#1
"""
the differnece is that :
map: apply the function on each elemnt of the iterable sparatly 
filter filters by the output of the function (true / false) of the dfunction passed in 
reduce : return one element from the outpu oof the function 
"""

#2
"""
closure : let the inner function acces the outer function scope
decoretors: the decoretor function change the output of the main function without changing the main function
high order function: are pre defined fuctions that take or retun a fcntion 
"""

#3
from functools import reduce


lst=[1,2,3,4,4,5]
def map_func(x):
    return x*x

def filter_func(x):
    return x%2

def reduce_func(x,y):
    return x-y

square_lst=map(map_func,lst)
paire_lsy=filter(filter_func,lst)
minus_lst=reduce(reduce_func,lst)

#leve 2
#1
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def uppercase(x):
    return str(x).upper()

upper_countries=map(uppercase , countries)

#2
square_lst=map(map_func,numbers)

#4
yup=lambda x : 'land'in x
yup_lst=filter(yup,countries)

#9
def get_string_lists (x):
    return list(filter(lambda x: isinstance(x,str),lst))

#10
sum=reduce(lambda x,y:x+y,numbers)

#11
sentence=str(reduce( lambda x,y: str(x) + '\' ' + str(y),countries ) +' are north European countries')
print(sentence)

#12 

def ategorize_countries(countries):
    land_countries=filter( lambda x : 'land' in x ,countries)
    ia_coutries=filter( lambda x : 'ia' in x ,countries)
    island_coutries=filter( lambda x : 'island' in x ,countries)
    stan_coutries=filter( lambda x : 'stan' in x ,countries)
    print(land_countries)
    print(island_coutries)
    print(ia_coutries)
    print(stan_coutries)

ategorize_countries(countries)

#13
def Q_13(countries):
    lst=[ 'land', 'ia', 'island', 'stan']
    output=[]
    for i in lst:
        output.append( { i , int( len( list( filter( lambda x:i in countries , countries ) ) ) ) } )
    print (output)

Q_13(countries)

