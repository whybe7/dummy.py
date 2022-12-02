def russian_egypt_product() -> int :
    a,b = input("input a number: ").split()
    a = int(a)
    b = int(b)
    result = 0
    while a > 0:
        if a % 2 != 0:
            result += b
        a //= 2
        b *= 2
    print(result) 

def search_element():
    elements = []
    f = True
    i = 0
    print("*"*6+" array items "+"*"*6)
    while f :
        i+=1
        elements.append(int(input(">\telement N'%d: "%i)))
        for ele in elements:
            if ele == 0 :
                f = False
                elements.pop()
                print("> array elements: ",elements)
                search = int(input("> search for: "))
                
                if search in elements:
                    
                    elements_map = {element:[] for element in set (elements)}
                    for index, element in enumerate(elements):
                        elements_map[element].append(index)
                    print("> your element %d in position indexes:"%(search),elements_map[search])

                else:
                    print('> that element( %d ) out of elements..!'%search)
                
def duplicate_element():
    elements = []
    f = True
    i = 0
    behind = 1
    print("*"*6+" array items "+"*"*6)
    while f :
        i += 1
        elements.append(int(input(">\telement N'%d: "%i)))
        for ele in elements:
            if ele == 0:
                f = False
                elements.pop()
                print("> array elements: ",elements)
                search = int(input("> search behind: "))
                plc  = elements.index(search)
                if search == elements[0]:
                    behind = 0
                else:
                    for i in range(elements[0],plc):
                        behind += 1
                print("> your number %d have %d elements behind.."%(search,behind))

def remove_element():
    elements = []
    find = []
    f = True 
    i = 0
    print("*"*6+" array items "+"*"*6)
    while f :
        i += 1
        elements.append(input(">\t element N'%d: "%i).lower())
        for ele in elements :
            if ele == '0' or ele == 'done':
                f = False
                elements.pop() 
                print("> array elements: ",elements)
                remove = input("> from array remove: ").lower()
                try:
                    while remove not in elements:
                        for element in elements:
                            if element[0] == remove[0]:
                                find.append(element)
                        if len(find) != 0:
                            print("-> your element ('%s') must be spill wrong maybe you mean :"%remove,find)
                            remove = input("> from array remove: ").lower()
                        else:
                            print("> your element out of array",elements)
                            remove = input("> from array remove duplicate: ").lower() 
                              
                except ValueError as ve:
                    print('> %s out of  array..!'%ve)
                    remove = input("> from array remove: ").lower()        
            
                plc = elements.index(remove)
                for i in range(plc,len(elements)-1):
                    elements[i] = elements[i+1]
                elements.pop()
                len(elements)-1
                print("> array after removing: ",elements)

def remove_duplicate():
    elements = []
    cleanArr = [] 
    find = []
    f = True 
    i = 0
    print("*"*6+" array items "+"*"*6)
    while f :
        i += 1
        elements.append(input(">\t element N'%d: "%i).lower())
        for u in elements:
            if u == '0' or u == 'done':
                f = False
                elements.pop()
                for item in elements:
                    if item not in cleanArr:
                        cleanArr.append(item)
                print("> array elements: ",elements)
                remove = input("> from array remove duplicate: ").lower()
                try:
                    while remove not in cleanArr :
                        for element in cleanArr:
                            if element[0] == remove[0]:
                                find.append(element)
                        if len(find) != 0:            
                            print("-> your element ('%s') must be spill wrong maybe you mean :"%remove,find)
                            remove = input("> from array remove duplicate: ").lower()
                        else: 
                            print("> your element out of array",cleanArr)
                            remove = input("> from array remove duplicate: ").lower()
                            
                except ValueError as ve:
                    print('> %s out of  array..!'%ve)
                    remove = input("> from array remove duplicate: ").lower()
                    
                plc = cleanArr.index(remove)
                for i in range(plc,len(cleanArr)-1):
                    cleanArr[i] = cleanArr[i+1]
                cleanArr.pop()
                len(cleanArr)-1
                print("> array after removing occurance: ",cleanArr)
                
def change_place():
    elements = []
    f = True
    i = 0
    while f :
        i += 1
        elements.append(input(">\t element N'%d: "%i).lower())
        
        for ele in elements:
            if ele  == '0' or ele == 'done':
                if  len(elements) > 1:
                    f = False
                    elements.pop()
                    print("> array elements: ",elements)
                    try:
                        fir = int(input(">\tchange the index: "))
                        sec = int(input(">\tby the index: "))
                    
                        temp = elements[fir]
                        elements[fir] = elements[sec]
                        elements[sec] = temp  
                        print("> array elements: ",elements)
                    except IndexError as ie:
                        print(ie)
                    except TypeError as te:
                        print(te)
                else:
                    print("> at least the lenght of array must be > 2")
                    f = True 
                    i = 0
                    
                
def revers_array():
    array = []
    f = True
    i = 0
    while f :
        i += 1 
        array.append(input(">\t element N'%d: "%i).lower()) 
        for ele in array:
            if ele  == '0' or ele == 'done':
                f = False
                array.pop()
                print("> array elements: ",array)
                for index in range(len(array)//2):
                    array[index],array[-index-1] = array[-index-1],array[index]     
                print("> revers array elements: ",array)
                
def addsert(arr:list,element:object,place:int):
    arr.append(element)
    for index in range(len(arr)-1,place,-1):
        arr[index] = arr[index-1]
    arr[place] = element
    len(arr)+1
                    
def insert_element():
    elements = []
    f = True 
    i = 0
    print("*"*6+" array items "+"*"*6)
    while f :
        i += 1
        elements.append(input(">\t element N'%d: "%i).lower())
        for ele in elements :
            if ele == '0' or ele == 'done':
                f = False
                elements.pop() 
                print("> array elements: ",elements)
                insert = input("> from array insert: ").lower()
                plc = int(input("> in index: "))
                addsert(elements,insert,plc)
                print("> array after inserting: ",elements)
 
def addsort(arr:list , element:object , pos:int):
    for index in range(len(arr)-1,pos,-1):
        arr[index] = arr[index-1]
    arr[pos] = element
    len(arr)+1
       
def sort_insert():
    arr = []
    i = 0
    f = True
    while f :
        i += 1
        arr.append(int(input(">\t element N'%d: "%i)))
        for ele in arr:
            if ele == 0:
                f = False
                arr.pop()
                print("> array elements: ",arr)
                for i in range(0,len(arr)-1):
                    if arr[i] <= arr[i+1]:
                        sor = True
                    else:
                        sor = False
                if sor :
                    insert = int(input("> insert in order: "))
                    arr.append(insert)
                    for j in range(0,len(arr)-1):
                        if insert <= arr[j]:
                            pos = arr.index(j)+1
                            break
                    print("pos = ",pos)
                    for index in range(len(arr)-1,pos,-1):
                        arr[index] = arr[index-1]
                    arr[pos] = insert
                    len(arr)+1
                    print("> array after order inserting: ",arr)

def upsort(array:list) -> bool:
    for index in range(0,len(array)-1):
        if array[index-1] <= array[index]:
            return True
        else:
            return False

def sort_check():
    arr = []
    i = 0
    f = True
    while f :
        i += 1
        arr.append(int(input(">\t elementN'%d: "%i)))
        for ele in arr:
            if ele == 0:
                f = False
                arr.pop()
                if upsort(arr):
                    print("> this array is sorted")
                else:
                    print("> this array is not sorted..!")

def quick_sort(arr:list):
    from random import randint
    if len(arr) < 2:
        return arr
    great,same,small = [],[],[]
    pivot = arr[randint(0,len(arr)-1)]
    for element in arr:
        if element < pivot:
            small.append(element)
        elif element == pivot:
            same.append(element)
        elif element > pivot:
            great.append(element)         
    return quick_sort(small) + same + quick_sort(great)
    
def extend_sort():
    arr1,arr2 = [],[]
    i = 0
    j = 0
    f1,f2 = True,True
    print("*"*6+" array 1 items "+"*"*6)
    while f1 :
        i += 1
        arr1.append(int(input(">\t element N'%d: "%i)))
        for ele in arr1:
            if ele == 0:
                f1 = False
                arr1.pop()
                print("> arr1 elements B.sort: ",arr1)
                if upsort(arr1) == False:
                    arr1s = quick_sort(arr1)
                    print("> arr1 elements A.sort: ",arr1s)
    
    print("*"*6+" array 2 items "+"*"*6)
    while f2:
        j += 1
        arr2.append(int(input(">\t element N'%d: "%j)))
        for ele in arr2:
            if ele == 0:
                f2 = False
                arr2.pop()
                print("> arr2 elements B.sort: ",arr2)
                if upsort(arr2) == False:
                    arr2s = quick_sort(arr2)
                    print("> arr2 elements A.sort: ",arr2s)                
    arr = arr1+arr2
    print("\n> the tow arrs no sort :",arr)
    arrs = quick_sort(arr)
    print("> the tow arrs sorted :",arrs)

def pascal_triangle(numRowes:int) -> list[list[int]]:
    res = [[1]]
    for i in range(numRowes-1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1])+1):
            row.append(temp[j]+temp[j+1])
        res.append(row)
    for j in range(1,len(res[-1]),-1):
        j = ' '
        for i in res:
            print((j+str(i)),end='')
                
def isSquear( squear:list ):                      
    result = True
    size = len(squear)
    for row in squear:
        if len(row) != size:
            result = False
            break
    return result 

def isMagic(squear:list):
    result = isSquear(squear)
    if result:
        total = []
        
        #diagonal /:
        sum = 0
        for same in range(len(squear)):
            sum += squear[same][same]
        total.append(sum)

        #diagonal \:
        sum = 0
        loc = len(squear)-1
        for row in range (len(squear)):
            sum += squear[row][loc]
            loc -= 1
        total.append(sum)
        
        #rows ── :
        sum = 0
        for row in range(len(squear)):
            for col in range(len(squear)):
                sum += squear[row][col]
            total.append(sum)
            sum = 0
        
        #col | :
        sum = 0
        for row in range(len(squear)):
            for col in range(len(squear)):
                sum += squear[col][row]
            total.append(sum)
            sum = 0
        
        value = total[0]
        for i in range(1,len(total)):
            if total[i] != value:
                result = False
                break
    return result

def magic_squear():
    l = int(input("Whats the lenght of this squear S(NxN): "))
    matrix = []
    d1 = []
    if l < 0:
        return l
    else:
        for row in range(l):
            matrix.append([])
            for col in range(l):
                matrix[row].append(int(input("> element (%d,%d): "%(row,col))))
        print(matrix)
        print(f"is this matrix(squear) magic ?: {isMagic(matrix)}")
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                d1.append(matrix[row][col])
            
    if l == 3 :      
        print('┌'+'─'*3+'┬'+'─'*3+'┬'+'─'*3+'┐')
        print('│'+' '+str(d1[0])+' '+'│'+' '+str(d1[1])+' '+'│'+' '+str(d1[2])+' '+'│')
        print('├'+'─'*3+'┼'+'─'*3+'┼'+'─'*3+'┤')
        print('│'+' '+str(d1[3])+' '+'│'+' '+str(d1[4])+' '+'│'+' '+str(d1[5])+' '+'│')
        print('├'+'─'*3+'┼'+'─'*3+'┼'+'─'*3+'┤')
        print('│'+' '+str(d1[6])+' '+'│'+' '+str(d1[7])+' '+'│'+' '+str(d1[8])+' '+'│')
        print('└'+'─'*3+'┴'+'─'*3+'┴'+'─'*3+'┘')
        

            

            
    
def Menu():
    print(' '*17+"┌────────────┐")
    print(" "*17+"│ Array Menu │")
    print('┌─────┬'+'─'*10+"┴────────────┴"+'─'*14+'┐')
    print("│  1  │ search for elements"+' '*18+"│")
    print("├─────┼"+"─"*38+"┤")
    print("│  2  │ search behind element"+' '*16+"│")
    print("├─────┼"+"─"*38+"┤")
    print("│  3  │ remove element from array"+' '*12+"│")
    print("├─────┼"+"─"*38+"┤")
    print("│  4  │ remove duplicate element array"+' '*7+"├"+"─"*11+'┐')
    print("├─────┼"+"─"*38+"┤"+" "*11+'│')
    print("│  5  │ change element place"+' '*17+"│"+' '*5+"┌"+'─'*5+"┼"+'─'*12+"┐")
    print("├─────┼"+"─"*38+"┤"+' '*5+"│"+'  0'+' '*2+"│"+' For Exit'+' '*3+"│")
    print("│  6  │ revers array"+' '*25+"│"+' '*5+"└"+'─'*5+"┼"+'─'*12+"┘")
    print("├─────┼"+"─"*38+"┤"+" "*11+'│')
    print("│  7  │ insert element"+' '*23+"├"+"─"*11+'┘')
    print("├─────┼"+"─"*38+"┤")
    print("│  8  │ sort insert"+' '*26+"│")
    print("├─────┼"+"─"*38+"┤")
    print("│  9  │ sort check"+' '*27+"│")
    print("├─────┼"+"─"*38+"┤")
    print("│ 10  │ sort and fussion 2 array"+' '*13+"│")
    print("├─────┼"+"─"*38+"┤")
    print("│ 11  │ Magic square"+' '*25+"│")
    print("└─────┴"+'─'*38+'┘')



Menu()
menu = list(range(0,12)) 
choice = eval(input("shose from Menu: "))
f = True
while f:
    if  choice not in menu:
        print("> your choice isn't in the menu...!")
        choice = eval(input("shose from Menu: "))
        f = True
    else:
        f = False
import os           
match choice:
    case 1:
        search_element()
    case 2:
        duplicate_element()
    case 3:
        remove_element()
    case 4:
        remove_duplicate()
    case 5:
        change_place()
    case 6:
        revers_array()
    case 7:
        insert_element()
    case 8:
        sort_insert()
    case 9:
        sort_check()
    case 10:
        extend_sort()
    case 11:
        magic_squear()
    case 0:
        os.system("cls")
if choice != 0:      
    respons = input("> want to repeat: ").lower()
    if respons == 'yes' or respons == 'y':
        os.system('cls')
        Menu()
        choice = eval(input("shose from Menu: "))
        f = True
       
        