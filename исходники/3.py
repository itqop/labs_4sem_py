def insertion_sort3(A):
    for i in range(1, len(A)):
        curNum = A[i]
        k = 0
        for j in range(i - 1, -2, -1):
            k = j
            if A[j] > curNum:
                A[j + 1] = A[j]
            else:
                break
        A[k + 1] = curNum

def selection_sort(A):
    for i in range(0, len(A) - 1):
        minIndex = i
        for j in range(i + 1, len(A)):
            if A[j] < A[minIndex]:
                minIndex = j
        if minIndex != i:
            A[i], A[minIndex] = A[minIndex], A[i]


def bubble_sort2(A):
    for i in range(0, len(A) - 1):
        done = True
        for j in range(0, len(A) - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                done = False
        if done:
            return

def merge_sort(A):
    merge_sort2(A, 0, len(A) - 1)

threshold = 20
def merge_sort2(A, first, last):
    if last - first < threshold and first < last:
        quick_selection(A, first, last)
    elif first < last:
        middle = (first + last) // 2
        merge_sort2(A, first, middle)
        merge_sort2(A, middle + 1, last)
        merge(A, first, middle, last)


def merge(A, first, middle, last):
    L = A[first:middle]
    R = A[middle:last + 1]
    L.append(999999999)
    R.append(999999999)
    i = j = 0

    for k in range(first, last + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
