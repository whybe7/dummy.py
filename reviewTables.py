
def fillArray():
    arr = []
    flage = True
    i = 0
    while flage:
        arr.append(input(f"\t> element N'{i}: "))
        i += 1
        for element in range(len(arr)):
            if arr[element] == 'done' or arr[element] == '0':
                flage = False
                arr.pop()
    return arr

def searchElement(arr:list,element):
    error = f"this {element} not exist in array"
    if element in arr:
        obj = {element:arr.index(element)}
        return obj
    return error

def ocurenceElementInArr(arr:list):
    ocurencSet = set()
    for index in range(len(arr)):
        for element in range(index+1, len(arr)):
            if arr[index] == arr[element]:
                ocurencSet.add(arr[element])

    ocurencList = list(ocurencSet)
    ocurencDict = {}
    for item in range(len(ocurencList)):
        find = 0
        for ocurenc in range(len(arr)):
            if arr[ocurenc] == ocurencList[item]:
                find += 1
                ocurencDict[ocurencList[item]] = find
    return ocurencDict

def insertElementToArr(arr:list, element, position:int):
    error = f"this {element} not exist in array"
    arr.append(None)
    if position in range(len(arr)-1):
        for index in range(len(arr)-1, position, -1):
            arr[index] = arr[index-1]
        arr[position] = element
        len(arr)+1
        return arr 
    return error
    
def arrSwapElement(arr:list,element1,element2):
    error = f"this {element1} or {element2} not exist in array"
    if element1 in arr and element2 in arr:
        temp = arr[arr.index(element1)]
        arr[arr.index(element1)] = arr[arr.index(element2)]
        arr[arr.index(element2)] = temp
        return arr
    return error

def removeElementFromArr(arr:list, element):
    error = f"this {element} not exist in array"
    if element in arr:
        for index in range(arr.index(element), len(arr)-1):
            arr[index] = arr[index+1]
        arr.pop()
        len(arr)-1
        return arr
    return error

def removeElementsFromArr(arr:list, elements):
    error = f"this occurenc {elements} not exist in array"
    newArr = []
    if elements in arr:
        for element in arr:
            while element not in newArr:
                newArr.append(element)
        for index in range(newArr.index(elements), len(newArr)-1):
            newArr[index] = newArr[index+1]
        newArr.pop()
        len(newArr)-1
        return newArr
    return error
        
def reversArray(arr:list) :
    for index in range(len(arr)//2):
        arr[index], arr[-index-1] = arr[-index-1], arr[index]
    return arr
    
def sortInsetElement(arr:list,element):
    newArr = QuickSort(arr)
    for index in range(len(arr)-1):
        if element <= newArr[index]:
            position = index
            break
    insertElementToArr(newArr,element,position)
    return newArr

def pascalTraiangle(numRows:int):
    result = [[1]]
    for index in range(numRows-1):
        temp = [0] + result[-1] + [0]
        row = []
        for col in range(len(result[-1])+1):
            row.append(temp[col] + temp[col+1])
        result.append(row)
    return result

def QuickSort(arr:list):
    from random import randint
    if len(arr) < 2:
        return arr
    small, same, large = [], [], []
    pivot = arr[randint(0, len(arr)-1)]
    
    for element in arr:
        if element < pivot:
            small.append(element)
        elif element == pivot:
            same.append(element)
        elif element > pivot:
            large.append(element)
            
    return QuickSort(small) + same + QuickSort(large)

def BubbelSort(arr:list):
    for i in range(len(arr)):
        alreday_sorted = True
        for j in range(len(arr) - i -1):
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                alreday_sorted = False
        if alreday_sorted:
            break
    return arr

def sortAdd(arr:list, element):
    newArr = QuickSort(arr)
    newArr.append(None)
    for check in range(len(newArr)):
        if element <= newArr[check]:
            position = check
            break
            
    for index in range(len(newArr)-1, position, -1):
        newArr[index] = newArr[index-1]
    newArr[position] = element
    len(arr)+1
    return newArr

def add(arr:list, element, position:int):
    arr.append(None)
    if position in range(len(arr)):
        for index in range(len(arr)-1, position, -1):
            arr[index] = arr[index-1]
        arr[position] = element
        len(arr)+1
        return arr
    
    

arr = [1,4,7,5,9,6,2,8,0,3]
arr1 = [1,2,2,2,3,4,4,6,7,7,7,8,2,9,2]

# print(BubbelSort(arr))
# arr = fillArray()
# [1,2,4,5,6]
# print(arr)
# newArr = reversArray(arr)        
# print(newArr)



class Characters(str):
    
    def majuscule(self):
        majWord = ''
        for character in range(len(self)):
            if self[character] >= 'a' and self[character] <= 'z':
                majWord += chr(ord(self[character]) - (ord('a') - ord('A')))
        return majWord
    
    def miniscule(self):
        misWord = ''
        for character in range(len(self)):
            if self[character] >= 'A' and self[character] <= 'Z':
                misWord += chr(ord(self[character]) + (ord('a') - ord('A')))
        return misWord
    
    def rvrs(self:str):
        __result = [*self]
        word = ''
        for c in range(len(__result)):
            word += __result[-c-1]
        return word
    
    
        
    
dictionary = ['Ahmed', 'bam' , 'Mostapha', 'bin' , 'yassine', 'bader', 'ban' , 'Hamza' ,'bon' ,'Karim', 'siham', 'bon']
normaliseDict = []
for word in dictionary:
    normaliseDict.append(word.lower())
    
# for word in range(len(normaliseDict)):
#     for character in range(len(normaliseDict[word])):
#         if normaliseDict[word][character] >:

def bubbelSort(arr:list):
    for i in range(len(arr)):
        sort = True
        for j in range(len(arr)-i-1):
            if arr[j] >= arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                sort = False
        if sort:
            break
    return arr
    
def atoi(str:str, base = 10):
        __sign = 1
        __start = 0
        __result = 0
        if str[0] == '-':
            __sign = -1
            __start = 1
        for digit in range(__start, len(str)):
            __result += base**(len(str) - (digit + 1)) * (ord(str[digit]) - ord('0'))
            
        return __sign * __result


# print(dictionary)
# print(normaliseDict)
# print(bubbelSort(normaliseDict))                     
        
# test = 'YB'
# Chr = Characters(test)
# print(Chr.miniscule())

# if value in list(range(0,9)):
#     print('its a number')
#     print(list(range(0,9)))
# else: 
#     print('its not')

# test = 'bouba yb yassine'
# print(test)
# result = [*test]
# word = ''
# for c in range(len(result)):
#     word += result[-c-1]
    
# print(word)

# Chr = Characters(test)
# print(Chr.rvrs())
     
    

    
