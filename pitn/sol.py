from copy import deepcopy


def successor(board):
    child = 0
    successor_boards = []
    temp1 = deepcopy(board)
    temp2 = deepcopy(board)
    temp3 = deepcopy(board)
    temp4 = deepcopy(board)
    for row in range(0, 4):
        for col in range(0, 4):
            if board[0][row][col] == 0 and child < 4:


                if row == 3:
                    a = board[0][row][col]
                    b = board[0][0][col]
                    a, b = b, a
                    temp1[0][row][col] = a
                    temp1[0][0][col] = b
                    log=temp1[1]
                    log.append('U')
                    successor_boards.append([temp1[0],log])
                    child += 1
                else:
                    a = board[0][row][col]
                    b = board[0][row + 1][col]
                    a, b = b, a
                    temp1[0][row][col] = a
                    temp1[0][row + 1][col] = b
                    log=temp1[1]
                    log.append('U')
                    successor_boards.append([temp1[0],log])
                    child += 1


                if row == 0:
                    a = board[0][row][col]
                    b = board[0][3][col]
                    a, b = b, a
                    temp2[0][row][col] = a
                    temp2[0][3][col] = b
                    log=temp2[1]
                    log.append('D')
                    successor_boards.append([temp2[0],log])
                    child += 1
                else:
                    a = board[0][row][col]
                    b = board[0][row - 1][col]
                    a, b = b, a
                    temp2[0][row][col] = a
                    temp2[0][row - 1][col] = b
                    log=temp2[1]
                    log.append('D')
                    successor_boards.append([temp2[0], log])
                    child += 1


                if col == 3:
                    a = board[0][row][col]
                    b = board[0][row][0]
                    a, b = b, a
                    temp3[0][row][col] = a
                    temp3[0][row][0] = b
                    log = temp3[1]
                    log.append('L')
                    successor_boards.append([temp3[0], log])
                    child += 1
                else:
                    a = board[0][row][col]
                    b = board[0][row][col + 1]
                    a, b = b, a
                    temp3[0][row][col] = a
                    temp3[0][row][col + 1] = b
                    log = temp3[1]
                    log.append('L')
                    successor_boards.append([temp3[0], log])
                    child += 1


                if col == 0:
                    a = board[0][row][col]
                    b = board[0][row][3]
                    a, b = b, a
                    temp4[0][row][col] = a
                    temp4[0][row][3] = b
                    log = temp4[1]
                    log.append('R')
                    successor_boards.append([temp4[0], log])
                    child += 1
                else:
                    a = board[0][row][col]
                    b = board[0][row][col - 1]
                    a, b = b, a
                    temp4[0][row][col] = a
                    temp4[0][row][col - 1] = b
                    log = temp4[1]
                    log.append('R')
                    successor_boards.append([temp4[0], log])
                    child += 1
    return successor_boards


def is_goal(board):
    if board==goal_board:
        return True


def get_element_distance(a,b):
    if a==0 and b==0:
        return 0
    elif a==1 and b==0:
        return 1
    elif a==2 and b==0:
        return 2
    elif a==3 and b==0:
        return 1

    elif a==0 and b==1:
        return 1
    elif a==1 and b==1:
        return 0
    elif a==2 and b==1:
        return 1
    elif a==3 and b==1:
        return 2

    elif a==0 and b==2:
        return 2
    elif a==1 and b==2:
        return 1
    elif a==2 and b==2:
        return 0
    elif a==3 and b==2:
        return 1

    elif a==0 and b==3:
        return 1
    elif a==1 and b==3:
        return 2
    elif a==2 and b==3:
        return 1
    elif a==3 and b==3:
        return 0

def get_board_distance(board):
    map = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (3, 0),(3, 1), (3, 2), (3, 3)]
    distance = 0
    for r in range(0, 4):
        for c in range(0, 4):
            if board[r][c]!=0:
                row = map[board[r][c] - 1][0]
                col = map[board[r][c] - 1][1]
                distance = distance + get_element_distance(row, r) + get_element_distance(col, c)
    return distance


def fringe_pop(fringe):
    ind=0
    fos=999999999999
    for f in fringe:
        if f[2]< fos:
            fos=f[2]
            ind=fringe.index(f)
    return fringe.pop(ind)


def fringe_append(successor_boards,fringe,popped_elements):
    fos = 999999999999
    for s in range(0,4):
        add=1
        cos=len(successor_boards[s][1])
        hos = get_board_distance(successor_boards[s][0])
        fos_current=hos+cos
        successor_boards[s]=[successor_boards[s][0],successor_boards[s][1],fos_current]
        for elements in popped_elements:
            if successor_boards[s][0]==elements[0]:
                add=0
        if add==1:
            fringe.append(successor_boards[s])

goal_board=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
fos = 0

def main(q):
    board=q
    fringe=[]
    log=[]
    popped_elements=[]
    fos=get_board_distance(board)
    fringe.append([board,log,fos])
    p = 0
    while 1:
        p+=1
        if fringe == []:
            exit(1)
        else:
            s=fringe_pop(fringe)
            popped_elements.append(s)
            if s:
                if is_goal(s[0]):
                    return s
                else:
                    successor_boards=successor(s)
                    fringe_append(successor_boards,fringe,popped_elements)