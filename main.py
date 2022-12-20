import tkinter as tk
from tkinter import messagebox
run = True # The break the infinite replay loop
bgc = '#B3C9FF' #Background color of the window

while run :
    # Necessary variables for storing the information of each positions
    pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    val = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    but = [[], [], [], [], [], [], [], [], []]
    lab = []

    # To keep count of how many x and o have been placed
    xo = 0

    # Actual window which contains all the game buttons
    window = tk.Tk()
    window.geometry('432x454')
    window.title("Tic-Tac-Toe Game")

    # Importing images of x and o for enhancement
    ximage = tk.PhotoImage(file= 'images/ximg.png')
    oimage = tk.PhotoImage(file= 'images/oimg.png')

    # Function to be invoked if the window is closed midgame
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()
            global run
            run = False

    # Creating a list for button information storing button positions
    for i in range(len(but)):
        exec('but[i].append("b{}")'.format(pos[i]))
        if i < 3:
            but[i].append(i * 140 + 15)
            but[i].append(10)
        elif i >= 3 and i < 6:
            but[i].append((i - 3) * 140 + 15)
            but[i].append(160)
        elif i >= 6 and i < 9:
            but[i].append((i - 6) * 140 + 15)
            but[i].append(310)

    # Creating all the nine buttons
    for i in but:
        exec('{} = tk.Button(relief = "solid", height = 8, width = 16, command = lambda : replace({}))'.format(i[0], i))
        exec('{}.place(x = {}, y = {})'.format(i[0], i[1], i[2]))

    # Checking is X has won
    def Xwin():
        if (val[0] == 'X' and val[1] == 'X' and val[2] == 'X') \
                or (val[0] == 'X' and val[4] == 'X' and val[8] == 'X') \
                or (val[0] == 'X' and val[3] == 'X' and val[6] == 'X') \
                or (val[1] == 'X' and val[4] == 'X' and val[7] == 'X') \
                or (val[3] == 'X' and val[4] == 'X' and val[5] == 'X') \
                or (val[6] == 'X' and val[7] == 'X' and val[8] == 'X') \
                or (val[2] == 'X' and val[5] == 'X' and val[8] == 'X') \
                or (val[2] == 'X' and val[4] == 'X' and val[6] == 'X'):
            return True
        else:
            return False

    # Checking if O has won
    def Owin():
        if (val[0] == 'O' and val[1] == 'O' and val[2] == 'O') \
                or (val[0] == 'O' and val[4] == 'O' and val[8] == 'O') \
                or (val[0] == 'O' and val[3] == 'O' and val[6] == 'O') \
                or (val[1] == 'O' and val[4] == 'O' and val[7] == 'O') \
                or (val[3] == 'O' and val[4] == 'O' and val[5] == 'O') \
                or (val[6] == 'O' and val[7] == 'O' and val[8] == 'O') \
                or (val[2] == 'O' and val[5] == 'O' and val[8] == 'O') \
                or (val[2] == 'O' and val[4] == 'O' and val[6] == 'O'):
            return True
        else:
            return False

    # Function to be invoked when a button is pressed
    def replace(n):
        global xo, lab, val
        xo += 1
        exec('{}.destroy()'.format(n[0]))

        # If it is H's chance X image has to placed, else O image has to be placed
        if xo % 2 == 0:
            txt = "ximage"
            color = "red"
        else:
            txt = "oimage"
            color = "green"
        exec('l{} = tk.Label(image = {}, bg = "{}", height = 120, width = 120).place(x = {}, y = {})'.format(n[0], txt, color, n[1],
                                                                                                           n[2]))
        lab.append([int(n[0][1]), txt[0].upper()])
        val[int(n[0][1]) - 1] = txt[0].upper()

        # Checking is either x or o has won
        res = check(txt[0].upper())
        if res:
            ans = messagebox.askyesno("Congratulation", "Congratulations!! {} has won the game\n\nDo you want too play again ??".format(txt[0].upper()))
            if ans != True :
                window.destroy()
                global run
                run = False
            elif ans :
                window.destroy()

        # If all the positions has been filled and none of them has won, means its a tie
        if draw() and res != True:
            dans = messagebox.askyesno("Game Draw", "The game has ended in a draw\n\nDo you want to play again ??")
            if dans :
                window.destroy()
            elif dans != True :
                window.destroy()
                run = False

    # To check if all the positions has been filled
    def draw() :
        global val
        t = True
        for i in val :
            if i == ' ' :
                t = False
        return t

    # To check if either x or o has won
    def check(txt):
        global val
        if Xwin():
            return True
        elif Owin():
            return True
        else:
            return False

    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.configure(bg = bgc)
    window.resizable(0, 0)
    window.mainloop()

