from tkinter import *
from random import randint
import sys


def keyPress(event):
    global window, matrix
    if event.keysym == 'Left':
        x = 'Left'
    elif event.keysym == 'Right':
        x = 'Right'
    elif event.keysym == 'Up':
        x = 'Up'
    elif event.keysym == 'Down':
        x = 'Down'
    key(x)


def color_label(position, matrix):

    color = {
        0: "#ccc",
        2: "#eee4da",
        4: "#ede0c8",
        8: "#f2b179",
        16: "#f59563",
        32: "#f67c5f",
        64: "#f65e3b",
        128: "#edcf72",
        256: "#edcc61",
        512: "#edc850",
        1024: "#edc53f",
        2048: "#edc22e"
    }

    return color[matrix[position % 4][position//4]]


def check_if_null(matrix, position):
    if matrix[position % 4][position // 4] == 0:
        return ''
    else:
        return matrix[position % 4][position // 4]


def initializeMatrix():
    M = []
    for j in range(4):
        l = []
        for k in range(4):
            l.append(0)
        M.append(l)
    a = randint(0, 1)
    if a == 0:
        M[randint(0, 3)][randint(0, 3)] = 2
    else:
        M[randint(0, 3)][randint(0, 3)] = 4
    return (M)


def game_over_check(matrix):
    verificare = False
    for i in range(4):
        for j in range(3):
            if (matrix[i][j] == matrix[i][j+1] and matrix[i][j] != 0) or (matrix[i][j] == 0 and matrix[i][j+1] > 0):
                verificare = True
    for i in range(4):
        for j in range(1, 4):
            if (matrix[i][j] == matrix[i][j-1] and matrix[i][j] != 0) or (matrix[i][j] == 0 and matrix[i][j-1] > 0):
                verificare = True
    for i in range(1, 4):
        for j in range(4):
            if (matrix[i][j] == matrix[i-1][j] and matrix[i][j] != 0) or (matrix[i-1][j] == 0 and matrix[i][j] > 0):
                verificare = True
    for i in range(3):
        for j in range(4):
            if (matrix[i][j] == matrix[i+1][j] and matrix[i][j] != 0) or (matrix[i+1][j] == 0 and matrix[i][j] > 0):
                verificare = True
    if verificare == False:
        exit()


def check_move(matrix, directie):
    if directie == "Left":
        for i in range(4):
            for j in range(3):
                if (matrix[i][j] == matrix[i][j+1] and matrix[i][j] != 0) or (matrix[i][j] == 0 and matrix[i][j+1] > 0):
                    return(True)
    elif directie == "Right":
        for i in range(4):
            for j in range(1, 4):
                if (matrix[i][j] == matrix[i][j-1] and matrix[i][j] != 0) or (matrix[i][j] == 0 and matrix[i][j-1] > 0):
                    return(True)
    elif directie == "Up":
        for i in range(1, 4):
            for j in range(4):
                if (matrix[i][j] == matrix[i-1][j] and matrix[i][j] != 0) or (matrix[i-1][j] == 0 and matrix[i][j] > 0):
                    return(True)
    elif directie == "Down":
        for i in range(3):
            for j in range(4):
                if (matrix[i][j] == matrix[i+1][j] and matrix[i][j] != 0) or (matrix[i+1][j] == 0 and matrix[i][j] > 0):
                    return(True)
    return(False)


def move_left(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                matrix[i].pop(j)
                matrix[i].append(0)
        for j in range(4):
            if matrix[i][j] == 0:
                matrix[i].pop(j)
                matrix[i].append(0)
        for j in range(3):
            if matrix[i][j] == matrix[i][j + 1]:
                matrix[i][j] *= 2
                matrix[i].pop(j + 1)
                matrix[i].append(0)
    return(matrix)


def move(matrix, directie):
    if directie == "Left":
        move_left(matrix)
    elif directie == "Right":
        for i in range(4):
            matrix[i] = matrix[i][::-1]
        move_left(matrix)
        for i in range(4):
            matrix[i] = matrix[i][::-1]
    elif directie == "Up":
        matrix = [[matrix[j][i] for j in range(len(matrix))]
                  for i in range(len(matrix[0]))]
        move_left(matrix)
        matrix = [[matrix[j][i] for j in range(len(matrix))]
                  for i in range(len(matrix[0]))]
    elif directie == "Down":
        matrix = [[matrix[j][i] for j in range(len(matrix))]
                  for i in range(len(matrix[0]))]
        for i in range(4):
            matrix[i] = matrix[i][::-1]
        move_left(matrix)
        for i in range(4):
            matrix[i] = matrix[i][::-1]
        matrix = [[matrix[j][i] for j in range(len(matrix))]
                  for i in range(len(matrix[0]))]
    return (matrix)


def new_element(matrix):
    list = []
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                list.append((i, j))
    if len(list) == 0:
        position = 0
    else:
        position = randint(0, len(list)-1)
    i = list[position][0]
    j = list[position][1]
    a = randint(0, 1)
    if a == 0:
        matrix[i][j] = 2
    else:
        matrix[i][j] = 4
    return (matrix)


def display_board(matrix, window):
    for j in range(16):
        temp = Label(window, height=2, width=4, font="Times 40 bold", text=check_if_null(matrix, j),
                     bg=color_label(j, matrix), borderwidth=2, relief="sunken")
        temp.grid(row=j % 4, column=j // 4)
    window.update()


def initializeDisplay():
    global window, matrix
    display_board(matrix, window)
    for i in ["Left", "Right", "Up", "Down"]:
        window.bind("<" + i + ">", keyPress)
    window.focus_set()


def key(x):
    global window, matrix
    game_over_check(matrix)
    possible_move = check_move(matrix, x)
    if possible_move == True:
        matrix = move(matrix, x)
        matrix = new_element(matrix)
        display_board(matrix, window)


window = Tk()
matrix = initializeMatrix()
initializeDisplay()
window.mainloop()
