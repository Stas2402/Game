import tennis
import tkinter
import tetris


class TopMenu:
    def __init__(self, root):
        self.root = root
        top_menu = tkinter.Menu(root, bg='grey')
        self.root.configure(menu=top_menu)

        first_item = tkinter.Menu(top_menu, tearoff=0)
        top_menu.add_cascade(label='Game', menu=first_item)
        first_item.add_command(label='Main menu')
        first_item.add_command(label='Tennis', command=tennis.start)
        first_item.add_command(label='Tetris', command=tetris.start)
        first_item.add_separator()


        top_menu.add_command(label='Quit', command=self.close_window)


    def close_window(self):
        self.root.quit()

