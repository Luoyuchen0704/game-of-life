import time
# 定义计时类：负责时间相关功能，在适当的时机触发游戏逻辑模块对地图的更新
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


