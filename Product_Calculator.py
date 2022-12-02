from math import*

def product_calculator():
    print('')
    print('                                 -------> PRODUCT CALCULATOR <-------             ')
    print('')
    print('   ------>> YB ')
    print()
    l = [['s','si','sir'],['m','me','mem']]
    n = None
    gen = None
    
    
    while not n :
        n = input('Enter your name: ')
        if n.isdigit() == True:
            n = None
            print("we don't support digit names")
            
    while not gen :
        gen = input('(Sir/Mem)?: ').lower()
        if gen  in l[0] or gen  in l[1] :
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
        while u :
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
                        print('the total price is : %.2f DH '%p)
                    print('')   
                    s = float(input(str(n.upper())+' enter your pyement...: '))
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
    
    
#--------------------------------------------->
product_calculator()
           
                    
