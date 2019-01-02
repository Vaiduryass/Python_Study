from tkinter import *
import threading
import queue
import time
import random


class GUI(Tk):
    def __init__(self, queue):
        Tk.__init__(self)
        self.queue = queue
        self.is_game_over = False
        self.canvas = Canvas(self, width=495, height=305, bg='#000000')
        self.canvas.pack()
        self.snake = self.canvas.create_line((0,0),(0,0), fill='#FFFF00', width=10)
        self.food = self.canvas.create_rectangle(0,0,0,0, fill='#00FF00', outline='#00FF00')
        self.point_score = self.canvas.create_text(455, 15, fill='white', text='score:0')



def main():
    q = queue.Queue()
    gui = GUI(q)
    gui.mainloop()

if __name__ == '__main__':
    main()
