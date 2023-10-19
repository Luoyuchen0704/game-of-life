import game_timer
import game_ui
import life_game

# 测试
if __name__ == '__main__':
    # 地图行数
    rows = 100
    # 地图列数
    cols = 100
    # 初始细胞存活率
    life_init_ratio = 0.1
    # 更新间隔
    interval = 0.1
    # 地图细胞边长
    a = 10

    """传入参数依次为地图行数，列数以及初始活细胞存活率"""
    game = life_game.LifeGame(rows, cols, life_init_ratio)
    """传入参数依次为循环一次游戏，更新间隔"""
    timer = game_timer.GameTimer(game.game_cycle,interval)
    """UI绘制"""
    ui = game_ui.GameUI(game,timer,10 * rows,10 * cols,a)
    """运行UI界面,传入参数为地图细胞边长"""
    ui.run()