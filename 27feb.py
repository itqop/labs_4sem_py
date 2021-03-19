"""             ZADANIE 1               """


def plus(Arg, int):
    global addX
    addX = Arg + int


def searchGolos(arr, part):
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] == 0:
            continue
        elif arr[i][0] == 'Add' and arr[i][1] == part:
            return i
    return -1


def n1():
    global addX
    k = int(input())
    Input = list(list(map(str, input().split())) for o in range(k))
    tree = [0 for i in range(k)]
    addX = 0
    Ans = True
    for i in range(k):
        Action = Input[i]
        if Action[0] == 'Add':
            tree[addX] = Action
            plus(addX, 1) if tree[1] == 0 else plus(addX, 2)

        if Action[0] == 'Vote':
            if Input[i - 1][0] == 'Add' and Input[i - 1][1] != Action[1]:
                Ans = False
                break
            Golos = searchGolos(tree, Action[1])

            if Golos == len(tree) - 3 or Golos == 0:
                tree[Golos + 2] = Action
            elif Golos == -1:
                Ans = False
                break
            else:
                tree[Golos + 3] = Action
    print('Yes') if Ans else print('No')
    print(tree)


"""             ZADANIE 2               """


def n2():
    N = int(input())
    i = 3
    while N % i != 0:
        i += 1
    print(i)


"""             ZADANIE 3               """


def isSost(n):
    if n % 2 == 0:
        return [not (n == 2), 2]
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return [not (d * d > n), d]


def Transfer(number, sys):
    l = len(number)
    number10 = 0
    for i in range(l):
        number10 += int(number[i]) * pow(sys, l - 1 - i)
    return number10


def n3():
    N = input()
    Space = False
    maX = max(list(map(int, N)))
    B = maX if maX > 1 else 2
    while not Space and B < 1000000000:
        B += 1
        Trans = Transfer(N, B)
        inf = isSost(Trans)
        Space = inf[0]
        X = inf[1]
    print(B, X)


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
