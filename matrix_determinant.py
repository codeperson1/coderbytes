def IsSquareMatrix(m):
    size = len(m)
    i = 0
    result = True
    while(i<size and result):
        if(len(m[i]) != size):
            result = False
        i += 1
    return result

def CreateMatrix(rows, cols):
    m = []
    for i in range(0, rows):
        r = []
        for j in range(0, cols):
            r.append(0)
        m.append(r)
    return m

def GetMatrixSize(m):
    size = [len(m), len(m[0])]
    return size

def DeleteRowCol(m, row, col):
    size = GetMatrixSize(m)
    nm = CreateMatrix(size[0]-1, size[1]-1)
    for i in range(0, size[0]-1):
        for j in range(0, size[1]-1):
            r = i
            if(r >= row):
                r += 1
            c = j
            if(c >= col):
                c += 1
            nm[i][j] = m[r][c]
    return nm

def CalculateDeterminant(m):
    if(IsSquareMatrix(m)):
        size = GetMatrixSize(m)
        if(size[0] == 2):
            det = m[0][0]*m[1][1] - m[0][1]*m[1][0]
        else:
            det = 0
            for r in range(0, size[0]):
                m2 = DeleteRowCol(m, r, 0)
                sign = 1 - 2*(r%2)
                det += sign * m[r][0] * CalculateDeterminant(m2)
    else:
        det = -1
    return det

def IsNumber(s):
    valid = True
    if(len(s) < 1):
        valid = False
    index = 0
    if(valid):
        if(s[0] == '+' or s[0] == '-'):
            if(len(s) < 2):
                valid = False
            else:
                index += 1
    if(valid):
        while(index<len(s) and valid):
            if(s[0]>='0' and s[0]<='9'):
                index += 1
            else:
                valid = False
    return valid

def ParseMatrixArray(strArr):
    m = []
    row = []
    index = 0
    while(index < len(strArr)):
        if(strArr[index] == "<>"):
            m.append(row)
            row = []
        else:
            row.append(int(strArr[index]))
        index += 1
    m.append(row)
    return m

def MatrixDeterminant(strArr): 
  # code goes here
  m = ParseMatrixArray(strArr)
  det = CalculateDeterminant(m)
  return det

# keep this function call here  
# to see how to enter arguments in Python scroll down
print(MatrixDeterminant(raw_input()))
