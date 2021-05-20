
class Node:
    def __init__(self, state, operator=None, parent=None, g=float('inf'), h=float('inf')):
        self.state = state
        self.operator = operator
        self.parent = parent
        self.g = g
        self.h = h

    @property
    def f(self):
        return self.g + self.h

    def __hash__(self):
        return hash(self.state_string())

    def __eq__(self, other):
        return self.state == other.state

    def __repr__(self):
        return '<' + self.state_string() + '>'

    def __lt__(self, other):
        return self.f < other.f

    def state_string(self):
        return ','.join(str(x) for x in self.state)


class Algorithm:
    def __init__(self, method, name):
        self.method = method
        self.name = name


class TilePuzzle:
    def __init__(self, size, initial_state):
        self.size, self.root = size, initial_state
        self.algorithms = {1: Algorithm(self._a_star, 'A*')}
        self.length = self.size ** 2
        self.goal = [x % self.length for x in range(1, self.length + 1)]

    def _successors(self, node):
        successors = []
        z = node.state.index(0)

        # Up
        if z + self.size < self.length:
            state_copy = list(node.state)
            state_copy[z], state_copy[z + self.size] = state_copy[z + self.size], state_copy[z]
            successors.append(Node(state_copy, 'U', node))

        # Down
        if z - self.size >= 0:
            state_copy = list(node.state)
            state_copy[z], state_copy[z - self.size] = state_copy[z - self.size], state_copy[z]
            successors.append(Node(state_copy, 'D', node))

        # Left
        if z % self.size + 1 < self.size:
            state_copy = list(node.state)
            state_copy[z], state_copy[z + 1] = state_copy[z + 1], state_copy[z]
            successors.append(Node(state_copy, 'L', node))

        # Right
        if z % self.size - 1 >= 0:
            state_copy = list(node.state)
            state_copy[z], state_copy[z - 1] = state_copy[z - 1], state_copy[z]
            successors.append(Node(state_copy, 'R', node))

        return successors

    def get_path_from_root(self, node):
        path = []
        current = node
        while current is not self.root:
            path.append(current.operator)
            current = current.parent
        path.reverse()
        return ''.join(path)

    def solve(self, algorithm_num):
        if algorithm_num in self.algorithms:
            algorithm = self.algorithms[algorithm_num]
            result = algorithm.method()
            return result

    def _list_index_to_matrix_index(self, i):
        return int(i / self.size), i % self.size

    def _manhattan_distance(self, state_as_list):
        distances_sum = 0
        for current_index, n in enumerate(state_as_list):
            if n == 0:
                continue

            current_row, current_column = self._list_index_to_matrix_index(current_index)
            goal_row, goal_column = self._list_index_to_matrix_index(self.goal.index(n))
            distances_sum += abs(goal_row - current_row) + abs(goal_column - current_column)

        return distances_sum

    def _a_star(self):
        from heapq import heappush, heappop

        opened = []
        self.root.g = 0
        self.root.h = self._manhattan_distance(self.root.state)
        heappush(opened, self.root)

        counter = 0
        while opened:
            n = heappop(opened)
            counter += 1
            if n.state == self.goal:
                path = self.get_path_from_root(n)
                return path, counter, n.g

            for s in self._successors(n):
                s.g = n.g + 1
                s.h = self._manhattan_distance(s.state)
                heappush(opened, s)
        return None, counter, -1


def main(board):
    algorithm_number = 1
    board_size = 4
    root = Node(board, 0)
    t = TilePuzzle(board_size, root)
    solution_path, total_opened, depth = t.solve(algorithm_number)
    if solution_path:
        result_string = solution_path

    return result_string