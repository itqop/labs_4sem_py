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
class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def check():
    k = 0

    with open("code.txt", "r") as f:
        z = f.read()
        for i in range(len(z)):
            s.push(z[i])
    while len(s.items) != 0:
        a = s.pop()
        if a == ")" or a == "(":
            k+=1
    if k % 2 == 0:
        k = "четное кол-во"
    else:
        k = "нечетное кол-во"
    return k

def check2():
    k = 0
    s2 = Deque()
    with open("code.txt", "r") as f:
        z = f.read()
        for i in range(len(z)):
            s2.addFront(z[i])
    while len(s.items) != 0:
        a = s2.removeRear()
        if a == "}" or a == "{":
            k+=1

    if k % 2 == 0:
        k = "четное кол-во"
    else:
        k = "нечетное кол-во"
    return k

if __name__ == "__main__":
    s = Stack()
    s2 = Deque()
    print(check() + " - ()")
    print(check2() + " - {}")
