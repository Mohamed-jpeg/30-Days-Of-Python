#1
from turtle import back


list=[]

#2
list=[0,1,2,3,4,5]

#3
n=len(list)

#4
first=list[0]
middle=list[int(n/2)]
last=list[-1]

#5
mixed_data_types=["med","cherif",20,180,"single","m5"]

#6
it_companies=["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle" ,"Amazon"]

#7
print(it_companies)

#8
print(len(it_companies))

#9  no

#10
it_companies[1]="keka"
print(it_companies)

#11
it_companies.append("hello")

#12
it_companies.insert(3,"BONJOUR")

#13
it_companies[3]=it_companies[3].upper()

#14
s=["#;"]
s=it_companies+s

#15
print("facebook" in it_companies )

#16
it_companies.sort()

#17
it_companies.sort(reverse=True)

#18
fisrt_slice=it_companies[:2]

#19
n=len(it_companies)
last_slice=it_companies[n-2:]

#20
middle_slice=it_companies[int(n/2)]

#21
it_companies.pop(0)

#22
n=len(it_companies)
it_companies.pop(int(n/2))

#23
it_companies.pop()

#24
it_companies.clear()

#25
del it_companies

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

l=front_end+back_end

#27
full_stack=l
