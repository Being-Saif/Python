import pyfiglet
import random 
import getpass
import time,os
z=0
zz=0
first=0
last=0
def playeronebatt():
    global z
    global first
    global last
    global ii 
    print(f"{c} is batting and {p} is bowling ")
    if ii==1:
        while True:
            print("-"*100)
            x = int(getpass.getpass(prompt=f"{c} enter the number : " ))
            y = int(getpass.getpass(prompt=f"{p} enter the number : " ))
            if x==y :
                print(f"{c} got out .now its time for the {p}")
                break
            else:
                z=z+x
                print(f"( {c} score is )",z)
                first=z
    else:
        while True:
            print("-"*100)
            x = int(getpass.getpass(prompt=f"{c} enter the number : " ))
            y = int(getpass.getpass(prompt=f"{p} enter the number : " ))
            if x==y or first>last:
                print(f"{c} got out .now its time for the {p}")
                break
            else:
                z=z+x
                print(f"( {c} score is )",z)
                first=z
           

def playertwobatt():
    global zz
    global last
    print(f"{p} is batting and {c} is bowling ")
    if ii==1:
        while True:
            print("-"*100)
            x = int(getpass.getpass(prompt=f"{p} enter the number : "))       #getpass.getpass(prompt
            y = int(getpass.getpass(prompt=f"{c} enter the number : " ))
            
            if x == y :
                print(f"{p} got out .now its time for the {c}")
                break
            else:
                zz = zz + x
                print(f"( {p} score is )", zz)
                last=zz
    else:
        while True:
            print("-"*100)
            x = int(getpass.getpass(prompt=f"{p} enter the number : "))
            y = int(getpass.getpass(prompt=f"{p} enter the number : " ))
            
            if x == y or last>first:
                print(f"{p} got out .now its time for the {c}")
                break
            else:
                zz = zz + x
                print(f"( {p} score is )", zz)
                last=zz
    
            
#----------------------------------------------------------------------------------
a=pyfiglet.Figlet(font="slant")
print(a.renderText("Hand Cricket"))
p=input("Enter the name of player 1: ")
c=input("Enter the name of player 2: ")
print(f"The match is between the {p} and {c} ")
print("-"*100)
print(f"{p} choose odd are even ")
b=int(input("1 is for odd 2 is for even : "))
print("-"*100)
if b==1:
    odd=p
    even=c
else:
    odd=c
    even=p

print(f"{odd} has choosen odd {even} has choosen even ")
d=int(getpass.getpass(prompt=f"{p} Enter number: "))
e=int(getpass.getpass(prompt=f"{c} Enter number: "))

dd=d+e
if dd%2==0:
    print("-"*100)
    print(f"{even} won the toss ")
    print(f"Sorry {odd}")
    print("-"*100)
    i=0
else:
    print("-"*100)
    print(f"{odd} won the toss ")
    print(f"sorry {even}")
    print("-"*100)
    i=1

print("please wait for 10 seconds ")
time.sleep(5)
os.system("clear")


if i==0:
    if even==c:
        print(f"The {c} has to chosse ")
        aa=int(input("1 is for batting 2 is for bowling :"))
        f=1
    else:
        print(f"The {c} has to choose")
        aa=int(input("1 is for batting 2 is for bowling :"))
        f=0
else:
    if odd==c:

        print(f"The {p} has to choose")
        aa=int(input("1 is for batting 2 is for bowling: "))
        f=1
    else:
        print(f"The {p} has to choose")
        aa=int(input("1 is for batting 2 is for bowling :"))
        f=0

if f==1:
    if aa==1:
        print(f"The {c} has choosen for batting")
        cb=1
    else:
        print(f"The {c} has choosen for bowling")
        cb=0
else:
    if aa==1:
        print(f"The {p} has choosen for batting ")
        cb=0
    else:
        print(f"The {p} has choosen for bowling ")
        cb=1

if cb==1:
    ii=1
    playeronebatt()
    tt=1
else:
    ii=1
    playertwobatt()
    tt=0

if tt==1:
    ii=2
    playertwobatt()
else:
    ii=2
    playeronebatt()

if z>zz:
    print(f"{c} won the match ")
    time.sleep(5)
    os.system("clear")
    vv=pyfiglet.figlet_format(f"CONGRATULATIONS {c}",font="slant")
    print(vv)
elif z==zz:
    print(f"{p} and {c} won the  match")
    time.sleep(5)
    os.system("clear")
    vv=pyfiglet.figlet_format(f"CONGRATULATIONS {p} AND {c}",font="slant")
    print(vv)
else:
    print(f"{p} won the match")
    time.sleep(5)
    os.system("clear")
    vv=pyfiglet.figlet_format(f"CONGRATULATIONS {p}",font="slant")
    print(vv)


