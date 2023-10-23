import game_map
import numpy as np

# 定义生命游戏类：控制完整游戏逻辑，按照地图数据依照逻辑进行相应更新
class LifeGame:
    def __init__(self, map_rows = 1, map_cols = 1, life_init_ratio = 0.0):
        """将在主程序中初始化实例"""
        self.map = game_map.GameMap(map_rows, map_cols)
        self.map.reset(life_init_ratio)

        

    def game_cycle(self):
        
        """进行一次游戏循环，将在此完成地图的更新 将在计时器触发时被调用"""
        new_map = game_map.GameMap(self.map.rows, self.map.cols)
        for i in range(self.map.rows):
            for j in range(self.map.cols):
                count = self.map.get_neighbor_count(i, j)
                if self.map.get(i, j):
                    if count < 2 or count > 3:
                        new_map.set(i, j, 0)
                    else:
                        new_map.set(i, j, 1)
                else:
                    if count == 3:
                        new_map.set(i, j, 1)
        self.map = new_map
        
        
        
        
    