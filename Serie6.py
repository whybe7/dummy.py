
def fill_matrix(rows:int , coloms:int):
    matrix = []
    if rows != 50 and coloms != 50:
        for row in range(rows):
            matrix.append([])
            for col in range(coloms):
                matrix[row].append(int(input(f"\t>Matrix element {row,col}: ")))
    return matrix

def Change_diag(matrix:list[list[int]],direc:int,by:int):
    der = [-1,0,1]
    if direc not in der:
        return matrix
    if len(matrix) != len(matrix[0]):
        return matrix
    for chek in range(len(matrix)):
        if type(matrix[chek]) != list :
            return matrix    
               
    if direc == der[0]:
        for step in range(len(matrix)):
            matrix[step][step] = by
            
    elif direc == der[1]:
        if len(matrix[0]) % 2 != 0:
            mid = (len(matrix[0])-1)//2
            for step in range(len(matrix)):
                matrix[step][mid] = by
                
    elif direc == der[-1]:
        loc = len(matrix) - 1
        for step in range(len(matrix)):
            matrix[step][loc] = by
            loc -= 1      
    return matrix

def trans_matrix(matrix:list[list[int]]):
    new_matrix = []
    for check in range(len(matrix)):
        if type(matrix[check]) != list:
            return matrix
    for row in range(len(matrix)):
        new_matrix.append([])
        for col in range(len(matrix)):
            new_matrix[row].append(matrix[col][row])
    return new_matrix     

def add_matrix(matrix1:list[list[int]],matrix2:list[list[int]]):
    new_matrix = []
    if len(matrix1) == len(matrix2): 
        lenght = len(matrix1)
    else:
        return 
    for check in range(lenght):
        if type(matrix1[check]) != list or type(matrix2[check]) != list:
            return 
    for row in range(lenght):
        new_matrix.append([])
        for col in range(lenght):
            new_matrix[row].append((matrix1[row][col])+(matrix2[row][col]))
    return new_matrix

def sum_matrix(matrix: list[list[int]]):
    sume = 0
    for row in range(len(matrix)):
        for col in range(len(matrix)):
            sume += matrix[row][col]
    return sume

def product_matrix(matrix1:list[list[int]],matrix2:list[list[int]]):
    new_matrix = []
    if len(matrix1[0]) != len(matrix2):
        return   
    for check in range(len(matrix1)):
        if type(matrix1[check]) != list or type(matrix2[check]) != list:
            return
        
    for row in range(len(matrix1)):
        new_matrix.append([])
        for col in range(len(matrix2)):
            for k in range(len(matrix1)):
                new_matrix[row].append((matrix1[row][k])+(matrix2[k][col]))
    return new_matrix

def mid_point(matrix:list[list[int]]):
    if len(matrix[0]) != len(matrix):
        return matrix
    for check in range(len(matrix)):
        if type(matrix[check]) != list:
            return matrix
    if len(matrix[0]) % 2 != 0:
        mid = (len(matrix[0])-1)//2
        for row in range(len(matrix)):
            if row == mid :
                dic = {matrix[row][mid]:(row,mid)}
                return dic
    return matrix

def point_col(matrix:list[list[int]]):
    for check in range(len(matrix)):
        if type(matrix[check]) != list:
            return matrix
    
    for row in range(len(matrix)):
        mx = matrix[row][0]
        for col in range(len(matrix)):
            if matrix[row][col] > mx:
                mx = matrix[row][col]
                
        mn = matrix[0][col]
        for coln in range(len(matrix)):
            if matrix[coln][col] < mn:
                mn = matrix[coln][col]
        return (mx,mn)

def matrix_row_sum(rows:int , coloms:int):
    matrix = []
    sume = 0
    if rows != 50 and coloms != 50:
        for row in range(rows):
            matrix.append([])
            for col in range(coloms):
                matrix[row].append(int(input(f"> matrix element index {row,col}: ")))
                sume += matrix[row][col]
                if len(matrix[row]) == coloms: 
                    print(f'the sum of row {row} is :{sume}')
                    sume = 0
    return matrix

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
        
        #diagonal \:
        sum = 0
        for same in range(len(squear)):
            sum += squear[same][same]
        total.append(sum)

        #diagonal /:
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
        
def convert(matrix:list[list[int]]):
    new_matrix = []
    for check in range(len(matrix)):
        if matrix[check] != list:
            return matrix
    for row in matrix:
        for col in row:
            new_matrix.append(col)
    return new_matrix

def pascal_traiangle(numRows:int) -> list[list[int]] :
    result = [[1]]
    for i in range(numRows - 1):
        temp = [0] + result[-1] + [0]
        row = []
        for index in range(len(result[-1])+1):
            row.append(temp[index] + temp[index+1])
        result.append(row)
    return result

def piramid(num:int, b:int ,c:int) -> list[list[int]]:
    [[1], [2, 1, 2],[(2+1+2)+(3)]]
    result = [[num]]
    for row in range(len(result[-1])):
        sume = 0
        for col in range(len(result[-1])):
            sume += result[-1][col]
        temp = [len(result[-1])+sume] + result[-1] + [len(result[-1])+sume]
        result.append(temp)
            
    return result


def fill_magic_squear(lenght:int):
    from random import randint
    from math import pow
    if lenght > 5 :
        return
    matrix = []
    for row in range(lenght):
        matrix.append([])
        sum = 0
        for col in range(lenght):
            choice = randint(1,pow(lenght,lenght))
            f= True
            while f and sum != 15:
                if matrix[col-1] != matrix[col]:
                    matrix[row].append(choice)
                    sum += choice
                else:
                    matrix[row].clear()
                    sum = 0
            sum = 0      
            f = True
       

#while sum != 3:
#    l.clear()
#    for i in range(3):
#        l.append(randint(1,9))
#    for j in range(len(l)):
#        sum += l[j]
            
            
            

[    [1],
   [2,1,2],
 [8,2,1,2,8]]
lst1 = [[2,2,2,2,2],
        [2,2,2,2,2],
        [2,2,2,2,2],
        [2,2,2,2,2],
        [2,2,2,2,2]]

lst2 = [[5,2,3],
        [-7,8,9],
        [-6,-3,-4]]

print(piramid(1,1,2))


    







