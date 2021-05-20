from random import shuffle
from tkinter import *
import sol
import new1
BOARD_SIZE = 4
SQUARE_SIZE = 80
EMPTY_SQUARE = BOARD_SIZE ** 2

root = Tk()
root.title("Пятнашки")

c = Canvas(root, width=BOARD_SIZE * SQUARE_SIZE,
           height=BOARD_SIZE * SQUARE_SIZE, bg='#FFCC66')
c.pack()

def Astar1():
    board[board.index(16)] = 0
    solutions = new1.main(board)
    board[board.index(0)] = 16
    for i in range(len(solutions)):
        global solution
        solu = solutions[i]
        empty_index = board.index(EMPTY_SQUARE)
        if solu == 'R':
            board_index = empty_index - 1
        elif solu == 'L':
            board_index = empty_index + 1
        elif solu == 'U':
            board_index = empty_index + 4
        elif solu == 'D':
            board_index = empty_index - 4
        empty_index = get_empty_neighbor(board_index)
        board[board_index], board[empty_index] = board[empty_index], board[board_index]
        solution.append(board[empty_index]) if board[empty_index] != 16 else solution.append(0)
        draw_board()
        if board == correct_board:
            print(solution)
            show_victory_plate()
        root.after(500)
        root.update()
def lob():
    solutions = sol.main(toMatrix(board))
    for i in range(solutions[2]):
        global solution
        solu = solutions[1][i]
        empty_index = board.index(EMPTY_SQUARE)
        if solu == 'R':
            board_index = empty_index - 1
        elif solu == 'L':
            board_index = empty_index + 1
        elif solu == 'U':
            board_index = empty_index + 4
        elif solu == 'D':
            board_index = empty_index - 4
        empty_index = get_empty_neighbor(board_index)
        board[board_index], board[empty_index] = board[empty_index], board[board_index]
        solution.append(board[empty_index]) if board[empty_index] != 16 else solution.append(0)
        draw_board()
        if board == correct_board:
            print(solution)
            show_victory_plate()
        root.after(500)
        root.update()


btnA = Button(text="Astar",command=Astar1)
btnA.pack()
btn = Button(text="B lob",command=lob)
btn.pack()


def toMatrix(boardq):
    lines = [[0,0,0,0] for i in range(4)]
    for row in range(0, 4):
        for col in range(0, 4):
            lines[row][col] = boardq[row*4+col]
            if lines[row][col] == 16:
                lines[row][col] = 0

    return lines

def get_inv_count():
    inversions = 0
    inversion_board = board[:]
    inversion_board.remove(EMPTY_SQUARE)
    for i in range(len(inversion_board)):
        first_item = inversion_board[i]
        for j in range(i+1, len(inversion_board)):
            second_item = inversion_board[j]
            if first_item > second_item:
                inversions += 1
    return inversions


def is_solvable():
    num_inversions = get_inv_count()
    if BOARD_SIZE % 2 != 0:
        return num_inversions % 2 == 0
    else:
        empty_square_row = BOARD_SIZE - (board.index(EMPTY_SQUARE) // BOARD_SIZE)
        if empty_square_row % 2 == 0:
            return num_inversions % 2 != 0
        else:
            return num_inversions % 2 == 0


def get_empty_neighbor(index):
    empty_index = board.index(EMPTY_SQUARE)
    abs_value = abs(empty_index - index)

    if abs_value == BOARD_SIZE:
        return empty_index
    elif abs_value == 1:
        max_index = max(index, empty_index)
        if max_index % BOARD_SIZE != 0:
            return empty_index
    return index


def draw_board():

    c.delete('all')


    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):

            index = str(board[BOARD_SIZE * i + j])

            if index != str(EMPTY_SQUARE):

                c.create_rectangle(j * SQUARE_SIZE, i * SQUARE_SIZE,
                                   j * SQUARE_SIZE + SQUARE_SIZE,
                                   i * SQUARE_SIZE + SQUARE_SIZE,
                                   fill='#CCCCCC',
                                   outline='#333333')

                c.create_text(j * SQUARE_SIZE + SQUARE_SIZE / 2,
                              i * SQUARE_SIZE + SQUARE_SIZE / 2,
                              text=index,
                              font="Arial {} italic".format(int(SQUARE_SIZE / 4)),
                              fill='#333333')


def show_victory_plate():

    c.create_rectangle(SQUARE_SIZE / 5,
                       SQUARE_SIZE * BOARD_SIZE / 2 - 10 * BOARD_SIZE,
                       BOARD_SIZE * SQUARE_SIZE - SQUARE_SIZE / 5,
                       SQUARE_SIZE * BOARD_SIZE / 2 + 10 * BOARD_SIZE,
                       fill='#000000',
                       outline='#FFFFFF')

    c.create_text(SQUARE_SIZE * BOARD_SIZE / 2, SQUARE_SIZE * BOARD_SIZE / 1.9,
                  text="Yep!!", font="Helvetica {} bold".format(int(10 * BOARD_SIZE)), fill='#DC143C')


def click(event):
    global solution

    x, y = event.x, event.y

    x = x // SQUARE_SIZE
    y = y // SQUARE_SIZE

    board_index = x + (y * BOARD_SIZE)


    empty_index = get_empty_neighbor(board_index)


    board[board_index], board[empty_index] = board[empty_index], board[board_index]
    solution.append(board[empty_index]) if board[empty_index] != 16 else solution.append(0)

    draw_board()

    if board == correct_board:
        print(solution)
        show_victory_plate()


c.bind('<Button-1>', click)
c.pack()


board = list(range(1, EMPTY_SQUARE + 1))
solution = []
correct_board = board[:]
shuffle(board)
board = [1, 2, 3, 4, 5, 6, 7, 8, 13, 9, 11, 12, 10, 14, 15, 16] # Доска из примера
while not is_solvable():
    shuffle(board)


draw_board()
root.mainloop()