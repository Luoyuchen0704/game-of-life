import unittest
from unittest.mock import MagicMock
from life_game import LifeGame
from game_map import GameMap


class Test_TestLifeGame(unittest.TestCase):
    def test_game_cycle(self):
       game = LifeGame(10,10,0) 
       game.map.set(3,4,1)
       game.map.set(4,5,1)
       game.map.set(5,3,1)
       game.map.set(5,4,1)
       game.map.set(5,5,1)

       game.map.print_map()
       print()

       game.game_cycle()

       game.map.print_map()
       print()

       new_map = GameMap(10,10)
       new_map.set(4,3,1)
       new_map.set(4,5,1)
       new_map.set(5,4,1)
       new_map.set(5,5,1)
       new_map.set(6,4,1)

       new_map.print_map()

       # 测试执行一次游戏循环后地图是否符合预期
       for i in range(0,10):
          for j in range(0,10):
              self.assertEqual(game.map.get(i,j),new_map.get(i,j),"Should get correct game_cycle()")
       
       
       

if __name__ == '__main__':
    unittest.main()
