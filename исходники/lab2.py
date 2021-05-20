import random
import time
import timeit

def binary_search(l, value):
    low = 0
    high = len(l)-1
    while low + 1 < high:
        mid = low + int(((float(high - low)/( l[high] - l[low])) * ( value - l[low])))
        if l[mid] > value:
            high = mid
        elif l[mid] < value:
            low = mid
        else:
            return mid
    return high if abs(l[high] - value) < abs(l[low] - value) else low
def fibonacci(n, a = [1, 1]):
    return (fibonacci(n, a + [sum(a[-2:])]) if len(a) < n else a[:n])
fibon = fibonacci(50)
def fibonacci_search(array,n,index = 0):
    i = 0
    while array[fibon[i]] <= n:
        if (array[fibon[i]] == n):
            index += fibon[i]
            return index
        if fibon[i+1] >= len(array):
            index += fibon[i]
            return fibonacci_search(array[fibon[i]:], n, index)

        i+=1
    index += fibon[i-1]
    return fibonacci_search(array[fibon[i-1]:fibon[i]],n,index)

m = 100
min_limit = -250000
max_limit = 200000
x = [random.randint(int(min_limit),int(max_limit) ) for a in range(int(m))]
"""
x.append(10)
x.sort()
print(x)
template = '{:.' + str(30) + 'f}'
o = x.copy()
strTime = time.time()
print(binary_search(o,10))
print(template.format(time.time()-strTime))
print(x.index(10))
print(fibonacci_search(x,10))"""


class node:
    # Инициализация узла. Значения левого ребенка, правого ребенка и родителя изначально заданы None, т.к. их может не быть вовсе.
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None


class binary_search_tree:
    # Инициализация бинарного дерева. Корня изначально нет.
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Если корня нет - создать новый корень
        if self.root == None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        # cur node - текущий узел
        # Если значение меньше текущего узла
        if value < cur_node.value:
            # Если нет левого ребенка
            if cur_node.left_child == None:
                # Установка левого ребенка
                cur_node.left_child = node(value)
                # Установка родителя для левого ребенка
                cur_node.left_child.parent = cur_node
            else:
                # Рекурсивно вызываем эту функцию для левого ребенка
                self._insert(value, cur_node.left_child)
        # Если значение больше текущего узла
        elif value > cur_node.value:
            # Если нет правого ребенка
            if cur_node.right_child == None:
                # Установка правого ребенка
                cur_node.right_child = node(value)
                # Установка родителя для правого ребенка
                cur_node.right_child.parent = cur_node
            else:
                # Рекурсивно вызываем эту функцию для правого ребенка
                self._insert(value, cur_node.right_child)
        else:
            print("Значение уже имеется в дереве!")

    # Поиск элемента в дереве
    def search(self, value):
        # Если есть корень
        if self.root != None:
            return self._search(value, self.root)
        else:
             return False

    # Поиск элемента в дереве
    def _search(self, value, cur_node):
        # Если значение совпадает с текущим значением
        if value == cur_node.value:
            return True
        # Если значение меньше текущего значения и есть левый ребенок
        elif value < cur_node.value and cur_node.left_child != None:
            # Рекурсивно вызывает поиск для левого ребенка
            return self._search(value, cur_node.left_child)
        # Если значение больше текущего значения и есть правый ребенок
        elif value > cur_node.value and cur_node.right_child != None:
            # Рекурсивно вызывает поиск для правого ребенка
            return self._search(value, cur_node.right_child)
        return False

    def delete_value(self, value):
        global array
        global tree
        while value in array:
            array.remove(value)
        new_tree = binary_search_tree()
        for number in array:
            new_tree.insert(number)
        tree = new_tree

print("Вывод времени поиска для поиска бинарным деревом")
# Время старта
start = time.time()

tree = binary_search_tree()
for number in array:
    tree.insert(number)
# Время после построения дерева
tree_time = time.time() - start

tree.search(0)
# Время после поиска
first = time.time() - start

# Время на построение и поиск нулевого элемента
print("Время, затраченное на построение дерева и поиск нулевого элемента:", first)
