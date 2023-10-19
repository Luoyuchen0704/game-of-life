import tkinter as tk
import game_timer
# 定义UI类 game_ui.py
class GameUI:
    def __init__(self, game, timer,w,h,a):
        """初始化UI界面"""
        self.game = game
        self.timer = timer

        self.root = tk.Tk()
        self.root.title("生命游戏")

        self.canvas = tk.Canvas(self.root, width=w, height=h)
        self.canvas.pack()

        self.a = a

    def draw(self):
        """绘制UI界面"""
        self.canvas.delete("all")
        for row in range(self.game.map.rows):
            for col in range(self.game.map.cols):
                state = self.game.map.get(row, col)
                if state == 1:
                    self.canvas.create_rectangle(col*self.a, row*self.a, col*self.a+self.a, row*self.a+self.a, fill="black")
                else:
                    self.canvas.create_rectangle(col*self.a, row*self.a, col*self.a+self.a, row*self.a+self.a, fill="white")

    def update(self):
        """更新UI界面"""
        self.draw()
        self.timer.start()
        self.root.after(100, self.update)

    def run(self):
        """运行UI界面"""
        self.update()
        self.root.mainloop()

