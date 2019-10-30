from random import randint
from os import system
from pynput.keyboard import Key, Listener

possible_values = {0: "  -  ",
                   2: "  2  ",
                   4: "  4  ",
                   8: "  8  ",
                   16: "  16 ",
                   32: "  32 ",
                   64: "  64 ",
                   128: " 128 ",
                   256: " 256 ",
                   512: " 512 ",
                   1024: " 1024",
                   2048: " 2048",
                   4096: " 4096",
                   8192: " 8192",
                   16384: "16384"
                   }


def initialize_matrix():
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
    return(M)


def new_element(masa):
    list = []
    for i in range(4):
        for j in range(4):
            if masa[i][j] == 0:
                list.append((i, j))
    if len(list) == 0:
        position = 0
    else:
        position = randint(0, len(list)-1)
    i = list[position][0]
    j = list[position][1]
    a = randint(0, 1)
    if a == 0:
        masa[i][j] = 2
    else:
        masa[i][j] = 4
    return (masa)


def display_board(masa):
    system('cls')
    print("------------------------------\n")
    print(possible_values[masa[0][0]] + " | "
          + possible_values[masa[0][1]] + " | "
          + possible_values[masa[0][2]] + " | "
          + possible_values[masa[0][3]] + "\n")
    print(possible_values[masa[1][0]] + " | "
          + possible_values[masa[1][1]] + " | "
          + possible_values[masa[1][2]] + " | "
          + possible_values[masa[1][3]] + "\n")
    print(possible_values[masa[2][0]] + " | "
          + possible_values[masa[2][1]] + " | "
          + possible_values[masa[2][2]] + " | "
          + possible_values[masa[2][3]] + "\n")
    print(possible_values[masa[3][0]] + " | "
          + possible_values[masa[3][1]] + " | "
          + possible_values[masa[3][2]] + " | "
          + possible_values[masa[3][3]] + "\n")
    print("------------------------------")


def game_over(masa):
    verificare = False
    for i in range(4):
        for j in range(3):
            if (masa[i][j] == masa[i][j+1] and masa[i][j] != 0) or (masa[i][j] == 0 and masa[i][j+1] > 0):
                verificare = True
    for i in range(4):
        for j in range(1, 4):
            if (masa[i][j] == masa[i][j-1] and masa[i][j] != 0) or (masa[i][j] == 0 and masa[i][j-1] > 0):
                verificare = True
    for i in range(1, 4):
        for j in range(4):
            if (masa[i][j] == masa[i-1][j] and masa[i][j] != 0) or (masa[i-1][j] == 0 and masa[i][j] > 0):
                verificare = True
    for i in range(3):
        for j in range(4):
            if (masa[i][j] == masa[i+1][j] and masa[i][j] != 0) or (masa[i+1][j] == 0 and masa[i][j] > 0):
                verificare = True
    if verificare == False:
        print("game over, try again")
        exit()


def arrows_input():
    keyPressed = None

    def on_press(key):
        nonlocal keyPressed
        keyPressed = key
        return False
    with Listener(on_press=on_press) as listener:
        listener.join()
    keyPressed = str(keyPressed)
    if keyPressed == 'Key.up':
        return('up')
    elif keyPressed == 'Key.down':
        return('down')
    elif keyPressed == 'Key.left':
        return('left')
    elif keyPressed == 'Key.right':
        return ('right')


def check_move(masa, directie):
    if directie == "left":
        for i in range(4):
            for j in range(3):
                if (masa[i][j] == masa[i][j+1] and masa[i][j] != 0) or (masa[i][j] == 0 and masa[i][j+1] > 0):
                    return(True)
    elif directie == "right":
        for i in range(4):
            for j in range(1, 4):
                if (masa[i][j] == masa[i][j-1] and masa[i][j] != 0) or (masa[i][j] == 0 and masa[i][j-1] > 0):
                    return(True)
    elif directie == "up":
        for i in range(1, 4):
            for j in range(4):
                if (masa[i][j] == masa[i-1][j] and masa[i][j] != 0) or (masa[i-1][j] == 0 and masa[i][j] > 0):
                    return(True)
    elif directie == "down":
        for i in range(3):
            for j in range(4):
                if (masa[i][j] == masa[i+1][j] and masa[i][j] != 0) or (masa[i+1][j] == 0 and masa[i][j] > 0):
                    return(True)
    return(False)


def move_left(masa):
    for i in range(4):
        for j in range(4):
            if masa[i][j] == 0:
                masa[i].pop(j)
                masa[i].append(0)
        for j in range(4):
            if masa[i][j] == 0:
                masa[i].pop(j)
                masa[i].append(0)
        for j in range(3):
            if masa[i][j] == masa[i][j + 1]:
                masa[i][j] *= 2
                masa[i].pop(j + 1)
                masa[i].append(0)
    return(masa)


def move(masa, directie):
    if directie == "left":
        move_left(masa)
    elif directie == "right":
        for i in range(4):
            masa[i] = masa[i][::-1]
        move_left(masa)
        for i in range(4):
            masa[i] = masa[i][::-1]
    elif directie == "up":
        masa = [[masa[j][i] for j in range(len(masa))]
                for i in range(len(masa[0]))]
        move_left(masa)
        masa = [[masa[j][i] for j in range(len(masa))]
                for i in range(len(masa[0]))]
    elif directie == "down":
        masa = [[masa[j][i] for j in range(len(masa))]
                for i in range(len(masa[0]))]
        for i in range(4):
            masa[i] = masa[i][::-1]
        move_left(masa)
        for i in range(4):
            masa[i] = masa[i][::-1]
        masa = [[masa[j][i] for j in range(len(masa))]
                for i in range(len(masa[0]))]
    return (masa)


matrix = initialize_matrix()
while True:
    possible_move = False
    matrix = new_element(matrix)
    display_board(matrix)
    game_over(matrix)
    while possible_move == False:
        direction = arrows_input()
        possible_move = check_move(matrix, direction)
    matrix = move(matrix, direction)
