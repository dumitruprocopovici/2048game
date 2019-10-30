from tkinter import *

matrix = [[0, 0, 2, 4],
          [4, 8, 2, 4],
          [8, 16, 2, 1024],
          [16, 32, 64, 512]]


def color_label(position, matrix):

    colors = {0: 'gray', 2: 'gray', 4: 'gray',
              8: 'yellow', 16: 'yellow',
              32: 'orange', 64: 'orange',
              128: 'red', 256: 'red',
              512: 'magenta', 1024: 'magenta',
              2048: 'green', 4096: 'green',
              8192: 'cyan', 16384: 'cyan'}

    return colors[matrix[position % 4][position//4]]


def check_if_null(matrix, position):
    if matrix[position % 4][position // 4] == 0:
        return ''
    else:
        return matrix[position % 4][position // 4]


def init_matrix(matrix):
    window = Tk()
    window.title("Game 2048")
    l = []
    for j in range(16):
        temp = Label(window, height=5, width=10, font="Times 20 bold", text=check_if_null(matrix, j),
                     bg=color_label(j, matrix), borderwidth=2, relief="sunken")
        temp.grid(row=j % 4, column=j // 4)
        l.append(temp)
    window.mainloop()
    return l


# l1.configure(background="red")
init_matrix(matrix)
