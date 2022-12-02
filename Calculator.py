#----------------------|| MATH LIBRARY USFULL FUNCTION ||------------------ 
from math import*
import os 

def plus(n1,n2):
    return n1 + n2

def sub(n1,n2):
    return n1 - n2

def mul(n1,n2):
    return n1 * n2


def deuc(n1,n2):
    mx = max(n1,n2)
    d =  n1 / n2
    m = (n1 % n2)
    print(n1)
    print('▬'*len(str(mx))+' = '+str('%.3f'%d))
    print(n2)

def clear():
    import os 
    os .system('cls')

def count(start,finish):
    n = -1
    for n in range(int(start),int(finish)):
        x = str(print('hi {}'.format(str(start))))
        n += 1 

def note(n):
     
    nt = list(range(1,21))
    for i in nt:
        i+=1
    if nt[11] >= n and n >= nt[10]:
        print('→ your mention is : A.Bien',end=' ')
        #,bold=True,colore='#FFA500'

    elif nt[13] >= n and n >= nt[12]:
        print('→ your mention is : Bien',end=' ')
        #,bold=True,colore='#FFFF00'
    
    elif nt[19] >= n and n >= nt[14]:
        print('→ your mention is : T.Bien',end=' ')
        #,bold=True,colore='#ADFF2F' 

    elif nt[7] <= n and n <= nt[10]:
        print('→ your mention is : Admis',end=' ')
        #,bold=True,colore='#FF8000'
    
    elif nt[0] <= n and n <= nt[7]:
        print('→ your mention is : Ajorné',end=' ')
        #,bold=True,colore='#FF0000'
    else:
        print('--->> Your over the set point x/20 ...')        
    print() 

def avg():
   print()
   n1 = int(input('How many Notes ?.. '))
   print()
   t = 0
   for n in range(n1):
       n+=1
       n2 = float(input('Here → your Note N° %d: ' %n))
       t += n2
   on = t / n1
   print()
   print('Average of %d on %d is %.2f'%(t,n1,on))
   note(on)

def cap():
    question = str(input('→(vol) for cylinder... ,and →($) for desk... : ')).lower()
    print()
    if question == '$':
        r1 = float(input('Enter the rayone of this circle → ($) :'))
        print()
        p1 = 2*pi*r1
        a1 = pi*pow(r1,2)
        print('The perimeter of ($) is : %.2f and the area of ($) is : %.2f '%(p1,a1))

    elif question == 'vol' or question == 'v' :
        r2 = float(input('Enter the rayone of this cylinder → (C) :'))
        h = float(input('Enter the height of this cylander → (C) :'))
        print()
        p2 = 2*pi*r2
        vol = h*pi*pow(r2,2)
        ls = 2*pi*r2*h
        s = 2*pi*r2*(r2+h)
        print('The perimeter of (C) is : %.2f and the letural area of (C) is : %.2f '%(p2,ls))
        print('And the total area of (C) is %.2f and the volume of it is %.2f'%(s,vol))

def maxe():
    n1 = int(input("enter value of a : "))
    n2 = int(input("enter value of b : "))
    if n1 > n2 or n2 > n1:
        mx = max(n1,n2)
        mn = min(n1,n2)
        print('this number {} great than {}'.format(mx,mn))
    elif n1 == n2 :
        print('in this situation  {} - {} = {} nothing to compare'.format(n1,n2,0))

def duo():
    n1 = int(input("enter value of a : "))
    n2 = int(input("enter value of b : "))
    try:
        if n1 == 0 or n2 == 0 :
            print('{} and {} inexpected value for duo() function cause any 0/x = 0'.format(n1,n2))
        elif n1 % 2 == 0 and n2 % 2 == 0:
            print('{} and {} boute are double'.format(n1,n2))
        elif n1 % 2 == 0 and n2 % 2 != 0:
            print('{} is double but {} is odd number'.format(n1,n2))
        elif n1 % 2 != 0 and n2 % 2 == 0:
            print('{} is double but {} is odd number'.format(n2,n1))
        else:
                print('{} and {} boute are odd numbers'.format(n1,n2))
    except ValueError :
        print('inexpected value for duo() function')

def equa1():
    print()
    print('----> ax+b=0 SOLVER <----')
    a = int(input('Entre value of a : '))
    b = int(input('Entre value of b : '))
    e = ('f(x) = '+str(a)+'×'+'+'+str(b)+' = 0')
    print()
    print(e)
    print()
    try:
        if a == 0 and b == 0:
            print('the solution of {} is reel set (IR)..'.format(e))
        elif a == 0 and b != 0:
            print('the solution of {} is empty set (Ø)..'.format(e))
        else:
            x = -b/a
            print('the solution of ({}) is {:.2f} ∈ (IR):]-∞;+∞[ ..'.format(e,x))

    except ValueError :
        print('inexpected value for {} function'.format(e))

def equa2():
    print()
    print('----> ax²+bx+c=0 SOLVER <----')
    a = int(input('Enter value of  a = '))
    b = int(input('Enter value of  b = '))
    c = int(input('Enter value of  c = '))
    f =  ('ƒ(x) = '+str(a)+'×² '+'+ '+str(b)+'× + '+str(c)+' = 0')
    fi = ('ƒ(x) = '+str(a)+'z² '+'+ '+str(b)+'z + '+str(c)+' = 0')
    print()
    try:
        if a != 0:
            d = (b**2)-(4*a*c)
            if d == 0:
                print('{} accepte one solution on reel set (IR)..'.format(f)) 
                x = -b/(2*a) 
                print('that solution is X = {}'.format(x))

            elif d > 0 :
                print('{} accepte tow solution on reel set (IR)..'.format(f))
                x1 = (-b-sqrt(d))/(2*a)
                x2 = (-b+sqrt(d))/(2*a)
                print('that solutions is X1 = {}'.format(x1))
                print('----------> and.. X2 = {}'.format(x2))

            elif d < 0:
                d = d*-1
                print('{} accepte tow solution on complex set (C)..'.format(fi))
                z1 = (-b-complex(0,sqrt(d))) / (2*a)
                z2 = (-b+complex(0,sqrt(d))) / (2*a)
                print('that solutions is Z1 = {:.2f}'.format(z1))
                print('----------> and.. Z2 = {:.2f}'.format(z2)) 
        elif a == 0:
            if b != 0:
                print(' your format will be '+str(b)+'x+'+str(c)+'= 0 then..')
                s = -c/b
                print(' the solution of this format is x = {:.2f}'.format(s))

    except Exception:
        print('somethig wrong in your format equation.. ☻')

def fectoriall():
    v = int(input('for vectoriall enter value of  !x '))
    m = 1
    for i in range(int(v)):
        i+=1
        m = m * i
        if v <= 10:
            print(i,end=' x ')
    print('the vectoriall of ',v,' is  = ',m)

def sum():
    s = int(input("start  = "))
    f = int(input("finish = "))
    k = 0
    for i in range(s,f):
        i+=1
        k += i
    print('the somme of repeat from ',s,' to ',f,' is : ',k)

 
def prem():
    p=int(input('enter a number to check if is premary: '))
    m = False
    for i in range(2,p):
        if p % i == 0:
            m = True
            print('this value ',p,' isn\'t premary number')
            break
            
    if m == False:
        print('this value ',p,' is premary number')

def rps():
    import random
    print('              ------> RPS GAME <------')
    chek = True
    win = 0
    lose = 0
    tie = 0
    while chek :
        choices =["rock","paper","scissorcs","r","p","s"]
        computer = random.choice(choices)
        player = None
        while player not in choices:
            print('======================')
            player = input('|rock|paper|scissorcs|. ?: ').lower()
            print('======================')
            
           
        if player == computer:
            print('computer: ',computer)
            print('player: ',player)
            print('Tie!..')
            tie+=1
        elif player == 'rock' or player == 'r':

            if computer == 'paper' or player == 'p':
                print('computer: ',computer)
                print('player: ',player)
                print('You lose!..')
                lose+=1

            if computer == 'scissorcs'or player == 's':
                print('computer: ',computer)
                print('player: ',player)
                print('You Win!..')
                win+=1
    
        elif player == 'scissorcs' or player == 's':

            if computer == 'rock':
                print('computer: ',computer)
                print('player: ',player)
                print('You lose!..')
                lose+=1

            if computer == 'paper' or player == 'p':
                print('computer: ',computer)
                print('player: ',player)
                print('You Win!..')
                win+=1
    
        elif player == 'paper' or player == 'p':

            if computer == 'scissorcs' or player == 's':
                print('computer: ',computer)
                print('player: ',player)
                print('You lose!..')
                lose+=1

            if computer == 'rock' or player == 'r':
                print('computer: ',computer)
                print('player: ',player)
                print('You Win!..')
                win += 1
        
        agin = input('want to play agin (yes/no): ').lower()
        if agin == 'yes' or agin == 'y':
            chek = True
        else:
            #[print(xp.count(item),item)for item in set(xp)]
            print("You score is %d win out of %d lose and %d tie!.. "%(win,lose,tie))
            print('BYE..!')
            break
def rgn():
    import random , getpass
    print('              ------> RGN GAME <------')
    level = int(input('Enter level of guesses: '))
    if level % 2 != 0 and level > 100:
       print('  │')
       print('  └─> your level game is not acceptable , sholdn\'t be odd number(2,7,9,11...) and great than 100' )
    else:
        print('1 ---> player1 vs player2')
        print('2 ---> player vs computer')
        menu = input('i want to play__ ')
        match menu:
            case '2':
                game2 = True
                com = random.randint(1,level)
                score = 0
                cp = 0
                while game2:
                    print('─'*40)
                    guess = int(input("Guess a number between (1 - "+str(level)+") : "))
                    system_color2 = ['9','a','b','c','d','e','f']
                    color2 = random.choice(system_color2)
                    os.system('color {}'.format(color2))
                    if guess <= level:
                        cp += 1
                        print('─'*40)
                        if com == guess:
                            print('You got it right !')
                            print('  │  ┌───────────────'+'─'*len(str(com))+'──┐')
                            print('  └─>│computer chose :'+str(com)+' │')
                            print('     └───────────────'+'─'*len(str(com))+'──┘')
                            print('     │  ┌────────────'+'─'*len(str(guess))+'──┐')
                            print('     └─>│  you guess :'+str(guess)+' │')
                            print('        └────────────'+'─'*len(str(guess))+'──┘')
                            score += 1
                            game2 = False
                            print()
                            print('you guess '+str(score)+' time..! out of '+str(cp))
                            print('─'*40)

                    else:
                        print("__your guess "+str(guess)+" out of guesses level "+str(level)+"__ ☻")
                        agin = input('want to play agin (yes/no): ').lower()
                        print()
                        if agin == 'yes' or agin == 'y':
                            game2 = True
                        else:
                            print('BYE.....')
                            game2 = False
            case '1':
                game1 = True
                player1 = int(getpass.getpass('Enter a number to guess it..: '))
                while player1 > level:
                    print("└──┬──┘")
                    print("   │")
                    print("   └─> your number should be less/equal level of guesses ( "+str(player1)+" ≤ "+str(level)+" )")
                    print()
                    player1 = int(getpass.getpass('Enter a number to guess it..: '))

                score1 = 0
                cp1 = 0
                while game1:
                    print('─'*40)
                    player2 = int(input("Guess a number between (1 - "+str(level)+") : "))
                    system_color1 = ['9','a','b','c','d','e','f']
                    color1 = random.choice(system_color1)
                    os.system('color {}'.format(color1))
                    if player2 <= level and player1 <= level:
                        cp1 += 1
                        print('─'*40)
                        if player1 == player2:
                            print('You got it right !')
                            print('  │  ┌───────────────'+'─'*len(str(player1))+'──┐')
                            print(f'  └─>│ player1 chose :{player1}'+' │')
                            print('     └───────────────'+'─'*len(str(player1))+'──┘')
                            print('     │  ┌──────────────'+'─'*len(str(player2))+'──┐')
                            print('     └─>│   you guess :'+str(player2)+'  │')
                            print('        └──────────────'+'─'*len(str(player1))+'──┘')
                            score1 += 1
                            game1 = False
                            print()
                            print('you guess '+str(score1)+' time..! out of '+str(cp1))
                            print('─'*40)

                    else:
                        print("__your guess "+str(player2)+" out of guesses level "+str(level)+"__ ☻")
                        agin = input('want to play agin (yes/no): ').lower()
                        print()
                        if agin == 'yes' or agin == 'y':
                            game1 = True
                        else:
                            print('BYE.....')
                            game1 = False
def fizzbuzz():
    print()
    print('  + 1 --> simple  FizzBuzz  ^_^') 
    print('  + 2 --> advance FizzBuzz  +_+')
    print('  + 3 --> super   FizzBuzz  O_O')
    print()
    print("    + type 'help()' for not understanding__ ")
    print()
    key = True
    while key:
        print()
        switch = input('your choise ')
        opn = True
        while opn:
            if switch == 'help()' or switch == 'help':
                print("   │")
                print("   └─> it's a game to check if a number is divisable by 3 \n +it's turn 'Fizz' same for 5 but it's turn to 'Buzz' \n +but if that number is divisable by 3 and 5 in same time\n +it's turn 'FizzBuzz' ")
                print("   │")
                print("   └─> for super fizzbuzz it will search for evry(x)%(3,5,3&5,7,11,13)=0")
                print()
                opn = False
            else:
                key = False
                match switch:
                    case '1':
                        n = int(input("put a number → "))
                        if n % 3 == 0 and n % 5 == 0:
                            print('FizzBuzz')
                        elif n % 5 == 0:
                            print('BUZZ')
                        elif n % 3 == 0 :
                            print('Fizz')
                        else:
                            print(n) 
                    case '2':
                        s = int(input('from(start)  → '))
                        f = int(input('to(finish)   → '))
                        fizz = 0
                        buzz = 0
                        fizzbuzz = 0
                        for i in range(s,f+1):
                            if i % 3 == 0 and i % 5 == 0:
                                fizzbuzz += 1
                            elif i % 3 == 0:
                                fizz += 1
                            elif i % 5 == 0:
                                buzz += 1   
                        print("from %d to %d there is: %d Fizz and %d Buzz and %d FizzBuzz"%(s,f,fizz,buzz,fizzbuzz))
                    case '3':
                        s = int(input('from(start)  → '))
                        f = int(input('to(finish)   → '))
                        fizz = 0
                        buzz = 0
                        fizzbuzz = 0
                        fuzz = 0
                        bizz = 0
                        biff = 0
                        for i in range(s,f+1):
                            if i % 3 == 0 and i % 5 == 0:
                                fizzbuzz += 1
                            elif i % 3 == 0:
                                fizz += 1
                            elif i % 5 == 0:
                                buzz += 1   
                            elif i % 7 == 0:
                                fuzz += 1
                            elif i % 11 == 0:
                                bizz += 0
                            elif i % 13 == 0:
                                biff += 1
                        print("from %d to %d there is: %d 'FIZZ' and %d 'BUZZ' and %d 'FIZZBUZZ'"%(s,f,fizz,buzz,fizzbuzz))
                        print(" and for super FIZZBUZZ you have %d 'FUZZ' and %d 'BIZZ' %d 'BIFF'"%(fuzz,bizz,biff))

            break    

def product_calculator():
    print('')
    print('                                 -------> PRODUCT CALCULATOR <-------             ')
    print()
    l = [['s','si','sir'],['m','me','mem']]
    n = None
    gen = None
    while not n:
        n = input('Enter your name: ')
        if n.isdigit() == True:
            n = None
            print("  we don't support digit names..!?")
    while not gen :
        gen = input('(Sir ♂ / Mem ♀)?: ').lower()
        if gen in l[0] or gen in l[1] :
            break
        else :
            gen = None
            print('we don\'t support other or empty gender... ☻')
            
    print()
    pi = []
    pr = []
    u = True
    p = 0
    try:
        while u == True :
            pr.append(float(input('Enter your product price: ')))
            
            for i in range(len(pr)):
                if pr[i] < 0:
                    pr.clear()
                    chek  = False
                else:
                    chek = True
            if chek  == False:
                print('Have you ever heart about negative price (-p) ☻')
                print()
            elif chek  == True :   
                pi.append(float(input('How many pieces: ')))
                o = input('add new product...! ')
    
            
           
                print('')
                if o == 'y' or o == 'yes' :
                    u == True
                elif o != 'y' and o != 'yes' :
                    u == False
                    for e in range(len(pr)):
                        p += float(pr[e] * pi[e])
                        rl = p*20
                    print('┌'+'────────────────────┬─'+'─'*2*len(str(rl))+'───┐')
                    print('│ the total price is │ %.2f DH'%p+' '*len(str(rl))+'│')
                    print('├'+'────────────────────┼─'+'─'*2*len(str(rl))+'───┤')
                    print('│ the total price is │ %.2f RL'%rl+' '*len(str(rl))+'│')
                    print('└'+'────────────────────┴─'+'─'*2*len(str(rl))+'───┘')
                    print()   
                    s = float(input(str(n.upper())+' enter your pyement in DH...: '))
                    print('')
                    if s > p and gen in l[0] :
                        r = (s-p)
                        print('Sir '+str(n.upper())+' your return is: %.2f'%r) 
                    elif s > p and gen in l[1] :
                        r = (s-p)
                        print('Mem '+str(n.upper())+' your return is: %.2f'%r) 
                    elif s == p and gen in l[0] :
                        print('Sir '+str(n.upper())+' you have no return...')   
                    elif s == p and gen in l[1]:
                        print('Mem '+str(n.upper())+' you have no return...' )  
                    else:
                            print('your pyement is under the Total price')
                    print('')
                    print('                    -------> THANK YOU '+str(n.upper())+' FOR USING PRODUCT CALCULATOR <-------')
                    print('')
                    break
    #-----> this blockes turn Erorrs structers to manuall explicaction.
    except Exception as e:
        print(str(e),'__SOMETHING WENT WRONG__  :(')
    
    except SyntaxError as e:
        print(str(e),'some structers are false... ☻')
    
    except ValueError as e:
        print(str(e),'Enter only numbrers...☻')


def quiz_game():
    print()
    print(' '*30+'┌────────────┐')
    print(' '*25+'─'*5+'│ QUIZE GAME │'+'─'*5)
    print(' '*30+'└────────────┘')
    print()
    def new_game():
        guesses = []
        correct_guesses = 0
        question_num = 1
        for key in question:
            print('─'*30)
            print(key)
            for i in options[question_num-1]:
                print(i)
            print('─'*30)
            guess = input('guess answer (A/B/C/D): ').lower()

            guesses.append(guess)
            correct_guesses += check_answer(question.get(key),guess)
            question_num += 1
        display_score(correct_guesses,guesses)

    def check_answer(answer,guess):
        if answer == guess:
            print('  ■ CORRECT...👍')
            return 1
        else:
            print('  ■ WRONG...👎')
            return 0

    def display_score(correct_guesses,guesses):
        print()
        print("┌"+"─"*2+"RESULT:"+"─"*4*len(guesses)+"┐")
        print("│ANSWERS: ",end=" ")
        for i in question:
            print((question.get(i)).upper(), end=" "+' │')
        print()
        print("│GUESSES: ",end=" ")
        for i in guesses:
            print(str(i).upper(), end=" "+' │')
        print('\n'+'└'+'─────────'+'─'*4*len(guesses)+'┘')


        score = int((correct_guesses/len(question))*100)
        print('┌'+14*'─'+'┬'+'─'*len(str(score))+3*'─'+'┐')
        print('│Your score is │ '+str(score)+'%'+' │')
        print('└'+14*'─'+'┴'+'─'*len(str(score))+3*'─'+'┘')

        if score == 100 :
            print()
            print('                 ██  █  █▌  █▀▀▀  █▀▀▀')
            print('                 █ █ █  █▌  █     █■■')
            print('                 █  ██  █▌  █▄▄▄  █▄▄▄')
            print()

    def play_again():
        import os , random
        respons = input('do you want to play again..? ').lower()
        if respons == 'yes' or respons == 'y':
            system_color = ['9','a','b','c','d','e','f']
            color = random.choice(system_color)
            os.system('cls')
            os.system('color {}'.format(color))
            return True 

        else:
            os.system('cls')
            return False

    question = {
        "► WHO CREATE PYTHON ?: ":"a",
        "► WHAT YEAR WAS PYTHON CREATED.?: ":"b",
        "► PYTHON IS TRIBUTED TO WICH COMEDY GROUP.?: ":"c",
        "► IS THE EARTH ROUND.?: ":"a",
        "► WHAT'S FIRST PROGRAMMING LANGUGE IN THE WORLD":"d",
        "► HOW MANY COUNTERIES IN THE WORLD":"c",
        "► HOW MANY 'FISH' IN OCEAN ..?":"b",
        "► HOW MANY COLORS YOU CAN SEE..?":"a",
        "► COMPLET: ∆ ☺ H ♦ │ ♠ S ☻ ► │ ☺ ▼ ♥ N│ .... │":"d",
        "► COMPLET: ▄▀█▄ + ▄█▄ ═ ?":"b",
        "► 141 : 5926 / 5358 / ...?":"c",
        "► LAST QUESTION: WHAT DOES COW DRINK ?":"d"
    }

    options = [["A. Guido van Rossum","B. Elon Mask","C. Harry Poter","D. Mark Zuckerburg"],
               ["A. 1984","B. 1991","C. 1997","D. 1940"],
               ["A. Green land","B. Smosh","C. Monty Python","D. SNL "],
               ["A. True","B. False","C. Sometimes","D. What is earth ? "],
               ["A. C","B. java","C. boolein","D. bainary"],
               ["A. 193","B. 195","C. 230","D. 215"],
               ["A. 7","B. 0","C. 130 000 000","D. 22456.68E46"],
               ["A. 3","B. 7","C. 14","D. 16 000 000"],
               ["A. ► ☻ ♦ X","B. ♥ ☺ ▲ I","C. W ♣ ☺ ◄","D. Z ♣ ◄ ☻"],
               ["A. 9","B. 1","C. 3","D. 0"],
               ["A. 8145","B. 5624","C. 9793","D. 6973"],
               ["A. Cocacola","B. Milk","C. Juece","D Water"]]
    new_game()
    while play_again():
        new_game()
    print(" Bye..")                           
                
##________________________________________________________________________________________________

print()
import os
os.system('color f')
try:
    def help():
        print(' '*26+'╔════════════════════╗')
        print(' '*26+'║ IRIGULAR FUNCTIONS ║')
        print('╔'+'═'*25+'╩════════════════════╩'+'═'*25+'╗')
        print('║ REF   ║ →  math functions(AVERAG/SOMATION/ODD NUMBERS/FECTORIAL)       ║')
        print('╠'+'═══════╬'+'═'*64+'╣')
        print('║ PRD   ║ →  function that calcule your product price times pieces of it ║')
        print('╠'+'═══════╬'+'═'*64+'╣')
        print('║ slove ║ →  (solve equation like (ax+b=0) or (ax²+bx+c=0))              ║')
        print('╠'+'═══════╬'+'═'*64+'╣')
        print('║  O    ║ →  calcule the vol(V),perimeter(P),area(A)[cyrcle/cylander]    ║')
        print('╚'+'═══════╩'+'═'*64+'╝')
        print()
    help()
    chek = True
    while chek :
        print('╔══════════════════════════════════════════╗╔═══╦═══╦═══╦═══╦═══╗')
        x = input("║ Enter regular/iregular ↑ symboll between ║║ + ║ - ║ x ║ / ║ ^ ║ : ").lower()
        print('╚══════════════════════════════════════════╝╚═══╩═══╩═══╩═══╩═══╝')
        l = ['solve','solve^1','solve^2']
        y = True
        while y:
            if x == 'o' or x == 'm' or x == 'game' or x == 'ref' or x == 'prd' or x in l :
                y = False 
            else:
                y = True
                a = int(input("Enter a number: "))
                b = int(input("Enter another number: "))
                y = False
                chek = False
                break



        match x:
            case '+':
                print(a,' + ',b, ' = ',plus(a,b))
            case '-':
                print(a,' - ',b, ' = ',sub(a,b))
            case 'x':
                print(a,' x ',b, ' = ',mul(a,b))
            case '/':
                deuc(a,b)
            case '^':
                print(a,' ^',b, ' = ',pow(a,b))
            case 'o':
                cap()
            case 'ref':
                print()
                print('  ».1 →  M   │  averag numbers(pour calcule la moyen du nombers)')
                print('  ».2 →  MAX │  for comperation numbers (a<b or a>b)')
                print('  ».3 →  DUO │  for double / odd numbers (for classification numbers odd/double)')
                print('  ».4 →  SUM │  calculate the sum of a numerical sequence (start+i+i+i...+finish)')
                print("  ».5 →  FEC │  fectorial (a!) of a number 'a' (1x2x3x....xa)")
                print ()
                calls = ['m','max','duo','sum','fec']
                digit = ['1','2','3','4','5']
                find = True
                while find:
                    med = input('choise from menu__ ').lower()
                    if med in calls or med in digit:
                        find = False
                        if med ==  calls[0] or med == digit[0]:
                            avg()
                        elif med ==  calls[1] or med == digit[1]:
                            maxe()
                        elif med ==  calls[2] or med == digit[2]:
                            duo()
                        elif med ==  calls[3] or med == digit[3]:
                            sum()
                        elif med ==  calls[4] or med == digit[4]:
                            fectoriall()
                    else:
                        print(str(med)+' not found in the menu 😓')
                        find = True
            case 'prd':
                product_calculator()
        if x in l:
            if x == l[0]:
                print()
                print('\t1--> solve for  ax+b=0 ')
                print('\t2--> solve for  ax²+bx+c=0 ')
                deg = str(input('Enter your choise: ')).lower()
                if deg == '1' :
                    equa1()
                if deg == '2' :
                    equa2()
            if x == l[1]:
                equa1()
            if x == l[2]:
                equa2()
        elif x == 'game':
                print()
                print('\t A ├► RPS GAME [rock|paper|scissorcs]')
                print('\t B ├► RGN GAME [random guess number]')
                print('\t C ├► FIZZBUZZ GAME')
                print('\t D ├► QUIZE GAME')
                tab = input('Enter your choise: ').lower()
                if tab == 'a' :
                    rps()
                if tab == 'b' :
                    rgn()
                if tab == 'c' :
                    fizzbuzz()
                if tab == 'd' :
                    quiz_game()
        print()
        ch = input('Continue__ ').lower()
        if ch == '' :
            clear()
            os.system('color f')
            help()
            chek = True
        elif ch == 'help':
            help()
            chek = True


#-----> this blockes turn Erorrs structers to manuall explicaction.
except ZeroDivisionError as e:
    print(str(e),'you can\'t divide by zero ! idiot! 😒')

except Exception as e:
    print(str(e),'__something went wrong__ 😢')

except ValueError as e:
    print(str(e),'Enter only numbrers...😔')

except SyntaxError:
    print('YOU HAVE MISSE SOMETHIG...↑')
#--------------------------------------------->

print()
print('     ---> YB <---')
print()
