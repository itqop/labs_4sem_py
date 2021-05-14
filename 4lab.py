import re


class Deque:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def push_front(self, item):
        self.items.append(item)

    def push_back(self, item):
        self.items.insert(0, item)

    def pop_front(self):
        return self.items.pop()

    def pop_back(self):
        return self.items.pop(0)

    def peek_first(self):
        return self.items[0]

    def peek_last(self):
        return self.items[-1]


class Stack(Deque):
    def push(self, item):
        super().push_front(item)

    def pop(self):
        return super().pop_front()

    def peek(self):
        return self.items[-1] if not self.is_empty() else "87654324567890"


def first_task():
    deque_input = Deque()
    deque_sorted = Deque()
    with open("text.txt", "r", encoding="utf8") as file:
        books_str = file.readlines()
        for i in books_str:
            deque_input.push_front(i)

    print("Сортировка книг в алфавитном порядке:")
    while not deque_input.is_empty():
        if deque_sorted.is_empty():
            deque_sorted.push_front(deque_input.pop_front())
        if deque_input.peek_last() >= deque_sorted.peek_last():
            deque_sorted.push_front(deque_input.pop_front())
        else:
            deque_input.push_back(deque_sorted.pop_front())
    i = 1
    while not deque_sorted.is_empty():
        print(str(i) + "): " + deque_sorted.pop_back(), end='')
        i += 1


def generation_alp(alf):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(25):
        alf.push_front(alph[i])
    alf.pop_front()
    return alf


def second_task():
    s = Deque()
    alf = Deque()
    decrp = Deque()
    t = ''
    alf = generation_alp(alf)
    with open('input.txt', "r", encoding='utf8') as f:
        z = f.read()
        for i in range(len(z)):
            s.push_front(z[i].lower())
        s.push_front('#')
    start_size = len(s)-1
    while len(decrp) != start_size:
        a = s.pop_back()
        check = True
        if a.isalpha():
            while check:
                if a == 'y':
                    a = alf.items[0]
                    decrp.push_front(a)
                    break
                elif a == 'z':
                    alf.pop_back()
                    a = alf.items[0]
                    decrp.push_front(a)
                    alf = generation_alp(alf)
                    break
                elif a == alf.pop_back():
                        alf.pop_back()
                        a = alf.items[0]
                        decrp.push_front(a)
                        alf.items.clear()
                        alf = generation_alp(alf)
                        break
        else:
            decrp.push_front(a)

    for i in range(len(decrp)):
        t += decrp.pop_back()
    return t


def postfix(temp):
    exp = ""
    for i in temp:
        if i == "A":
            exp += "*"
        elif i == "X":
            exp += "^"
        elif i == "O":
            exp += "+"
        elif i == "N":
            exp += "!"
        else:
            exp += i + ""
    temp = ""
    stack = Stack()
    print(exp)
    for i in exp:
        # print(stack.seen())
        if i in "TF":
            temp += i + " "
            continue
        if (i in "+") and (stack.peek() in "*!^"):
            ch = stack.pop()
            while ch != "(":
                temp += ch + ' '
                ch = stack.pop()
            stack.push("(")
        if i == ")":
            ch = stack.pop()
            while ch != "(":
                temp += ch + ' '
                ch = stack.pop()

            continue
        stack.push(i)
    while not stack.is_empty():
        temp += stack.pop() + " "
    print(temp)
    return temp


def nine_task(expr):
    operators = {
        '+': bool.__or__,
        '*': bool.__and__,
        '^': bool.__xor__,
    }
    expr = str(postfix(expr).strip())
    ops = operators.keys()
    res = Stack()
    # ((N(TAF))OFATOF)
    # TO(FANTOT)AT
    for atom in re.split(r"\s+", expr):
        try:
            if atom == "F":
                atom = False
            elif atom == "T":
                atom = True
            elif atom == "!":
                res.push_front(not res.pop())
                continue
            else:
                raise ValueError
            res.push_front(atom)
        except ValueError:
            for oper in atom:
                if oper not in ops:
                    continue
                oper2 = res.pop()
                oper1 = res.pop()
                oper = operators[oper](oper1, oper2)
                res.push_front(oper)

    return res.pop()


def ten_task(expr):
    # M(M(3,9),N(N(89,1),0))
    res = Stack()
    e = ""
    for i in expr:
        res.push(i)
        if i == ')':
            ch = res.pop()
            n1 = ""
            n2 = ""
            F = True
            while ch != '(':
                while ch != ',' and F:
                    # print(res.peek()+ "---- n1")
                    ch = res.pop()
                    n1 += ch if ch != ',' else ""
                F = False
                # print(res.peek()+"-------- n2")
                ch = res.pop()
                n2 += ch if ch != '(' else ""
            n1, n2 = int(n1[::-1]), int(n2[::-1])
            # print(n1, n2, "------__---")
            if res.pop() == 'M':
                res.push(str(max(n1, n2)))
            else:
                res.push(str(min(n1, n2)))
    return res.pop()
    # print(res.items)


def temp11(exp):
    temp = ""
    stack = Stack()
    for i in exp:
        # print(stack.items)
        if i in "xyz":
            temp += i + " "
            continue
        if i == ")":
            ch = stack.pop()
            while ch != "(":
                temp += ch + ' '
                ch = stack.pop()
            continue
        stack.push(i)
    while not stack.is_empty():
        temp += stack.pop() + " "
    print(temp)
    return temp


def el_task(expr):
    expr = str(temp11(expr).strip())
    operator = {'+': int.__add__}
    ops = operator.keys()
    res = Stack()
    lst = list(expr)
    for atom in re.split(r"\s+", expr):
        try:
            assert atom in "xyz+ "
            if atom in "xyz":
                atom = 1
            else:
                raise ValueError
            res.push_front(atom)
        except ValueError:
            for oper in atom:
                if oper not in ops:
                    return False
                oper2 = res.pop()
                oper1 = res.pop()
                oper = operator[oper](oper1, oper2)
                res.push_front(oper)
        except AssertionError:
            return False

    return res.pop() and True


if __name__ == "__main__":
    num = int(input("Введите номер задания\n"))
    if num == 1:
        first_task()
    elif num == 2:
        print(second_task())
    elif num == 3:
        print()
    elif num == 4:
        print()
    elif num == 5:
        print()
    elif num == 6:
        print()
    elif num == 7:
        print()
    elif num == 8:
        print()
    elif num == 9:
        print(nine_task(input("Введите логическое выражение:\n")))
    elif num == 10:
        print(ten_task(input("Введите выражение:\n")))
    elif num == 11:
        print(el_task(input("Введите выражение:\n")))
