#1
from turtle import st


dct={}

#2
dct['name']='med'
dct['color']='blue'
dct['legs']='2'
dct['age']='20'
dct['name']='mde'
dog=dct
print (dog)

#3
student={
    'first_name' : "med",
    'last_name' : "cherif",
    'gender' : "male",
    'age' : "20",
    'status' : "single",
    'skills' : ["nothing","nothinng","..."]
}

#4
print(len(student))

#5
skill=student['skill']

#6
dct['skills']=dct['skills'].append("shit")

#7
keys=dct.key()

#8
values=dct.values()

#9
list_of_tuples=tuple((dct.items))

#10
dct.popitem()

#11
del dct
