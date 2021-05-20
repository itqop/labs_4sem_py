class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)


    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

def revers():
    s = Stack()
    with open('text8.txt','r') as f:
        z = f.read()
        for i in range(len(z)):
            s.push(z[i])
    for i in range(s.size()):
        print(s.pop(), end='')

revers()