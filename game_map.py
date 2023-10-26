import random

# 定义地图类:管理与地图相关一切数据的初始化、获取、更新等
class GameMap(object):
    def __init__(self, rows, cols):
        """初始化地图"""
        self.rows = rows
        self.cols = cols
        self.map = [[0 for j in range(cols)] for i in range(rows)]

    def reset(self, life_ratio = 0.5):
        """重置地图并按life_ratio随机地填充一些活细胞"""
        if not isinstance(life_ratio,float):
            raise Typestance("life_ratio should be float")
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
                if i != 0 or j != 0:
                    count += self.map[(row + i) % self.rows][(col + j) % self.cols]
        return count




    def set(self, row, col, val):
        """设置地图上方格的状态"""
        self.map[row][col] = val

    def get(self, row, col):
        """获取地图上方格的状态"""
        return self.map[row][col]

    def compare_map(self,new_map):
        """比较地图上方格的状态"""
        ret = 1
        for i in range(0,self.rows):
           for j in range(0,self.cols):
               if self.map[i][j] != new_map[i][j] :
                   return 0
        return 1
    
