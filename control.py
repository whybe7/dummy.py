def fillList(length:int ,type=str):
    lst = []
    if type == str:
        for index in range(length):
            lst.append(input(f"\t> list item index {index}: "))
        return lst
    
    if type == int:
        for index in range(length):
            lst.append(int(input(f"\t> list item index {index}: ")))
        return lst
    
def LstElementFind(lst:list[int|str], item:object):
    if item in lst:
        return lst.index(item)
    
def occurenc(lst:list[int|str]):
    itemsSet = set()
    for index in range(len(lst)):
        for element in range(index+1, len(lst)):
            if lst[index] == lst[element]:
                itemsSet.add(lst[element])
                
    occurencDict = {}
    itemsList = [*itemsSet] 
    for item in range(len(itemsList)):
        find = 0
        for occurenc in range(len(lst)):
            if itemsList[item] == lst[occurenc]:
                find += 1
                occurencDict[itemsList[item]] = find 
                
    return occurencDict
            
def lstRemove(lst:list[int|str], item:object):
    if item in lst:
        for index in range(LstElementFind(lst, item), len(lst)-1):
            lst[index] = lst[index+1]
        lst.pop()
        return lst        
    
def LstOccurencRemove(lst:list[int|str], *items:object, method='specific'):
    newList = []
    for index in range(len(lst)):
        while lst[index] not in newList:
            newList.append(lst[index])
        
    if method == 'specific':
        if items[0] != '':
            for item in items:
                lstRemove(newList, item)
            return newList
        return None
    if method == 'auto':
        occurencDict = occurenc(lst)
        
        for key in occurencDict.keys():
            lstRemove(newList, key)
        return newList
            
        
def swap(lst:list[int|str], item1:object, item2:object):
    if item1 in lst and item2 in lst:
        temp = lst[lst.index(item2)]
        lst[lst.index(item2)] = lst[lst.index(item1)]
        lst[lst.index(item1)] = temp
        return lst
            
def invers(lst:list[int|str]):
    for index in range(len(lst)//2):
        lst[index], lst[-index-1] = lst[-index-1], lst[index]
    return lst

def Insert(lst:list[int|str], item:object, position:int):
    lst.append('')
    for index in range(len(lst)-1, position,  -1):
        lst[index] = lst[index-1]
    lst[position] = item
    return lst
    
def sortInsert(lst:list[int], item:int):
    # position
    for i in range(len(lst)):
        if lst[i] >= item:
            position = i
            break
    # adding a empty slot
    lst.append('')
    # inserting
    for index in range(len(lst)-1, position, -1):
        lst[index] = lst[index-1]
    lst[position] = item
    return lst


def isSorted(lst:list[int]):
    itsSorted = True
    for item in range(len(lst)-1):
        if lst[item] > lst[item+1]:
            itsSorted = False
    
    return itsSorted

def bubbelSort(lst:list[int|str]):
    for pd in range(len(lst)):
        alreadySorted = True
        for nd in range(len(lst)-pd-1):
            if lst[nd] > lst[nd+1]:
                lst[nd], lst[nd+1] = lst[nd+1], lst[nd]
                alreadySorted = False
        if alreadySorted:
            break
    return lst

def insertionSort(lst:list[int|str]):
    for i in range(1, len(lst)):
        j = i
        while j > 0 and lst[j -1] > lst[j]:
            lst[j], lst[j -1] = lst[j -1], lst[j]
            j -= 1
    return lst   
            
    
def extendSort(*lists:list[int|str]):
    mergeList = []
    for list in lists:
        for item in bubbelSort(list):
            mergeList.append(item)
         
    return insertionSort(mergeList) 

def Shift(string:str, base='lowercase'):
    result = ''
    sample = string.split(' ')
    if base == 'lowercase':
        for word in range(len(sample)):
            worde = ''
            for c in range(len(sample[word])):
                worde += chr(ord(sample[word][c]) + (ord('a') - ord('A')))
            sample[word] = worde
            
    if base == 'uppercase':
        for word in range(len(sample)):
            worde = ''
            for c in range(len(sample[word])):
                worde += chr(ord(sample[word][c]) - (ord('a') - ord('A')))
            sample[word] = worde
    
    for word in range(len(sample)):
        result += sample[word]
        result += ' '
    return result.strip()

def Atoi(digit:str):
    start = 0
    sign = 1
    result = 0
    if digit[0] == '-':
        start = 1
        sign = -1
    for d in range(start, len(digit)):
        if digit[d] >= '0' and digit[d] <= '9':
            result += 10**(len(digit) - (d+1)) * (ord(digit[d]) - ord('0'))
            
    return sign*result

def matrixTransposition(matrix:list[list]):
    newMatrix = []
    for row in range(len(matrix)):
        newMatrix.append([])
        for col in range(len(matrix[row])):
            newMatrix[row].append(matrix[col][row])
    return newMatrix

def matrixRotation(matrix:list[list], times = 1):
    
    newMatrix = []
    for row in range(len(matrix)):
        newMatrix.append([])
        for col in range(len(matrix)):
            newMatrix[row].append(matrix[-col-1][row])
    return newMatrix           
        
def matrixsSum(matrix1:list[list[int]], matrix2:list[list[int]]):
    sumMatrix = [] 
    if len(matrix1) == len(matrix2) and len(matrix1[0]) == len(matrix2[0]):
        for row in range(len(matrix1)):
            sumMatrix.append([])
            for col in range(len(matrix2)):
                sumMatrix[row].append(matrix1[row][col] + matrix2[row][col])
                
    return sumMatrix

def matrixProduct(matrix1:list[list[int]], matrix2:list[list[int]]):
    prodMatrix = []                                                                                                                                                                                                                              
    if len(matrix1[0]) == len(matrix2):
        for row in range(len(matrix1)):
            prodMatrix.append([])
            for col in range(len(matrix2[0])):
                prodMatrix[row].append(0)
                for k in range(len(matrix2)):
                    prodMatrix[row][col] += matrix1[row][k] * matrix2[k][col]
    return prodMatrix 

def PascalTriangle(Xrows:int):
    result = [[1]]
    for i in range(Xrows-1):
        temp = [0] + result[-1] + [0]
        row = [] 
        for j in range(len(result[-1])+1):
            row.append(temp[j] + temp[j+1])
        result.append(row)
    return result
            
def pointCols(matrix:list[list[int]]):
    for row in range(len(matrix)):
        maxe = matrix[row][0]
        for col in range(len(matrix[row])):
            if matrix[row][col] > maxe:
                maxe = matrix[row][col]
                start = col
           
    for row in range(len(matrix)):          
        mine = matrix[0][start]
        for col in range(len(matrix[row])):
            if matrix[col][start] < mine:
                mine = matrix[col][start]
    if mine == maxe:
        return {mine: (col,start)}
            
     
def isUpperCase(sentence:str):
    for c in range(len(sentence)):
        if (sentence[c] >= 'a' and sentence[c] <= 'z') or (sentence[c] >= 'A' and sentence[c] <= 'Z'):
            if sentence[c] >= 'A' and sentence[c] <= 'Z':
                checked = True
            else:
                checked = False
    return checked

def matrixOcrChange(matrix:list[list[int|str]], ocr:str|int, trg:int|str):
    for row in range(len(matrix)):
        while ocr in matrix[row]:
            matrix[row][matrix[row].index(ocr)] = trg
    return matrix

def RJproduct(a:int, b:int):
    result = 0
    while a > 0:
        if a % 2 != 0:
            result += b
        a //= 2
        b *= 2

def a2i(s:str) -> int:
    digit = [*s]
    cleanDigit = []
    start = 0
    sign = 1
    result = 0
    for c in range(len(digit)):
        if digit[c] == '-':
            cleanDigit.insert(0, '-')
        if digit[c] >= '0' and digit[c] <= '9':
            cleanDigit.append(digit[c])
    if cleanDigit[0] == '-':
        start = 1
        sign = -1
    for d in range(start, len(cleanDigit)):
        result += 10**(len(cleanDigit) - (d+1)) * (ord(cleanDigit[d]) - ord('0'))

    return sign*result




mtrxpos = [[5 ,  2,  3],
         [-7,  8,  9], # pointcols = mtrx1[2][1] = -3
         [-6, -3, -4]]



mtrx = [[1, 2, 3],
        [2, 2, 6],
        [7, 2, 2]]

mtrx1 =[[7, 4, 1],                   
        [8, 5, 2], 
        [9, 6, 3]]

mtrx2 = [[9, 8, 7], 
         [6, 5, 4], 
         [3, 2, 1]]

mtrx3 = [[3, 6, 9],
         [2, 5, 8],
         [1, 4, 7]]

mtrx4 = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9]]

test = '       .,,.,.,.-232  HELLO   WORLD  '
print(a2i(test) + 2)