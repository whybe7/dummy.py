#import os
#path = "C:\\Users\\♦ Hatym ♦\\Desktop\\text.txt"
#
#if os.path.exists(path):
#    print('that location is exists')
#    if os.path.isfile(path):
#        print('that\' a file')
#else:
#    print('that location doesn\'t exists')
#text = '\nhiiiiiiiiiiiiiiiiiiiiii heeelloooo world'
#with open('text.txt','a') as file:
#    print(file.write(text))
#import shutil
#shutil.copyfile('text.txt','copy.txt')
#import os
#src ="C:\\Users\\♦ Hatym ♦\\Desktop\\test\\text.txt"
#des ="C:\\Users\\♦ Hatym ♦\\Desktop\\test\\text.txt"
#try:
#    n = input("sure wante delet "+src+" (Y/N):")
#    if n == 'y':
#        os.remove(src)
#        print(src+" was deleted..")
#    else:
#         print(src+" wasn't deleted..")
#        
#except FileNotFoundError:
#    print(src+" was not found")
#import random
#print('              ------> RPS GAME <------')
#while True:
#    choices =["rock","paper","scissorcs"]
#    computer = random.choice(choices)
#    player = None
#    while player not in choices:
#        player = input('rock/"paper/scissorcs. ?: ').lower()
#
#    if player == computer:
#        print('computer: ',computer)
#        print('player: ',player)
#        print('Tie!..')
#    elif player == 'rock':
#        if computer == 'paper':
#            print('computer: ',computer)
#            print('player: ',player)
#            print('You lose!..')
#        if computer == 'scissorcs':
#            print('computer: ',computer)
#            print('player: ',player)
#            print('You Win!..')
#
#    elif player == 'scissorcs':
#        if computer == 'rock':
#            print('computer: ',computer)
#            print('player: ',player)
#            print('You lose!..')
#        if computer == 'paper':
#            print('computer: ',computer)
#            print('player: ',player)
#            print('You Win!..')
#
#    elif player == 'paper':
#        if computer == 'scissorcs':
#            print('computer: ',computer)
#            print('player: ',player)
#            print('You lose!..')
#        if computer == 'rock':
#            print('computer: ',computer)
#            print('player: ',player)
#            print('You Win!..')
#    agin = input('want to play agin (yes/no): ').lower()
#    if agin != 'yes':
#        print('BYE..
#import getpass
#passowrd = getpass.getpass('Enter a password ')
#print(f"your password is --> {passowrd}")
#



from os import system


alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','u','r','s','t','w','x','y','z']
numbers = [0,2,1,3,4,5,8,7,9,11,12,13,14,17,]

def quiz_game():
    import os , random , time
    limit_time = 60
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
      #Timer  
    start_time = int(time.time())
    def check_answer(answer,guess):
        if answer == guess:
            print('  ■ CORRECT...👍')
            return 1
        else:
            print('  ■ WRONG...👎')
            return 0

    def display_score(correct_guesses,guesses):
        elapsed_time = int(time.time()-start_time)
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
        game_time = elapsed_time-start_time
        stp = 0
        if elapsed_time > limit_time:
            for j in range(1,game_time+1):
                if j % 5 == 0:
                    stp += 1
               
                for g in range(1,stp+1):
                    new_score = score - g*5
                print('┌'+14*'─'+'┬'+'─'*len(str(new_score))+3*'─'+'┐')
                print('│Your score is │ '+str(new_score)+'%'+' │')
                print('└'+14*'─'+'┴'+'─'*len(str(new_score))+3*'─'+'┘')
        else:
            print('┌'+14*'─'+'┬'+'─'*len(str(score))+3*'─'+'┐')
            print('│Your score is │ '+str(score)+'%'+' │')
            print('└'+14*'─'+'┴'+'─'*len(str(score))+3*'─'+'┘')
        if score == 100 :
            print()
            print('                 ██  █  █▌  █▀▀▀  █▀▀▀')
            print('                 █ █ █  █▌  █     █■■')
            print('                 █  ██  █▌  █▄▄▄  █▄▄▄')

    def play_again():
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
        "► ██████████████████████████ ..?":"c",
        "► COMPLET: ▄▀█▄ + ▄█▄ ═ ?":"c"
    }

    options = [["A. Guido van Rossum","B. Elon Mask","C. Harry Poter","D. Mark Zuckerburg"],
               ["A. 1984","B. 1991","C. 1997","D. 1940"],
               ["A. Green land","B. Smosh","C. Monty Python","D. SNL "],
               ["A. True","B. False","C. Sometimes","D. What is earth ? "],
               ["A. C","B. java","C. boolein","D. bainary"],
               ["A. 193","B. 195","C. 230","D. 215"],
               ["A. 7","B. 0","C. 130 000 000","D. 22456.68E46"],
               ["A. 3","B. 7","C. 14","D. 16 000 000"],
               ["A. ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄","B. ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄","C. ▄▄▄▄▄▄▄▄▄▄▄▄▄","D. ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄"],
               ["A. 9","B. 3","C. 1","D. 0"]]
    new_game()
    while play_again():
        new_game()
    print(" Bye..")




class Car:
    def __init__(self,make,model,color,year):
        self.make = make
        self.module = model
        self.color = color
        self.year  = year

class Animal:
    alive = True
    def eat(self):
        print("this animal is eating...")
    def sleep(self):
        print("this animal is sleeping...")
    
class Rabbit(Animal): 
    def run(self): 
        print("this rabbit is running")
        return self

class Fish(Animal):
    def swim(self):
        print("this fish is swimming")
        return self

class Hawk(Animal):
    def fly(self):
        print("this hawk is flying")

class Crocodile(Fish,Rabbit):
    def none(self):
        pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()
croco = Crocodile()

rabbit.run()
fish.swim()
hawk.fly()
croco.swim().run()