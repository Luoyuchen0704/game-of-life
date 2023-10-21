import unittest
from unittest.mock import MagicMock
from life_game import LifeGame


class Test_TestLifeGame(unittest.TestCase):
    def setUp(self):
        self.game = LifeGame(map_rows=5, map_cols=5, life_init_ratio=0.0)

    def test_game_cycle(self):
        self.game.map.set(0, 3, 1)
        self.game.map.set(1, 1, 1)
        self.game.map.set(1, 3, 1)
        self.game.map.set(2, 2, 1)
        self.game.map.set(2, 3, 1)
        self.assertEqual(self.game.map.compare_map([[0, 0, 0, 1, 0],
                                                    [0, 1, 0, 1, 0],
                                                    [0, 0, 1, 1, 0],
                                                    [0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0]]), 1)
        self.game.game_cycle()

        self.assertEqual(self.game.map.compare_map([[0, 0, 1, 0, 0],
                                                    [0, 0, 0, 1, 1],
                                                    [0, 0, 1, 1, 0],
                                                    [0, 0, 0, 0, 0],
                                                    [0, 0, 0, 0, 0]]), 1)
       
if __name__ == '__main__':
    unittest.main()
