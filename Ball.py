import random
import math
from Const import *


def getRandSpeed():
    velo = random.randint(BALL_VELOCITY_RANGE[0], BALL_VELOCITY_RANGE[1])  # 随机球的速度
    x = 0  # x坐标
    y = 0  # y坐标
    while (x & y) == 0:  # 避免0速度bug 不能只有x或y轴分量
        angle = random.uniform(0, 2 * math.pi)  # 随机方向角
        x = round(velo * math.cos(angle))
        y = round(velo * math.sin(angle))
    return [x, y]  # 返回速度向量


def dotProduct(A, B):
    return [A[0] * B[0], A[1] * B[1]]


def mult(k, A):
    return [k * A[0], k * A[1]]


def minus(A, B):
    return [A[0] - B[0], A[1] - B[1]]


def plus(A, B):
    return [A[0] + B[0], A[1] + B[1]]


class Ball:
    def __init__(self):
        self.color = UNSELECTED_COLOR  # 球颜色
        self.radius = BALL_RADIUS  # 球半径
        self.posi = (SCREEN_X_SIZE // 2, SCREEN_Y_SIZE // 2)  # 球位置
        self.speed = getRandSpeed()  # 球速度
        self.guessedY = self.updateGuessY()  # 估计球的落点
        self.belongTo = NULL_NAME  # 球属于哪个player
        self.out = False  # 球是否出界

    def setBelongTo(self, name):
        self.belongTo = name

    def getBelongTo(self):
        return self.belongTo

    def setSpeed(self, speed):
        self.speed = speed

    def getSpeed(self):
        return self.speed

    def getPosi(self):
        return self.posi

    def getRadius(self):
        return self.radius

    def isOut(self):
        return self.out

    def setColor(self, color):
        self.color = color

    def getGuessedY(self):
        return self.guessedY

    def isRebound(self, board):  # 反弹判定 球的y轴在板子范围内
        return board.getPosi()[Y_AXIS] <= self.posi[Y_AXIS] <= board.getPosi()[Y_AXIS] + BOARD_Y_SIZE

    # def isTopCorner(self, board):  # 板子上顶角反弹判断
    #     return board.getPosi()[Y_AXIS] - self.radius <= self.posi[Y_AXIS] < board.getPosi()[Y_AXIS]
    #
    # def isBottomCorner(self, board):  # 板子下顶角反弹判断
    #     return board.getPosi()[Y_AXIS] + boardY < self.posi[Y_AXIS] <= board.getPosi()[Y_AXIS] + boardY + self.radius

    def getNewSpeed(self, board, rVec):
        vr = dotProduct(self.speed, rVec)
        vr = mult(1 / self.radius ** 2, vr)
        vt = minus(self.speed, vr)
        vr = mult(-1, vr)
        vr2 = dotProduct(board.getSpeed(), rVec)
        vr2 = mult(2 / (self.radius ** 2), vr2)
        newV = plus(vr, vt)
        newV = plus(newV, vr2)
        return newV

    def boundaryJudge(self, boardLi):  # 边界判断
        if self.posi[Y_AXIS] - self.radius <= 0:  # top
            self.speed[Y_AXIS] = -self.speed[Y_AXIS]  # 上边界反弹
        elif self.posi[Y_AXIS] + self.radius >= SCREEN_Y_SIZE:  # bottom
            self.speed[Y_AXIS] = -self.speed[Y_AXIS]  # 下边界反弹
        if self.posi[X_AXIS] - self.radius <= BOARD_X_SIZE:  # left
            if self.isRebound(boardLi[PLAYER_1_CODE]):  # 如果反弹
                self.speed[X_AXIS] = -self.speed[X_AXIS]
                self.color = PLAYER_1_COLOR
                self.belongTo = boardLi[PLAYER_1_CODE].getName()
                self.guessedY = self.updateGuessY()  # 更新guessY
                self.guessedY[GUESSED_Y_BELONG_TO] = PLAYER_1_CODE
            # 角反弹判断 有bug
            # elif self.isBottomCorner(boardLi[0]):
            #     rVec = [boardLi[0].getPosi()[0] + BOARD_X_SIZE - self.posi[0], boardLi[0].getPosi()[1] + boardY - self.posi[1]]
            #     if rVec[0]**2 + rVec[1]**2 == self.radius**2:
            #         newV = self.getNewSpeed(boardLi[0],rVec)
            #         self.speed = [round(newV[0]),round(newV[1])]
            #         self.color = colorLi[1]
            #         self.belongTo = boardLi[0].getName()
            # elif self.isTopCorner(boardLi[0]):
            #     rVec = [boardLi[0].getPosi()[0] + BOARD_X_SIZE - self.posi[0], boardLi[0].getPosi()[1] - self.posi[1]]
            #     if rVec[0]**2 + rVec[1]**2 == self.radius**2:
            #         newV = self.getNewSpeed(boardLi[0],rVec)
            #         self.speed = [round(newV[0]),round(newV[1])]
            #         self.color = colorLi[1]
            #         self.belongTo = boardLi[0].getName()
            else:  # 不反弹判定为出界
                self.out = True
                if self.belongTo == PLAYER_2_CODE:  # 如果为p2的球 p2加分
                    boardLi[PLAYER_2_CODE].addScore()
        elif self.posi[X_AXIS] + self.radius >= SCREEN_X_SIZE - BOARD_X_SIZE:  # right
            if self.isRebound(boardLi[PLAYER_2_CODE]):  # 如果反弹
                self.speed[X_AXIS] = -self.speed[X_AXIS]
                self.color = PLAYER_2_COLOR
                self.belongTo = boardLi[PLAYER_2_CODE].getName()
                self.guessedY = self.updateGuessY()  # 更新guessY
                self.guessedY[GUESSED_Y_BELONG_TO] = PLAYER_2_CODE
            # elif self.isBottomCorner(boardLi[1]):
            #     rVec = [boardLi[1].getPosi()[0] - self.posi[0], boardLi[1].getPosi()[1] + boardY - self.posi[1]]
            #     if rVec[0]**2 + rVec[1]**2 == self.radius**2:
            #         newV = self.getNewSpeed(boardLi[1],rVec)
            #         self.speed = [round(newV[0]),round(newV[1])]
            #         self.color = colorLi[1]
            #         self.belongTo = boardLi[1].getName()
            # elif self.isTopCorner(boardLi[1]):
            #     rVec = [boardLi[1].getPosi()[0] - self.posi[0], boardLi[1].getPosi()[1] - self.posi[1]]
            #     if rVec[0]**2 + rVec[1]**2 == self.radius**2:
            #         newV = self.getNewSpeed(boardLi[1],rVec)
            #         self.speed = [round(newV[0]),round(newV[1])]
            #         self.color = colorLi[1]
            #         self.belongTo = boardLi[1].getName()
            else:  # 不反弹判定为出界
                self.out = True
                if self.belongTo == PLAYER_1_CODE:  # 如果为p1的球 p1加分
                    boardLi[PLAYER_1_CODE].addScore()

    def show(self, screen):
        pygame.draw.circle(screen, self.color, self.posi, self.radius)
        if SHOW_GUESS_POINT:  # 如果要绘出预测落点球
            if self.guessedY[GUESSED_Y_DROP_ONTO] == PLAYER_1_CODE:  # 预计落在左边
                guessPosi = (BOARD_X_SIZE, self.guessedY[GUESSED_Y_GUESS_Y])
            elif self.guessedY[GUESSED_Y_DROP_ONTO] == PLAYER_2_CODE:  # 预计落在右边
                guessPosi = (SCREEN_X_SIZE - BOARD_X_SIZE, self.guessedY[GUESSED_Y_GUESS_Y])
            if self.guessedY[GUESSED_Y_BELONG_TO] == PLAYER_1_CODE:  # 属于p1的球
                pygame.draw.circle(screen, PLAYER_1_COLOR, guessPosi, GUESS_BALL_R)
            elif self.guessedY[GUESSED_Y_BELONG_TO] == PLAYER_2_CODE:  # 属于P2的球
                pygame.draw.circle(screen, PLAYER_2_COLOR, guessPosi, GUESS_BALL_R)
            elif self.guessedY[GUESSED_Y_BELONG_TO] == PLAYER_NULL_CODE:  # 白球
                pygame.draw.circle(screen, UNSELECTED_COLOR, guessPosi, GUESS_BALL_R)

    def move(self, boardLi):  # 球移动
        self.posi = (self.posi[X_AXIS] + self.speed[X_AXIS], self.posi[Y_AXIS] + self.speed[Y_AXIS])
        self.boundaryJudge(boardLi)  # 更新边界判断

    def updateGuessY(self):
        ballX = self.getPosi()[X_AXIS]  # 球位置
        ballY = self.getPosi()[Y_AXIS]
        ballR = self.getRadius()  # 球半径
        veloX = self.getSpeed()[X_AXIS]  # 球速度
        veloY = self.getSpeed()[Y_AXIS]
        global guessY
        if veloX > 0 and veloY > 0:  # 往右下的球
            deltaX = SCREEN_X_SIZE - BOARD_X_SIZE - ballX - ballR  # 到右边界的距离
            tick = deltaX / veloX  # 触碰到右边界的时间
            deltaY = SCREEN_Y_SIZE - ballR - ballY  # 此时与下边界的距离
            excessY = veloY * tick - deltaY  # 超出的距离
            if excessY <= 0:  # 没有碰到边界
                guessY = ballY + veloY * tick
            elif (excessY // (SCREEN_Y_SIZE - 2 * ballR)) % 2 == 0:
                # 最终在下边界反弹
                guessY = SCREEN_Y_SIZE - ballR - excessY % (SCREEN_Y_SIZE - 2 * ballR)
            elif (excessY // (SCREEN_Y_SIZE - 2 * ballR)) % 2 == 1:
                # 最终在上边界反弹
                guessY = ballR + excessY % (SCREEN_Y_SIZE - 2 * ballR)
            return [PLAYER_2_CODE, guessY, tick, PLAYER_NULL_CODE]
        elif veloX > 0 and veloY < 0:  # 往右上的球
            deltaX = SCREEN_X_SIZE - BOARD_X_SIZE - ballX - ballR  # 到右边界的距离
            tick = deltaX / veloX  # 触碰到右边界的时间
            deltaY = ballY - ballR  # 此时与上边界的距离
            excessY = -(veloY) * tick - deltaY  # 超出的距离
            if excessY < 0:  # 没有碰到边界
                guessY = ballY + veloY * tick
            elif (excessY // (SCREEN_Y_SIZE - 2 * ballR)) % 2 == 1:
                # 最终在下边界反弹
                guessY = SCREEN_Y_SIZE - ballR - excessY % (SCREEN_Y_SIZE - 2 * ballR)
            elif (excessY // (SCREEN_Y_SIZE - 2 * ballR)) % 2 == 0:
                # 最终在上边界反弹
                guessY = ballR + excessY % (SCREEN_Y_SIZE - 2 * ballR)
            return [PLAYER_2_CODE, guessY, tick, PLAYER_NULL_CODE]
        elif veloX < 0 and veloY > 0:  # 往左下的球
            deltaX = ballX - ballR - BOARD_X_SIZE  # 到左边界的距离
            tick = deltaX / (-veloX)  # 触碰到左边界的时间
            deltaY = SCREEN_Y_SIZE - ballR - ballY  # 此时与下边界的距离
            excessY = veloY * tick - deltaY  # 超出的距离
            if excessY <= 0:  # 没有碰到边界
                guessY = ballY + veloY * tick
            elif (excessY // (SCREEN_Y_SIZE - 2 * ballR)) % 2 == 0:
                # 最终在下边界反弹
                guessY = SCREEN_Y_SIZE - ballR - excessY % (SCREEN_Y_SIZE - 2 * ballR)
            elif (excessY // (SCREEN_Y_SIZE - 2 * ballR)) % 2 == 1:
                # 最终在上边界反弹
                guessY = ballR + excessY % (SCREEN_Y_SIZE - 2 * ballR)
            return [PLAYER_1_CODE, guessY, tick, PLAYER_NULL_CODE]
        elif veloX < 0 and veloY < 0:  # 往坐上的球
            deltaX = ballX - ballR - BOARD_X_SIZE  # 到左边界的距离
            tick = deltaX / (-veloX)  # 触碰到左边界的时间
            deltaY = ballY - ballR  # 此时与上边界的距离
            excessY = (-veloY) * tick - deltaX  # 超出的距离
            if excessY < 0:  # 没有碰到边界
                guessY = ballY - (-veloY) * tick
            elif (excessY // (SCREEN_Y_SIZE - 2 * ballR)) % 2 == 1:
                # 最终在下边界反弹
                guessY = SCREEN_Y_SIZE - ballR - excessY % (SCREEN_Y_SIZE - 2 * ballR)
            elif (excessY // SCREEN_Y_SIZE) % 2 == 0:
                # 最终在上边界反弹
                guessY = ballR + excessY % (SCREEN_Y_SIZE - 2 * ballR)
            return [PLAYER_1_CODE, guessY, tick, PLAYER_NULL_CODE]
