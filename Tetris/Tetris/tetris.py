import tkinter
import time
from objects import TetrisFigure

def start():

    tk = tkinter.Tk()
    tk.wm_title('Tetris')
    canvas = tkinter.Canvas(tk, width=500, height=500)
    canvas.pack()

    figure = TetrisFigure(canvas)

    #x-->(width)              y^(height)

    tk.update()
    tk.mainloop()

    time.sleep(2)