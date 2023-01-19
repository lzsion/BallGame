import pygame
import random
import math
from Const import *
def getRandSpeed():
    velo = random.randint(ballVeloRange[0],ballVeloRange[1])    #随机球的速度
    x = 0   #x坐标
    y = 0   #y坐标
    while (x & y) == 0:   #避免0速度bug 不能只有x或y轴分量
        angle = random.uniform(0, 2 * math.pi)  #随机方向角
        x = round(velo * math.cos(angle))
        y = round(velo * math.sin(angle))
    return [x,y]    #返回速度向量
def dotProduct(A,B):
    return [A[0] * B[0],A[1] * B[1]]
def mult(k,A) :
    return [k * A[0],k * A[1]]
def minus(A,B) :
    return[A[0] - B[0],A[1] - B[1]]
def plus(A,B) :
    return[A[0] + B[0],A[1] + B[1]]

class Ball():
    def __init__(self):
        self.color = UNSELECTED_COLOR   #球颜色
        self.radius = BALL_RADIUS       #球半径
        self.posi = SCREEN_MID_POSI     #球位置
        self.speed = getRandSpeed()     #球速度
        self.guessedY = self.updateGuessY()
        self.belongTo = NULL_NAME    #球属于哪个player
        self.out = False    #球是否出界
    def setBelongTo(self,name):
        self.belongTo = name
    def getBelongTo(self):
        return self.belongTo
    def setSpeed(self,speed):
        self.speed = speed
    def getSpeed(self):
        return self.speed
    def getPosi(self):
        return self.posi
    def isOut(self):
        return self.out
    def setColor(self,color):
        self.color = color
    def getGuessedY(self):
        return self.guessedY
    def isRebound(self,board):  #反弹判定 球的y轴在板子范围内
        return self.posi[Y_AXIS] >= board.getPosi()[Y_AXIS] and self.posi[Y_AXIS] <= board.getPosi()[Y_AXIS] + BOARD_Y_SIZE
    # def isTopCorner(self,board):  #板子上顶角反弹判断
    #     return self.posi[Y_AXIS] >= board.getPosi()[Y_AXIS] - self.radius and self.posi[Y_AXIS] < board.getPosi()[Y_AXIS]
    # def isBottomCorner(self,board):   #板子下顶角反弹判断
    #     return self.posi[Y_AXIS] > board.getPosi()[Y_AXIS] + boardY and self.posi[Y_AXIS] <= board.getPosi()[Y_AXIS] + boardY + self.radius
    def getNewSpeed(self,board,rVec):
        vr = dotProduct(self.speed,rVec)
        vr = mult(1/self.radius**2,vr)
        vt = minus(self.speed,vr)
        vr = mult(-1,vr)
        vr2 = dotProduct(board.getSpeed(),rVec)
        vr2 = mult(2/(self.radius**2),vr2)
        newV = plus(vr,vt)
        newV = plus(newV,vr2)
        return newV
    def boundaryJudge(self,boardLi):    #边界判断
        if self.posi[Y_AXIS] - self.radius <= 0: #top
            self.speed[Y_AXIS] = -self.speed[Y_AXIS]  #上边界反弹
        elif self.posi[Y_AXIS] + self.radius >= SCREEN_Y_SIZE:   #bottom
            self.speed[Y_AXIS] = -self.speed[Y_AXIS]  #下边界反弹
        if self.posi[X_AXIS] - self.radius <= BOARD_X_SIZE:    #left
            if self.isRebound(boardLi[PLAYER_1_CODE]):  #如果反弹
                self.speed[X_AXIS] = -self.speed[X_AXIS]
                self.color = PLAYER_1_COLOR
                self.belongTo = boardLi[PLAYER_1_CODE].getName()
                self.guessedY = self.updateGuessY()
                self.guessedY[3] = 1
            #角反弹判断 有bug
            # elif self.isBottomCorner(boardLi[0]):
            #     rVec = [boardLi[0].getPosi()[0] + boardX - self.posi[0], boardLi[0].getPosi()[1] + boardY - self.posi[1]]
            #     if rVec[0]**2 + rVec[1]**2 == self.radius**2:
            #         newV = self.getNewSpeed(boardLi[0],rVec)
            #         self.speed = [round(newV[0]),round(newV[1])]
            #         self.color = colorLi[1]
            #         self.belongTo = boardLi[0].getName()
            # elif self.isTopCorner(boardLi[0]):
            #     rVec = [boardLi[0].getPosi()[0] + boardX - self.posi[0], boardLi[0].getPosi()[1] - self.posi[1]]
            #     if rVec[0]**2 + rVec[1]**2 == self.radius**2:
            #         newV = self.getNewSpeed(boardLi[0],rVec)
            #         self.speed = [round(newV[0]),round(newV[1])]
            #         self.color = colorLi[1]
            #         self.belongTo = boardLi[0].getName()
            else :  #不反弹判定为出界
                self.out = True
                if self.belongTo == PLAYER_2_CODE :     #如果为p2的球 p2加分
                    boardLi[PLAYER_2_CODE].addScore()
        elif self.posi[X_AXIS] + self.radius >= SCREEN_X_SIZE - BOARD_X_SIZE:  #right
            if self.isRebound(boardLi[PLAYER_2_CODE]):  #如果反弹
                self.speed[0] = -self.speed[0]
                self.color = PLAYER_2_COLOR
                self.belongTo = boardLi[PLAYER_2_CODE].getName()
                self.guessedY = self.updateGuessY()
                self.guessedY[3] = 2
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
            else :  #不反弹判定为出界
                self.out = True
                if self.belongTo == PLAYER_1_CODE :     #如果为p1的球 p1加分
                    boardLi[PLAYER_1_CODE].addScore()
    def show(self,screen):
        pygame.draw.circle(screen,self.color,self.posi,self.radius)
        if self.guessedY[0] == 0:
            guessPosi = (boardX,self.guessedY[1])
            if showGuessPoint:
                pygame.draw.circle(screen,colorLi[self.guessedY[3]],guessPosi,guessRedius)
        elif self.guessedY[0] == 1:
            guessPosi = (screenX - boardX,self.guessedY[1])
            if showGuessPoint:
                pygame.draw.circle(screen,colorLi[self.guessedY[3]],guessPosi,guessRedius)
    def move(self,boardLi):
        self.boundaryJudge(boardLi)
        self.posi = (self.posi[0] + self.speed[0] , self.posi[1] + self.speed[1])
    def updateGuessY(self):
        ballX = self.getPosi()[0]
        ballY = self.getPosi()[1]
        ballR = circleRadius
        veloX = self.getSpeed()[0]
        veloY = self.getSpeed()[1]
        global guessY
        if veloX > 0 and veloY > 0:
            tick = (screenX - boardX - ballX - ballR) / veloX
            detaY = veloY * tick - (screenY - ballR - ballY)
            if detaY <= 0:
                guessY = ballY + veloY * tick
            elif (detaY // (screenY - 2 * ballR)) % 2 == 0:
                guessY = screenY - ballR - detaY % (screenY - 2 * ballR)
            elif (detaY // (screenY - 2 * ballR)) % 2 == 1:
                guessY = ballR + detaY % (screenY - 2 * ballR)
            return [1,guessY,tick,0]
        elif veloX > 0 and veloY < 0:
            tick = (screenX - boardX - ballX - ballR) / veloX
            detaY = (-veloY) * tick - (ballY - ballR)
            if detaY < 0:
                guessY = ballY - (-veloY) * tick
            elif (detaY // (screenY - 2 * ballR)) % 2 == 1:
                guessY = screenY - ballR - detaY % (screenY - 2 * ballR)
            elif (detaY // screenY) % 2 == 0:
                guessY = ballR + detaY % (screenY - 2 * ballR)
            return [1,guessY,tick,0]
        elif veloX < 0 and veloY > 0:
            tick = (ballX - boardX - ballR) / (-veloX)
            detaY = veloY * tick - (screenY - ballR - ballY)
            if detaY <= 0:
                guessY = ballY + veloY * tick
            elif (detaY // (screenY - 2 * ballR)) % 2 == 0:
                guessY = screenY - ballR - detaY % (screenY - 2 * ballR)
            elif (detaY // (screenY - 2 * ballR)) % 2 == 1:
                guessY = ballR + detaY % (screenY - 2 * ballR)
            return [0,guessY,tick,0]
        elif veloX < 0 and veloY < 0:
            tick = (ballX - boardX - ballR) / (-veloX)
            detaY = (-veloY) * tick - (ballY - ballR)
            if detaY < 0:
                guessY = ballY - (-veloY) * tick
            elif (detaY // (screenY - 2 * ballR)) % 2 == 1:
                guessY = screenY - ballR - detaY % (screenY - 2 * ballR)
            elif (detaY // screenY) % 2 == 0:
                guessY = ballR + detaY % (screenY - 2 * ballR)
            return [0,guessY,tick,0]
            
