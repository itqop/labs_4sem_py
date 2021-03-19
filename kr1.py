"""             ZADANIE 1               """


def n1():
    A = list(map(int, input().split(" ")))
    A.sort(reverse=True)
    for i in range(len(A) - 2):
        if A[i] < A[i + 1] + A[i + 2]:
            print(sum(A[i], A[i + 1], A[i + 2]))
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
              ]
    matrix = [[3, 3, 1, 1],
              [2, 2, 1, 2],
              [1, 1, 1, 2]]

    n = len(matrix1)
    m = len(matrix1[0])
    matrix_s = []

    for j in range(n - 1, 0, -1):
        matrix_s.append(sorted(list(matrix1[i][i - j] for i in range(j, n))))
    for j in range(m //2):
        matrix_s.append(sorted(list(matrix1[i][i+j] for i in range(n))))
    for j in range(0, n - 1):
        matrix_s.append(sorted(list(matrix1[i-m//2-j][i] for i in range(m//2+j, m))))



    print(matrix_s)


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
