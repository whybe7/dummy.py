# To ensure app dependencies are ported from your virtual environment/host machine into your container, run 'pip freeze > requirements.txt' in the terminal to overwrite this file
#import  time 
#a = int(time.time())
#
#for s in range(1,10+1):
#    for ms in range(1,100+1):
#        print(s,ms)
#b= int(time.time())
#score = 100
#c = b-a #20
#stp = 0
#if c > 0 :
#    for j in range(1,c+1):
#        if j % 5 == 0:
#            stp += 1
#    print(stp)
#    for i in range(1,stp+1):
#        new =score - i*5
#    print(new)
#name = None
#gender = None
#flage = True
#l = [['sir','si','s'],['mem','me','m']]
#while not name :
#    name = input("Enter your name : ").lower()
#    if name.isdigit() == True:
#        name = None
#        print("we don't support numbers")
#while not gender:
#    gender = input("(sir/mem): ")
#    if gender  in l[0] or gender in l[1]:
#        break
#    else:
#        gender = None
from math import*
from abc import ABC,abstractclassmethod

def cap():
    question = str(input('→(vol) for cylinder... ,and →($) for desk... : '))
    print()
    if question == '$':
        r1 = float(input('Enter the rayone of this circle → ($) :'))
        print()
        p1 = 2*pi*r1
        a1 = pi*pow(r1,2)
        print('The perimeter of ($) is : %.2f and the area of ($) is : %.2f '%(p1,a1))

    elif question == 'Vol' or question == 'v' :
        r2 = float(input('Enter the rayone of this cylinder → (C) :'))
        h = float(input('Enter the height of this cylander → (C) :'))
        print()
        p2 = 2*pi*r2
        vol = h*pi*pow(r2,2)
        ls = 2*pi*r2*h
        s = 2*pi*r2*(r2+h)
        print('The perimeter of (C) is : %.2f and the letural area of (C) is : %.2f '%(p2,ls))
        print('And the total area of (C) is %.2f and the volume of it is %.2f'%(s,vol))
def small(text:str) -> str:
    txt = text.lower()
    print(txt)
    
def larg(text:str) -> str:
    txt = text.upper()
    print(txt)
    
def convert(func,text):
    func(text)
    
    
class Animals(ABC):
    
    @abstractclassmethod
    def alive(self):
        pass

class Rabbit(Animals):
    def alive(self):
        print("this rabbit is alive")

class Fish(Animals):
    def alive(self):
        print("this fish is alive")

fish = Fish()
rabbit = Rabbit()


class Car():
    color = None
class Bike():
    color = None
def change_color(vehicle,color):
    vehicle.color = color
    
car1 = Car()
car2 = Car()

bike1 = Bike()
bike2 = Bike()

change_color(car1,"red")
change_color(bike1,"red")


class Duck:
    def walk(self):
        print("this duck is walking")
    def talk(self):
        print("this duck is quacking")
class Chiken:
    def walk(self):
        print("this chiken is walking")
    def talk(self):
        print("this chiken is clacking")
class Person():
    def catch(self,obj):
        obj.walk()
        obj.talk()
        print("this person walk")

chiken = Chiken()
duck =  Duck()
person = Person()


#foods = list()
#while food := input("what's your favorit food") != 'quit': foods.append(food) 
chek_age = lambda age : True if age >= 18 else False
print(chek_age(18) )