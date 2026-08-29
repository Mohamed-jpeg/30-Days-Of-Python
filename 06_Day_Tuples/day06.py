#ex1
#1
tuple=()

#2
brothers=("john","mike")
sisters=("jane","mary")

#3
siblings=brothers+sisters

#4
n=len(siblings)

#5
parents=("mom","dad")
familly_members= siblings+parents

#ex2
#1
siblings=familly_members[0:4]
parents=familly_members[4:6]    

#2
fruits=("apple","banana","cherry")
vegtables=("carrot","broccoli","spinach")
animals=("dog","cat","rabbit")  
food_stuff_tp=fruits+vegtables+animals  

#3
food_stuff_lt=list(food_stuff_tp)

#4
mid=food_stuff_lt[4]

#5
fisrt=food_stuff_lt[0:3]
last=food_stuff_lt[5:8]

#6
del food_stuff_lt[5:8]

#7
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia'in nordic_countries)
print('Iceland'in nordic_countries) 
