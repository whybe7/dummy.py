
def fillMatrix(Xrow:int, Xcol:int, type = str , ) -> list[list[str|int]]:
    matrix = []
    if type == str:
        for row in range(Xrow):
            matrix.append([])
            for col in range(Xcol):
                matrix[row].append(input(f'\t> value of {row,col}: '))
        return matrix
    if type == int:
        for row in range(Xrow):
            matrix.append([])
            for col in range(Xcol):
                matrix[row].append(int(input(f'\t> value of {row,col}: ')))
        return matrix
    
class squear:
    def __init__(self) -> None:
        isSquear = False
        for row in range(len(self)):
            if len(self[row]) != len(self):
                isSquear = True
        return isSquear
                
        
def changeDiagonal(matrix:squear, dir:int, by:int|str):
    if dir == -1:
        for col in range(len(matrix)):
            matrix[col][col] = by
        return matrix
    
    if dir == 0:
        for row in range(len(matrix)):
            for col in range(len(matrix)):
                matrix[row][(len(matrix[row])-1) // 2] = by
        return matrix
    
    if dir == 1:
        for row in range(len(matrix)):
            matrix[row][len(matrix[row])-1-row] = by
        return matrix
    
def checkMatrixs(matrixs, action='plus'):
    checked = True
    if action == 'plus':
        for matrix in range(len(matrixs)-1):
            for row in range(len(matrixs[matrix])):
                if len(matrixs[matrix]) == len(matrixs[matrix+1]):
                    if len(matrixs[matrix][row]) != len(matrixs[matrix+1][row]):
                        checked = False    
                else:
                    checked = False
        return checked
                
    if action == 'multiplication':
        for matrix in range(len(matrixs)-1):
            for row in range(len(matrixs[matrix])):
                if len(matrixs[matrix][row]) != len(matrixs[matrix+1]):
                    checked = False
        return checked
            
        
def matrixSum(matrix1:list[list[int]], matrix2:list[list[int]]):
    sumMatrix = []
    if checkMatrixs((matrix1, matrix2)):
        for row in range(len(matrix1)):
            sumMatrix.append([])
            for col in range(len(matrix2[0])):
                sumMatrix[row].append(matrix1[row][col] + matrix2[row][col])
        return sumMatrix

def matrixProduct(matrix1:list[list[int]], matrix2:list[list[int]]):
    prodMatrix = []
    if checkMatrixs((matrix1, matrix2), action='multiplication'):
        for row in range(len(matrix1)):
            prodMatrix.append([])
            for col in range(len(matrix2[0])):
                prodMatrix[row].append(0)
                for k  in range(len(matrix2)):
                    prodMatrix[row][col] += matrix1[row][k] * matrix2[k][col]
    return prodMatrix

def isSquear(squear:list[list[int]]):
    check = True
    for row in range(len(squear)):
        if len(squear[row]) != len(squear):
            check = False
    return check

def isMagicSquear(squear:list[list[int]]):
    result  = []
    Yes = True
    No = False
    if isSquear(squear):
         # rows ___
        for row in range(len(squear)):
            sume = 0
            for col in range(len(squear[0])):
                sume += squear[row][col]
            result.append(sume)
        
        # col |
        for row in range(len(squear)):
            sume = 0
            for col in range(len(squear[0])):
                sume += squear[col][row]
            result.append(sume)
            
        # diagonal \
        sume = 0
        for same in range(len(squear)):
            sume += squear[same][same]
        result.append(sume)
            
        # anti diagonal /
        sume = 0
        for revers in range(len(squear)):
            sume += squear[revers][len(squear)- revers -1]
        result.append(sume)
            
        magicValue = result[0]
        for value in range(len(result)):
            if result[value] != magicValue:
                return No
        return Yes
        

                     
        
                  
      
              
                
            
            

# print('--------------Matrix 1---------')
# matrix1 = fillMatrix(2, 2, type=int)
# print('--------------Matrix 2---------')
# matrix2 = fillMatrix(2, 2, type=int)
# print('--------------Matrix 3---------')
# matrix3 = fillMatrix(2, 2, type=int)

matrix1 = [[12,7,3],
           [4,5,6],
           [7,8,9]]

matrix2 = [[5,8,1,2],
           [6,7,3,0],
           [4,5,9,1]]

matrix3 = [[2, 2, 2],
           [2, 2, 2], #n x m = 2 x 3
           [2, 2, 2]] #n x m = 2 x 3

matrix4 = [[2, 2, 2],
           [2, 2, 2],
           [2, 2, 2]] #m x p  = 3 x 2


A = [[1, 7, 3],
     [3, 5, 6],
     [6, 8, 9]]

B = [[1, 1, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

magicsquear = [[2, 7, 6],
               [9, 5, 1],
               [4, 3, 8]]





