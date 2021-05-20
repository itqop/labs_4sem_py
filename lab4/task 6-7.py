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

def sort_symb():
    s = Stack()
    result = ''
    alp = Stack()
    num = Stack()
    b = Stack()

    with open("text6.txt", "r") as f:
        z = f.read()
        for i in range(len(z)):
            s.push(z[i])

    while len(s.items) > 0:
        a = s.pop()

        if a.isdigit():
            num.push(a)

        elif a.isalpha():
            alp.push(a)

        elif a != "\n" and a != " ":
            b.push(a)

    for i in range(num.size()):
        result += num.pop()

    for i in range(alp.size()):
        result +=alp.pop()

    for i in range(b.size()):
        result += b.pop()
    return result


def search():


    result = ""
    result2 = ""

    with open("text7.txt", "r") as f:
        z = f.read()
        for i in range(len(z)):
            s.addFront(z[i])
    check = False
    while len(s.items) > 0:
        a = s.removeRear()
        if a == "-":
            check = True
        if check == True:
            numnm.addFront(a)
            if a == " ":
                check = False
                numpl.addFront(a)
        else:
            numpl.addFront(a)

    for i in range(numpl.size()):
        result += numpl.removeRear()

    for i in range(numnm.size()):
        result2 += numnm.removeRear()
    m = "Plus " + result + " and minus " + result2
    return m

if __name__ == "__main__":
    s = Deque()
    numpl = Deque()
    numnm = Deque()
    print("6 задание - " + sort_symb())
    print("7 задание - " + search())
