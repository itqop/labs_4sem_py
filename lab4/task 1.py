import random
from lab4.containers import deque


if __name__ == "__main__":
    #Int deque
    deque_ = deque()
    for i in range(10):
        deque_.push_back(random.randint(1, 100))

    deque_.sort()

    deque_ = deque()
    with open("text.txt", "r", encoding="utf8") as file:
        books_str = file.readlines()
        for i in range(len(books_str)):
            deque_.push_back(books_str[i])

    print("\nSorting string deque:")

    deque_.sort(lambda lhs, rhs: lhs[0] > rhs[0])
    for i in range(deque_.size()):
        print(str(i + 1) + "): " + deque_.pop_back() + '\n')