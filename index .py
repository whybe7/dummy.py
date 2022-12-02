#l = [['s','si','sir'],['m','me','mem']]
#x = input('enter something ').lower()
#
#if x in l[0] or x in l[1]:
#    if x in l[0]:
#        print(l[0])
#        print('sir')
#    if x in l[1]:
#        print(l[1])
#        print('mem')
#else:
#    print('try again ☻')
#
#from math import*
#print('----> ax^2+bx+c=0 SOLVER <----')
#a = int(input('Enter value of  a = '))
#b = int(input('Enter value of  b = '))
#c = int(input('Enter value of  c = '))
#f = ('f(x) = '+str(a)+'×^2'+'+'+str(b)+'× +'+str(c)+'= 0')
#fi = ('f(x) = '+str(a)+'z^2'+'+'+str(b)+'z +'+str(c)+'= 0')
#if a != 0:
#            d = (b**2)-(4*a*c)
#            if d < 0:
#                print('{} accepte tow solution on complex set (C)..'.format(fi))
#                z1 = (-b-complex(0,sqrt(d*-1))) / (2*a)
#                z2 = (-b+complex(0,sqrt(d*-1))) / (2*a)
#                print('that solutions is Z1 = {:.2f}'.format(z1))
#                print('----------> and.. Z2 = {:.2f}'.format(z2)) 
class Animal:
    alive = True

    def eat(self):
        print('this animal is eating')

    def slumber(self):
        print('this animal is  sleeping')
class rubbit(Animal):
    def run(self):
        print('this rubbit is running')

class fish(Animal):
    def swim(self):
        print('this fish is swiming')
class hawk(Animal):
    def fly(self):
        print('this hawk is flying')
class dainassor(Animal):
    alive = False

print(rubbit.alive)
print(rubbit.eat)
print(rubbit.run)
