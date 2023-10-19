import time
# 定义计时类 game_timer.py
class GameTimer(object):
    def __init__(self, trigger, interval):
        """将在主程序中初始化实例 计时器以interval秒的频率触发
        trigger是个函数，计时器被触发时调用该函数"""
        self.trigger = trigger
        self.interval = interval

    def start(self):
        """启动计时器，之后将以interval秒的间隔持续触发"""
        self.trigger()
        time.sleep(self.interval)


