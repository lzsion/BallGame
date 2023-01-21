import sys

from Initial import *
from Display import *


class BallGame:
    def __init__(self):
        self.disp = Display()
        while True:
            self.disp.serveBall()  # 发球
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # 右上关闭退出
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # 按esc退出
                        sys.exit()
                    if event.key == pygame.K_r:  # 按r重新开始
                        self.disp = Display()
                self.disp.keyEvent(event)  # 更新按键事件
            self.disp.setScreen(screen)  # 绘制屏幕
            pygame.display.flip()  # 更新
            fclock.tick(FPS)
