def sequence():    
    cileule = int(input("Enter a sequence to follow it : "))
    sequence = list(range(1,cileule+1))
    s= 0
    for i in sequence:
        print(i)
        s += i +1
        
    print(s)

def great_posfind():
    numbers = []
    f = True
    while f:
        numbers.append(int(input('Enter a number ')))
        mx = numbers[0]
        for num  in numbers:
            if num != 0 :
                if num > mx :
                    mx = num
            else:
                pos = numbers.index(mx)
                f = False   
    print (' the great number is %d in position %d'%(mx,pos+1))

def note(n):
     
    nt = list(range(1,21))
    for i in nt:
        i+=1
    if nt[11] >= n and n >= nt[10]:
        print('→ your mention is : A.Bien',end=' ')

    elif nt[13] >= n and n >= nt[12]:
        print('→ your mention is : Bien',end=' ')
        
    elif nt[19] >= n and n >= nt[14]:
        print('→ your mention is : T.Bien',end=' ')
        
    elif nt[7] <= n and n <= nt[10]:
        print('→ your mention is : Admis',end=' ')
       
    elif nt[0] <= n and n <= nt[7]:
        print('→ your mention is : Ajorné',end=' ')
    
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

def phrase():
    user = True
    phrase = []
    while user:
        phrase.append(str(input("phrase ")))
        for i in phrase:
            if i == "0":
                spc = phrase.index("0") 
                phrase[spc] = ' '
            if i == ".":
                phrase.pop()
                user = False
    for j in phrase:
        print(j,end='')

def search_element():
    elements = []
    f = True
    i = 0
    while f :
        i+=1
        elements.append(int(input("element N'%d: "%i)))
        for ele in elements:
            if ele == 0 :
                f = False
                search = int(input("search for: "))
                plc = elements.index(search)

                if ele == search:
                    same_srch = elements.index(ele)
                    print("your element %d in position %d and %d"%(search,plc+1,same_srch+1))
                else:
                    print("your element %d in position %d "%(search,plc+1))

                if search not in elements:
                    print('that element( %d ) out of  elements..!'%search)
def swap_iem(arr,iem1,iem2):
    temp = arr[iem1]
    arr[iem1] = arr[iem2]
    arr[iem2] = temp
    return temp
    

def part(arr,start,end):
    pivot = start
    pValue = arr[end]
    for i in range(start,end):
        if arr[i] < pValue:
            swap_iem(arr,i,pivot)
            pivot += 1
    swap_iem(arr,pivot,end)
    return pivot

def quickSort(arr,start,end):
    if start >= end:
        return
    index = part(arr,start,end)
    quickSort(arr,start,index-1)
    quickSort(arr,index+1,end)  

def quicksort(array):
   from random import randint
   if len(array) < 2:
       return array
   small,sam,large = [],[],[]
   pivot = array[randint(0,len(array)-1)]
   for item in array:
       if item < pivot:
           small.append(item)
       elif item == pivot:
           sam.append(item)
       elif item > pivot:
           large.append(item)
   return quicksort(small) + sam + quicksort(large)

def estPremiere(a:int):
    if a < 0:
        return False
    else:
        for i in range(2,a-1):
            if a % i != 0:
                return True
            return False

n = int(input("How many numbers "))
for i in range(1,n+1):
    if estPremiere(i):
        print(i)


    
    
