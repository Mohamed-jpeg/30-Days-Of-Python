#1
import random
import string


def random_user_id()->None:
    ch=string.ascii_letters + string.digits
    id=''
    for i in range(0,6):
        id=id+ch[random.randint(0,len(ch))]
    
    print(id)

random_user_id()

#2
def list_of_rgb_colors()->list[int] :
    l=[]
    for i in range(0,3):
        l.append(random.randint(0,255))
    return l

print(list_of_rgb_colors())

#3

def generate_colors(type,nb):
    l=[]
    if (type=='hexa'):
        for i in range(nb):
            hex_color_alt = "#" + "".join(random.choices("0123456789abcdef", k=6))
            l.append( hex_color_alt )
    else :
        l=[]
        for i in range(nb):
            k=[]
            for i in range(0,3):
                    k.append(random.randint(0,255))
            l.append(k)
    
    return l

print(generate_colors('rgb', 3))  # ['rgb(5, 55, 175','rgb(50, 105, 100','rgb(15, 26, 80'] 

#level3
#1
def shuffle_list(l):
    return random.shuffle(l)
    