"""
#1

for i in range(0 ,11):

    print(i)

i=0

while i<10:

    i=i+1

    print(i)



#2

for i in range(10,0,-1):

    print(i)



i=10

while i>1:

    i=i-1

    print(i)



#3

ch=''

while ch!='#######':

    ch=ch+'#'

    print(ch)



#4

for i in range (5):

    print("# # # # # # # #")



#5

for i in range(0,10):

    print(i,'x',i,'=',i*i)



#6

for i in ['Python', 'Numpy','Pandas','Django', 'Flask']:

    print(i)



#7

for i in range(0, 100):

    if(i%2==0) :print(i)



#8

for i in range(0, 100):

    if(i%2!=0) :print(i)



#EX 2

#1

s=0

for i in range(0,100):

    s=s+i

print (s)



"""
#Exercises: Level 3

#1
from ..data.countries import countries

for i in countries :
    if 'land' in i:print(i)

#2
t=[]
for i in ['banana', 'orange', 'mango', 'lemon']:
    t=list(i) + t

#3...

