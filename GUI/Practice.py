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
        self.food = self.canvas.create_rectangle(0,0, fill='#00FF00', outline='#00FF00')
        self.point_score = self.canvas.create_text(455, 15, fill='white', text='score:0')
    def restart(self):
        self.destroy()
        main()
    def queue_handler(self):
        try:
            while True:
                task = self.queue.get(block=False)
                if task.get('game_over'):
                    self.game_over()
                elif task.get('move'):
                    points = [x for point in task['move'] for x in point]
                    self.canvas.coords(self.snake, *points)
                elif task.get('food'):
                    self.canvas.coords(self.food, *task['food'])
                elif task.get('points_score'):
                    self.canvas.itemconfigure(self.point_score,
                                              text='score:{}'.format(task['points_score']))
                    self.queue.task_done()
        except queue.Empty:
            if not self.is_game_over:
                self.canvas.after(100, self.queue_handler)

    def game_over(self):
        self.is_game_over = True
        self.canvas.create_text(220, 150, fill='white',text='Game Over!')
        quitbtn = Button(self, text='Quit', command=self.destroy)
        retbtn = Button(self, text='Resume', command=self.restart)
        self.canvas.create_window(230, 180, anchor=W, window=quitbtn)
        self.canvas.create_window(200, 180, anchor=E, window=retbtn)




def main():
    q = queue.Queue()
    gui = GUI(q)
    gui.mainloop()

if __name__ == '__main__':
    main()
