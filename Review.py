#------------Serie 1:    
from os import remove


def ex_1(a:int,b:int) -> int:
    if -13 <= a <= 13 and 0 <= b <= 8:
        result = list()
        result[0] = a*b
        result[1] = a/b
        result[2] = pow(a,b)
        for i in result:
            return result[i]

def ex_2(a:int,n:int):
    s = 0
    for i in range(0,n):
        s+= pow(a,n)/n

def ex_3(a:int)-> int:
    for i in range(1,11):
        s = a * i
        print(str(a)+' x '+str(i)+' = '+str(s))

def ex_4(a:int) ->int:
    for i in range(1,11):
        nextnum = a+i
        print(nextnum)
    
#f = True
#i = 0
#pos = 0
#arr =[]
#while f:
#    i += 1
#    arr.append(int(input("\tEnter value N•%d : "%i)))
#    for i in arr:
#        if i == 0:
#            f = False
#            print(arr)
#            x = int(input("Searsh for : "))
#            for n in arr:
#                if x == n:
#                    pos = n
#                    arr.pop()
#                    for j in range(0,len(arr)-1):
#                        arr[j] = arr[j+1]   
#                    arr[-1]-1  
#print(arr)
def Qsort(array:list) -> list[:int]:
    from random import randint
    if len(array) < 2:
        return array
    else:
        small,same,large = [],[],[]
        pivot = array[randint(0,len(array)-1)]
        for i in array:
            if pivot == i:
                same.append(i)
            if i < pivot:
                small.append(i)
            if i > pivot:
                large.append(i)
            
            
            
arr = ['1','hi','kill','9','cooca']
print(arr)
start_src = []
remove = input("remove from array: ").lower()
f = True
while f :
    if remove not in arr:
        for j in arr:
            if j[0] == remove[0]:
                start_src.append(j)
        print("-> your element ('%s') must be spill wrong... maybe you mean : "%(remove), start_src)

    else:
        f = False
        for i in arr:
            if remove == i :
                start_src.append(j)
print("-> your element ('%s') must be spill wrong... maybe you mean : "%(remove), start_src)

#for i in arr:
#    start_src.append(i[0])
#print(start_src)

