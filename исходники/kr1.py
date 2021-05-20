"""             ZADANIE 1               """

def n1():
    A = list(map(int, input().split(" ")))
    A.sort(reverse=True)
    for i in range(len(A) - 2):
        if A[i] < A[i + 1] + A[i + 2]:
            print(A[i]+ A[i + 1]+ A[i + 2])
            break
    else:
        print(-1)


"""             ZADANIE 2               """


def sort_f(array):
    for i in range(0, len(array) - 1):
        minIndex = i
        for j in range(i + 1, len(array)):
            if cmp(array[j], array[minIndex]):
                minIndex = j
        if minIndex != i:
            array[i], array[minIndex] = array[minIndex], array[i]
    return array


def cmp(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return True if ab > ba else False


def re_sort(array, arg):
    agr1 = arg
    while array[arg] == array[arg + 1]:
        arg += 1


def n2():
    nums = list(map(str, input().split()))
    nums = sort_f(nums)
    print(''.join(nums))


"""             ZADANIE 3               """


def n3():
    matrix1 = [[11, 25, 66, 1, 69, 7],
              [23, 55, 17, 45, 15, 52],
              [75, 31, 36, 44, 58, 8],
              [22, 27, 33, 25, 68, 4],
              [84, 28, 14, 11, 5, 50]
              ]

    m2 = [[3, 3, 1, 1],
              [2, 2, 1, 2],
              [1, 1, 1, 2]]

    n = len(matrix1)
    m = len(matrix1[0])
    matrix = []
    for i in range(n):
        for j in range(m):
            matrix.append(matrix1[i][j])
    o = m+n-3
    for i in range(m-1):
        temp = []
        col = i+2 if i+2 <= n else n
        f = m - 2 - i
        temp_f = f
        for j in range(col):
            temp.append(matrix[f])
            f += o
        temp.sort()
        f = temp_f
        for j in range(col):
            matrix[f] = temp[j]
    for i in range(1,n-1):
        temp = []
        col = n-1-i
        f = m * i
        temp_f = f
        for j in range(col):
            temp.append(matrix[f])
            f += o
        temp.sort()
        f = temp_f
        for j in range(col):
            matrix[f] = temp[j]
            f += o
    for i in range(n * m):
        if i % m == 0:
            print('\n')
        print(matrix[i], end=' ')


"""             START                   """

s = input("Введите номер задачи - ")
if s == '1':
    n1()
elif s == '2':
    n2()
elif s == '3':
    n3()
else:
    print("Хозяяиин, не та-ааак многоо ^_^ ")
