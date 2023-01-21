from Const import *
from Key import *


class Board:
    def __init__(self, name):
        if name == PLAYER_1_NAME:
            self.color = PLAYER_1_COLOR
            self.posi = BOARD_LEFT_POSI
            self.name = PLAYER_1_CODE
        elif name == PLAYER_2_NAME:
            self.color = PLAYER_2_COLOR
            self.posi = BOARD_RIGHT_POSI
            self.name = PLAYER_2_CODE
        self.speed = [0, 0]  # 板子移动速度
        self.score = 0  # 得分
        self.upKey = Key()
        self.downKey = Key()
        self.isComputer = False  # 是否为电脑

    def setIsComputer(self, isComputer):
        self.isComputer = isComputer

    def getIsComputer(self):
        return self.isComputer

    def getPosi(self):
        return self.posi

    def getName(self):
        return self.name

    def getSpeed(self):
        return self.speed

    def addScore(self):
        self.score += 1

    def getScore(self):
        return self.score

    def boundaryJudge(self):  # 边界判定
        if self.posi[Y_AXIS] + self.speed[Y_AXIS] < 0:  # 上边界
            self.speed = [0, 0]
        elif self.posi[Y_AXIS] + BOARD_Y_SIZE + self.speed[Y_AXIS] > SCREEN_Y_SIZE:  # 下边界
            self.speed = [0, 0]

    def move(self):  # 移动
        self.boundaryJudge()  # 判断边界
        self.posi = (self.posi[X_AXIS], self.posi[Y_AXIS] + self.speed[Y_AXIS])  # 更新位置

    def eventKeyUp(self):  # 向上事件
        self.speed = [0, -BOARD_VELOCITY]  # 设定速度
        self.move()  # 移动

    def eventKeyDown(self):  # 向下事件
        self.speed = [0, BOARD_VELOCITY]  # 设定速度
        self.move()  # 移动

    def show(self, screen):  # 显示屏幕
        rect = (self.posi[X_AXIS], self.posi[Y_AXIS], BOARD_X_SIZE, BOARD_Y_SIZE)
        pygame.draw.rect(screen, self.color, rect, 0)

    def computerEvent(self, allBallLi):  # 电脑分析
        sideBallLi = []  # 可以接到的球
        sideBoardTop = self.getPosi()[Y_AXIS]  # 板子上边界
        sideBoardBottom = sideBoardTop + BOARD_Y_SIZE  # 板子下边界
        for eachBall in allBallLi:  # 遍历所有球
            guessedY = eachBall.getGuessedY()
            if guessedY[GUESSED_Y_DROP_ONTO] == self.name:  # 如果球预计落点为该板一侧
                if sideBoardTop - guessedY[GUESSED_Y_TICK] * BOARD_VELOCITY > guessedY[GUESSED_Y_GUESS_Y]:
                    # 板子现在往上也来不及
                    continue
                if sideBoardBottom + guessedY[GUESSED_Y_TICK] * BOARD_VELOCITY < guessedY[GUESSED_Y_GUESS_Y]:
                    # 板子现在往下也来不及
                    continue
                sideBallLi.append(guessedY)
        if len(sideBallLi) == 1:  # 如果只有一个可以接到的球
            minGuessY = min(sideBallLi, key=lambda x: x[GUESSED_Y_TICK])  # 下一个到达的球
            if minGuessY[GUESSED_Y_GUESS_Y] > SCREEN_Y_SIZE // 2:  # 预计落点在下半屏幕
                if minGuessY[GUESSED_Y_GUESS_Y] < sideBoardBottom - COMPUTER_CATCH_PRECISION:
                    # 往上走 (尽量用板子下半部接球)
                    return COMPUTER_UP_EVENT
                elif minGuessY[GUESSED_Y_GUESS_Y] > sideBoardBottom:
                    # 往下走
                    return COMPUTER_DOWN_EVENT
                else:
                    return COMPUTER_STOP_EVENT
            elif minGuessY[GUESSED_Y_GUESS_Y] < SCREEN_Y_SIZE // 2:  # 预计落点在上半屏幕
                if minGuessY[GUESSED_Y_GUESS_Y] < sideBoardTop:
                    # 往上走
                    return COMPUTER_UP_EVENT
                elif minGuessY[GUESSED_Y_GUESS_Y] > sideBoardTop + COMPUTER_CATCH_PRECISION:
                    # 往下走 (尽量用板子上半部接球)
                    return COMPUTER_DOWN_EVENT
                else:
                    return COMPUTER_STOP_EVENT
        elif len(sideBallLi) > 1:  # 多于一个可以接到的球
            # sideBallLi.sort(key = lambda x : x[GUESSED_Y_TICK])            
            sideBallLi.sort(key=lambda x: (x[GUESSED_Y_BELONG_TO], x[GUESSED_Y_TICK]))  # 先接属于对方的球
            firstGuessY = sideBallLi[0]
            secGuessY = sideBallLi[1]
            if firstGuessY[GUESSED_Y_GUESS_Y] > secGuessY[GUESSED_Y_GUESS_Y]:  # 如果第一个球在第二个球下面
                if firstGuessY[GUESSED_Y_GUESS_Y] < sideBoardBottom - COMPUTER_CATCH_PRECISION:
                    # 往上走 (尽量用板子下半部接球)
                    return COMPUTER_UP_EVENT
                elif firstGuessY[GUESSED_Y_GUESS_Y] > sideBoardBottom:
                    # 往下走
                    return COMPUTER_DOWN_EVENT
                else:
                    return COMPUTER_STOP_EVENT
            elif firstGuessY[GUESSED_Y_GUESS_Y] < secGuessY[GUESSED_Y_GUESS_Y]:  # 如果第一个球在第二个球上面
                if firstGuessY[GUESSED_Y_GUESS_Y] < sideBoardTop:
                    # 往上走
                    return COMPUTER_UP_EVENT
                elif firstGuessY[GUESSED_Y_GUESS_Y] > sideBoardTop + COMPUTER_CATCH_PRECISION:
                    # 往下走 (尽量用板子上半部接球)
                    return COMPUTER_DOWN_EVENT
                else:
                    return COMPUTER_STOP_EVENT
        else:  # 没有到这边的球 让板子在中间
            if sideBoardTop + BOARD_Y_SIZE // 2 > SCREEN_Y_SIZE // 2 + COMPUTER_CATCH_PRECISION:
                # 往上走
                return COMPUTER_UP_EVENT
            elif sideBoardTop + BOARD_Y_SIZE // 2 < SCREEN_Y_SIZE // 2 - COMPUTER_CATCH_PRECISION:
                # 往下走
                return COMPUTER_DOWN_EVENT
        return COMPUTER_STOP_EVENT
