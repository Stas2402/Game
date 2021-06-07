import tkinter
import time
from objects import TetrisFigure, TetrisGame

def start():

    tk = tkinter.Tk()
    tk.wm_title('Tetris')
    canvas = tkinter.Canvas(tk, width=500, height=500)
    canvas.pack()
    tk.update()
    figure = TetrisFigure(canvas)
    Game_field = TetrisGame(canvas)
    #x-->(width)              y^(height)

    tk.mainloop()

    time.sleep(2)