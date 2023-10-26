import tkinter as tk
import game_timer

# 定义UI类：创建和管理图形用户界面
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

        for row in range(self.game.map.rows):
            for col in range(self.game.map.cols):
                if self.game.map.get(row, col):
                    self.canvas.create_rectangle(col*self.a, row*self.a, col*self.a+self.a, row*self.a+self.a, fill="black")
                else:
                    self.canvas.create_rectangle(col*self.a, row*self.a, col*self.a+self.a, row*self.a+self.a, fill="white")


    def draw(self):
        """绘制UI界面,尚存优化空间，不必每次都重绘地图，更改一下由0->1和由1->0的状态就好了"""
        while self.game.turn_alive:
            self.canvas.create_rectangle(self.game.turn_alive[-1][1]*self.a, self.game.turn_alive[-1][0]*self.a, self.game.turn_alive[-1][1]*self.a+self.a, self.game.turn_alive[-1][0]*self.a+self.a, fill="black")
            self.game.turn_alive.pop()
        while self.game.turn_dead:
            self.canvas.create_rectangle(self.game.turn_dead[-1][1]*self.a, self.game.turn_dead[-1][0]*self.a, self.game.turn_dead[-1][1]*self.a+self.a, self.game.turn_dead[-1][0]*self.a+self.a, fill="white")
            self.game.turn_dead.pop()
        
    def update(self):
        """更新UI界面"""
        self.draw()
        self.timer.start()
        self.root.after(1, self.update)

    def run(self):
        """运行UI界面"""
        self.update()
        self.root.mainloop()


