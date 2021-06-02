import random

class Ball:

    def __init__(self, canvas, platform, score, color):
        self.canvas = canvas
        self.color = color
        self.platform = platform
        self.not_loose = True
        self.score = score
        # x--> y^
        self.ball_id = canvas.create_oval(10, 10, 25, 25, fill=self.color)
        self.canvas.move(self.ball_id, 245, 200)

        #start directions
        starts = [-2, -1, 1, 2]
        random.shuffle(starts)

        self.x = starts[0]
        self.y = 2

    def get_coords(self):
        return self.canvas.coords(self.ball_id)

    def move(self):
        self.canvas.move(self.ball_id, self.x, self.y)

        platform_pos = self.platform.get_coords()
        ball_pos = self.get_coords()

        # [0] x1  [1] y1   [2] x2    [3] y2
        # x1y1 ____________
        #      |           |            |
        #      |           |            V Y  ---> X
        #      |           |
        #      |___________| x2 y2
        # Loose == hit bottom
        if ball_pos[3] >= self.canvas.winfo_height():
            self.canvas.create_text(250, 120, text='Вы проиграли', font=('Courier', 30), fill='red')
            self.not_loose = False
        # hit platform
        elif ball_pos[3] >= platform_pos[1] and ball_pos[0] >= platform_pos[0] and ball_pos[2] <= platform_pos[2]:
            self.y *= -1
            self.score.update_score()

        # hit left border
        elif ball_pos[0] <= 0:
            self.x *= -1
        # hit right border
        elif ball_pos[2] >= self.canvas.winfo_width():
            self.x *= -1
        # hit top
        elif ball_pos[1] <= 0:
            self.y *= -1




class Platform:

    def __init__(self, canvas, color):
        self.canvas = canvas
        self.color = color
        self.x = 0
        self.platform_id = canvas.create_rectangle(100, 490, 200, 500, fill=self.color)

        # key press handlers
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Up>', self.restart)

    def get_coords(self):
        return self.canvas.coords(self.platform_id)

    def restart(self, event):
        self.x = 0

    def turn_right(self, event):
        self.x = 3

    def turn_left(self, event):
        self.x = - 3

    def move(self):
        self.canvas.move(self.platform_id, self.x, 0)
        pos = self.canvas.coords(self.platform_id)
        if pos[0] < 0 or pos[2] > 500:
            self.x = 0


class Score:

    def __init__(self, canvas):
        self.canvas = canvas
        self.points = 0
        self.score = self.canvas.create_text(450, 50, text='0', font=('Courier', 15), fill='blue')
        self.canvas.create_text(400, 50, text='Score:', font=('Courier', 15), fill='blue')

    def update_score(self):
        self.points += 1
        self.canvas.itemconfig(self.score, text=self.points)

