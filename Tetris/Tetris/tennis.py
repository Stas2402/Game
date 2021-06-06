import tkinter
import time
from objects import Ball, Platform, Score

def start():

    tk = tkinter.Tk()
    tk.wm_title('Tennis')
    canvas = tkinter.Canvas(tk, width=500, height=500)
    canvas.pack()

    #x-->(width)              y^(height)
    score = Score(canvas)
    platform = Platform(canvas, color='green')
    ball = Ball(canvas, platform, score, color='red')

    tk.update()

    while ball.not_loose:
        ball.move()
        platform.move()
        tk.update()
        time.sleep(0.01)

    time.sleep(2)