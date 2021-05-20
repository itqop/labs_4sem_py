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



def generationAlp():
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(25):
        alf.addFront(alph[i])
    alf.removeFront()

def decryption():
    t = ''
    generationAlp()
    with open('text2.txt', "r") as f:
        z = f.read()
        for i in range(len(z)):
            s.addFront(z[i].lower())
        s.addFront('#')
    startSize = s.size()-1
    while decrp.size() != startSize:
        a = s.removeRear()
        check = True
        if a.isalpha():
            while check == True:
                if a == 'y':
                    a = alf.items[0]
                    decrp.addFront(a)
                    break
                elif a == 'z':
                    alf.removeRear()
                    a = alf.items[0]
                    decrp.addFront(a)
                    generationAlp()
                    break
                elif a == alf.removeRear():
                        alf.removeRear()
                        a = alf.items[0]
                        decrp.addFront(a)
                        alf.items.clear()
                        generationAlp()
                        break
        else:
            decrp.addFront(a)

    for i in range(decrp.size()):
        t += decrp.removeRear()
    return t

if __name__ == "__main__":
    s = Deque()
    alf = Deque()
    decrp = Deque()
    print(decryption())

