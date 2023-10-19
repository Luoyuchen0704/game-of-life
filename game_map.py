import random
# 定义地图类 game_map.py
class GameMap(object):
    def __init__(self, rows, cols):
        """初始化地图"""
        self.rows = rows
        self.cols = cols
        self.map = [[0 for j in range(cols)] for i in range(rows)]

    def reset(self, life_ratio):
        """重置地图并按life_ratio随机地填充一些活细胞"""
        for i in range(self.rows):
            for j in range(self.cols):
                if random.random() < life_ratio:
                    self.map[i][j] = 1
                else:
                    self.map[i][j] = 0

    def get_neighbor_count(self, row, col):
        """获取地图上一个方格周围活细胞数"""
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if self.map[(row + i) % self.rows][(col + j) % self.cols] == 1:
                    count += 1
        return count

    def set(self, row, col, val):
        """设置地图上方格的状态"""
        self.map[row][col] = val

    def get(self, row, col):
        """获取地图上方格的状态"""
        return self.map[row][col]

    def print_map(self):
        """打印地图上方格的状态"""
        for i in range(0,self.rows):
           for j in range(0,self.cols):
               print(self.map[i][j],end=' ')
           print()

    def compare_map(self,new_map):
        """比较地图上方格的状态"""
        ret = 1
        for i in range(0,self.rows):
           for j in range(0,self.cols):
               if self.map[i][j] != new_map[i][j] :
                   ret = 0
        return ret

