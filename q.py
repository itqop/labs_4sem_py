import time
import random
m = 10
n = 10
min_limit = -250
max_limit = 1007
x = [[random.randint(int(min_limit),int(max_limit) ) for a in range(int(m))] for k in range(int(n))]
def selection_sort(j):
    for A in j:
        for i in range(len(A)):
            A[A[i:].index(min(A[i:])) + i],A[i] = A[i], min(A[i:])
    return j

def insertion_sort(a):
    for A in a:
        for i in range(1,len(A)):
            q=A[i]
            j=i-1
            while(j>=0 and A[j]>q):
                A[j + 1] = A[j]
                j=j-1
            A[j+1]=q
    return(a)

def bubble_sort(a):
    for A in a:
        for i in range(len(A)-1):
            c = 0
            for j in range(len(A)-1-i):
                if (A[j]>A[j+1]):
                    c+=1
                    A[j],A[j+1] = A[j+1],A[j]
            if c == 0:
                break
    return a


def shell(a):
    for A in a:
        d = len(A) // 2
        while d:
            for i, el in enumerate(A[d:], d):
                while i >= d and A[i - d] > el:
                    A[i] = A[i - d]
                    i -= d
                A[i] = el
            d //= 2
    return a
def tour(a):
    for A in a:
        print()

def quick(a):
    i = 0
    for A in a:
        a[i] = qsort(A)
        i+=1
    return a
def qsort(array):
    if len(array) <=1:
        return array
    *unsort, Z = array
    low = qsort([i for i in unsort if i < Z])
    high = qsort([i for i in unsort if i >= Z])
    return low + [Z] + high

def maxHeap(a, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and a[i] < a[l]:
        largest = l
    if r < n and a[largest] < a[r]:
        largest = r
    if largest != i:
        a[i],a[largest] = a[largest],a[i]
        maxHeap(a, n, largest)
def heap(a):
    for A in a:
        for i in range(len(A), -1, -1):
            maxHeap(A, len(A), i)
        for i in range(len(A) - 1, 0, -1):
            A[i], A[0] = A[0], A[i]
            maxHeap(A, i, 0)
    return a
strTime = time.time()
print(heap(x))
print(round(time.time()-strTime,11))































"""
m = 100
n = 100
min_limit = -250
max_limit = 1007
x = [[random.randint(int(min_limit),int(max_limit) ) for a in range(int(m))] for k in range(int(n))]
def shellS(a):
    for A in a:
        d = len(A) // 2
        while d:
            for i, el in enumerate(A[d:], d):
                while i >= d and A[i - d] > el:
                    A[i] = A[i - d]
                    i -= d
                A[i] = el
            d //= 2
            #d = 1 if d == 2 else d * 5 // 11
    return a
x1 = x.copy()
strTime = time.time()
print(shellS(x))
print(round(time.time()-strTime,11))
strTime = time.time()
print(shellS(x1))
print(round(time.time()-strTime,11))
"""