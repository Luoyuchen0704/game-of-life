# 导入unittest库、game_map模块和mock库
import unittest
import game_map
from unittest.mock import patch
from unittest.mock import MagicMock
# 创建一个继承自unittest.TestCase的测试类
class Test_TestGameMap(unittest.TestCase):
    def setUp(self):
        self.game_map = game_map.GameMap(4,3)

    def test_rows(self):
        self.assertEqual(4,self.game_map.rows,"Should get correct rows")

    def test_cols(self):
        self.assertEqual(3,self.game_map.cols,"Should get correct cols")

    @patch('game_map.random.random', MagicMock(return_value=0.25))
    def test_reset(self):
        self.game_map.reset(0.3)

        #print(self.game_map.map)

        live_cells = sum(sum(self.game_map.map, []))
        self.assertGreater(live_cells, 0)  # 检查是否有一些活细胞

        self.game_map.reset(0.2)

        #print(self.game_map.map)

        live_cells = sum(sum(self.game_map.map, []))
        self.assertEqual(live_cells, 0)  # 检查是否都是死细胞


    def test_get_set(self):
        self.assertEqual(0,self.game_map.get(0,0))
        self.game_map.set(0,0,1)
        self.assertEqual(1,self.game_map.get(0,0))

    def test_get_neighbor_count(self):
        expected_value = [[8] * 3] * 4
        for i in range(0,4):
            for j in range(0,3):
                self.game_map.set(i,j,1)
        for i in range(0,4):
            for j in range(0,3):
                self.assertEqual(expected_value[i][j],(self.game_map.get_neighbor_count(i,j)),'(%d %d)' % (i,j))



if __name__ == '__main__':
    unittest.main()