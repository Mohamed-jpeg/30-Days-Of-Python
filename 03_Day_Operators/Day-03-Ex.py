import math

age = 20
height = 180 
complex = 2+2j

print("enter base and height of a triangular:")
a=float(input("Base:"))
b=float(input("Heaight:"))
print("The area of the triangle is ",(a*b)/2 )
print("The area of the rectangle is ",a**b)
print("The perimeter of the rectangle is ",2*(a+b) )



b=0
for i in range (0,3):
    a=float(input("side "+str(i)+":") )
    b+=a
print(b)

print("task 8")
x1=1
y1= 2*x1 +2
x2= 2
y2=2*x2+2
print("slope :",( (y1+y2)/(x1+x2) ))

print("task 9")

# y= x**2 + 6*x +9 

delta = 6**2 - 4*2*9

if (delta > 0):
    delta=math.sqrt(delta)
    x1=(-6 -delta)/4
    x2=  (-6 +delta)/4
    print("x1= ",x1,"   x2= ",x2)
elif(delta==0):
    print("x=",-6/4)
else : print ("aint no way")

s="python"
ss="dragons"
if(len(s)<len(ss)):print(ss) 
else : print(s)

s="I hope this course is not full of jargoon"
print ('jargon'in s)



