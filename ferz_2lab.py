
X1 = [
    [0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0]
]
W = [[1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0]]

def Valid(matrix):
    n = len(matrix)
    T = False
    #Check rows
    for i in matrix:
        if sum(i) >1:break
    else:
        T = True
    if not T:
        return T
    else:
        T = False
    #Check cols
    for i in range(n):
        if sum(matrix[j][i] for j in range(n))>1:break
    else:
        T = True
    if not T:
        return T
    else:
        T = False
    #Check first diagonal
    for j in range(n-2,0,-1):
        if sum(matrix[i][i-j] for i in range(j,n))>1:break
    else:
        T = True
    if not T:
        return T
    else:
        T = False
    for j in range(n-1):
        if sum(matrix[i-j][i] for i in range(j,n))>1:break
    else:
        T = True
    if not T:
        return T
    else:
        T = False
    #Check second diagonal
    for j in range(2,n):
        if sum(matrix[i][j-1-i] for i in range(j))>1:break
    else:
        T = True
    if not T:
        return T
    else:
        T = False
    for j in range(0,n-1):
        if sum(matrix[i][j-1-i] for i in range(j,n))>1:break
    else:
        T = True
    return T
def Print(matrix):
    for i in matrix:
        print(i)
    print("-------------------------------------------------")
def Right(x):
    i = x.index(1)
    x[i], x[i+1] = x[i+1], x[i]
    return x

def BruteForce(matrix):
    n = len(matrix)
    o = 1
    for part1 in range(n):
        u1 = matrix[1].copy()
        for part2 in range(n):
            u2 = matrix[2].copy()
            for part3 in range(n):
                u3 = matrix[3].copy()
                for part4 in range(n):
                    u4 = matrix[4].copy()
                    for part5 in range(n):
                        u5 = matrix[5].copy()
                        for part6 in range(n):
                            u6 = matrix[6].copy()
                            for part7 in range(n):
                                u7 = matrix[7].copy()
                                if Valid(matrix): Print(matrix)
                                #print(matrix, o)
                                for part8 in range(n - 1):
                                    matrix[7] = Right(matrix[7])
                                    if Valid(matrix): Print(matrix)
                                    #print(matrix, o)
                                matrix[7] = u7
                                if part7 != n - 1:
                                    matrix[6] = Right(matrix[6])
                            matrix[6] = u6
                            if part6 != n - 1:
                                matrix[5] = Right(matrix[5])
                        matrix[5] = u5
                        if part5 != n - 1:
                            matrix[4] = Right(matrix[4])
                    matrix[4] = u4
                    if part4 != n - 1:
                        matrix[3] = Right(matrix[3])
                matrix[3] = u3
                if part3 != n - 1:
                    matrix[2] = Right(matrix[2])
            matrix[2] = u2
            if part2 != n - 1:
                matrix[1] = Right(matrix[1])
        matrix[1] = u1
        if part1 != n-1:
            matrix[0] = Right(matrix[0])

#print(Valid(W))
X = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0]
]
BruteForce(X)