# 导入unittest库、game_map模块和mock库
import unittest
import game_map
from unittest.mock import patch
from unittest.mock import MagicMock
# 单元测试
# 1. 通过所有被测模块的数据流
# 2. 数据结构的定义和使用
# 3. 边界条件
# 4. 计算错误、判定错误、控制流错误
# 5. 可能引发错误处理的路径以及进行错误处理的路径
# Mock测试：对于不容易构造或者不容易获取的对象
# 断言方法 assert_called_with,assert_called_once_with等
# 行为控制 返回值 return_value:固定返回值 side_effects:返回值的序列或自定义方法
# Python单元测试之unittest 属性断言 assertTrue assertFalse assertEqual等
# coverage.py统计代码覆盖率
# 创建一个继承自unittest.TestCase的测试类
class Test_TestGameMap(unittest.TestCase):
    def setUp(self):
        self.game_map = game_map.GameMap(4, 3)

    def test_rows(self):
        self.assertEqual(4, self.game_map.rows, "Should get correct rows")

    def test_cols(self):
        self.assertEqual(3, self.game_map.cols, "Should get correct cols")

    @patch('game_map.random.random', MagicMock(side_effect = [0.1, 0.5, 0.6, 0.2, 0.7, 0.8, 0.3, 0.51, 0.65, 0.13, 0.56, 0.78]))
    def test_reset(self):
        self.game_map.reset(0.33)
        for i in range(0, 4):
            self.assertEqual(1, self.game_map.get(i, 0))
            for j in range(1, 3):
                self.assertEqual(0, self.game_map.get(i,j))

    def test_get_set(self):
        self.assertEqual(0, self.game_map.get(0, 0))
        self.game_map.set(0, 0, 1)
        self.assertEqual(1, self.game_map.get(0, 0))

    def test_get_neighbor_count(self):
        expected_value = [[8] * 3] * 4
        for i in range(0, 4):
            for j in range(0, 3):
                self.game_map.set(i, j, 1)
        for i in range(0, 4):
            for j in range(0, 3):
                self.assertEqual(expected_value[i][j],(self.game_map.get_neighbor_count(i, j)),'(%d %d)' % (i,j))



if __name__ == '__main__':
    unittest.main()