class stack:
    def __init__(self):
        self.items = []

    def __len__(self):
        return self.size()

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class deque:
    def __init__(self):
        self.__items = []

    def __len__(self):
        return self.size()

    def is_empty(self):
        return self.__items == []

    def push_front(self, item):
        self.__items.append(item)

    def push_back(self, item):
        self.__items.insert(0, item)

    def pop_front(self):
        return self.__items.pop()

    def pop_back(self):
        return self.__items.pop(0)

    def size(self):
        return len(self.__items)

    def sort(self, comparsion_function=lambda lhs, rhs: lhs > rhs):
        for l in range(1, len(self.__items)):
            item_to_insert = self.__items[l]
            j = l - 1
            while j >= 0 and comparsion_function(self.__items[j], item_to_insert):
                self.__items[j + 1] = self.__items[j]
                j -= 1
            self.__items[j + 1] = item_to_insert