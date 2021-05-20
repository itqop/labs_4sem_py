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


def transfer():

    sizeT = a.size()

    while a.size() != 1:
        point = a.pop()
        b.push(point)

    while c.size() != sizeT:
            if a.size() == 1:
                point = a.pop()
                c.push(point)
            if b.size() > 0:
                point = b.pop()
                c.push(point)
    while b.size() != c.size()-1:
        b.push(" ")
    while a.size() != c.size()-1:
        a.push(" ")

    return c.items
if __name__ == "__main__":
    a = Stack()
    b = Stack()
    c = Stack()
    with open('text3.txt','r') as f:
        z = f.read()
        for i in range(len(z)):
            if z[i].isdigit():
                a.push(z[i])
    print(a.items, " - пирамидка А до перемещений")
    print(transfer(), " - пирамидка С после перемещений")

    with open('text3.txt','w') as f:

        f.write("\n" + 'a = ')
        for i in range(a.size()):
            f.write(a.items[i])

        f.write("\n" + 'b = ')
        for i in range(b.size()):
            f.write(b.items[i])

        f.write("\n"+'c = ')
        for i in range(c.size()):
            f.write(c.items[i])
