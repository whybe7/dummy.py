
#----SSERIE 8 -----------------------

from math import floor


def n_power(x,n):
    result = 1
    for item in range(n):
        result = result * x
    return result
 
def raise_power( x: float, n: int) -> float:
    def check(x,n):
        if x == 0:
            return 0
        if n  == 0:
            return 1
        result = check(x * x,n // 2)
        if n % 2 :
            return x * result
        else:
            return result
    result = check(x, abs(n))
    if n >= 0:
        return result
    else:
        return 1 / result

def sin_ln(x):
    from math import sin,log,exp
    arr_x = []
    if x > 0 :
        fx =sin(x) + log(x,exp(1))
        arr_x.append(fx)
        return arr_x

def hManyDigitIn1(n:int) -> int:
    return len(str(n))
        
def hManyDigitIn2(n:int) -> int:
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

def fact(n:int) -> int:
    if n <= 0:
        return 1
    return n * fact(n-1)

def pascal_triangle(numRowes:int) -> list[list[int]]:
    res = [[1]]
    for i in range(numRowes-1):
        temp = [0] + res[-1] + [0]
        row = []
        for j in range(len(res[-1])+1):
            row.append(temp[j]+temp[j+1])
        res.append(row)
        
    for row in range(len(res)):
        for col in range(len(res)-row):
            print(' ',end='')
        print(res[row])
        
def scan_list(colums: int ,maxValue:int):
    lst = list()
    colm = int(input(f'how many colums max({maxValue}) ?'))
    while colm >= maxValue:
        colm = int(input(f'how many colums max({maxValue}) ?'))
        
    for col in range(colm):
        lst.append(int(input(f'\t> element({col}) :')))
    return lst

def flex_list(array: list[int] ,type:str):
    if type.lower() == 'print':
        for i in range(len(array)):
            print(array[i] , end=' ')
            
    if type.lower() == 'sum':
        sume = 0
        for i in range(len(array)):
            sume += array[i]
        print(sume)
        
    if type.lower() == 'multip':
        sume = 1
        for i in range(len(array)):
            sume *= array[i]
        print(sume)
        
    if type.lower() == 'div':
        sume = 0
        div = 0
        for i in range(len(array)):
            sume += array[i]
        for i in range(len(array)):
            div += array[i] / sume
        print(div)
        
    if type.lower() == 'average':
        sume = 0
        for i in range(len(array)):
            sume += array[i]
        print(sume/len(array))

def lenOfChar(char:str) -> int:
    if type(char) == list[str]:
        return len(char)
    
    lst = list()
    for i in char:
        lst.append(i)
    return len(lst)
# 65 -> 90 : Upper 
# 97 -> 122 : lower
#arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','u','r','s','t','w','x','y','z']
#for i in range(len(arr)):
#    print(ord(arr[i]),end=' ')
#print("\n")
def countWords(phrase:str):
    count = 1
    for i in range(lenOfChar(phrase)):
        if phrase[i-1] == ' ' and phrase[i] != ' ':
            count += 1
    if phrase[-1] == ' ':
        count-=1
    return count

class Character(str):
    def majuscule(self):
        upper = list(range(65,82)) +[85,82,83,84]+ list(range(87,91))
        lower = list(range(97,114)) + [117,114,115,116]+ list(range(119,123))
        arr = []
        for i in self:
            arr.append(ord(i))
         
        ch = ''  
        for c in range(len(arr)):
            arr[c] = chr(upper[lower.index(arr[c])])
            ch += arr[c]
        return ch
    
    def minuscule(self):
        upper = list(range(65,82)) +[85,82,83,84]+ list(range(87,91))
        lower = list(range(97,114)) + [117,114,115,116]+ list(range(119,123))
        arr = []
        for i in self:
            arr.append(ord(i))
            
        ch = ''  
        for c in range(len(arr)):
            arr[c] = chr(lower[upper.index(arr[c])])
            ch += arr[c]
        return ch
    
    def addsert(self , newChr:str ,position:int):
        if lenOfChar(newChr) > 1:
            return self
        
        self.newChr = newChr
        self.partition = position
        arr = []
        for i in self:
            arr.append(i)
            
        for index in range(len(arr)-1,position,-1):
            arr[index] = arr[index-1]
        arr[position] = newChr
        len(arr)+1
        
    def appendChr1(self,newChr:str):
        if lenOfChar(newChr) > 1:
            return self
        self.newChr = newChr
        arr = []
        for i in self:
            arr.append(i)
        arr.append(newChr)
        
    def appendChr2(self,newChr:str):
        if lenOfChar(newChr) > 1:
            return self
        self.newChr = newChr
        return self + newChr
    
    def reversChr(self):
        arr = []
        for i in self:
            arr.append(i)

        for index in range(lenOfChar(arr)//2):
            arr[index] ,arr[-index-1] = arr[-index-1],arr[index]
            
        ch = ''
        for i in range(lenOfChar(arr)):
            ch += arr[i]
        
        return ch
    

    #def equalStartWith(self)
  
    def spil_it2(self,spil:str):
        self.spil = spil
        arr = []
        arr.append(self[0:self.index(spil)])
        for i in range(countWords(self)):
            arr.append(self[self.index(spil)::])
        arr.append(self[self.index(spil)::])
        return arr
            
a = 'hello by world      bls bls     g' #-> ['hello','world'] 
 ## end spilit
def countWords1(sentenc:str):
    arr = []
    indexes = []
    word = ''
    for space in range(lenOfChar(sentenc)):
        if sentenc[space] == ' ':
            indexes.append(space)
            
    i = 0
    while sentenc[indexes[i]+2] != ' ':
        word += sentenc[indexes[i]-1] 
        i += 1
    arr.append(word)

    return arr
        
print(countWords1(a))
    


#a = 'hello by world'
#ch = Character(a)
#print(ch.spil_it(' '))
        


            
        