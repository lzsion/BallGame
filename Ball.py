import pygame
import random
import math
from Const import *
def getRandSpeed():
    velo = random.randint(ballVeloRange[0],ballVeloRange[1])
    x = velo
    y = 0
    while x & y == 0:
        angle = random.uniform(0, 2 * math.pi)
        x = round(velo * math.cos(angle))
        y = round(velo * math.sin(angle))
    return [x,y]
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
        self.color = colorLi[0]
        self.radius = circleRadius
        self.posi = screenMid
        self.speed = getRandSpeed()
        self.guessedY = self.updateGuessY()
        self.belongTo = initName
        self.out = False
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
    def isRebound(self,board):
        return self.posi[1] >= board.getPosi()[1] and self.posi[1] <= board.getPosi()[1] + boardY
    def isTopCorner(self,board):
        return self.posi[1] >= board.getPosi()[1] - self.radius and self.posi[1] < board.getPosi()[1]
    def isBottomCorner(self,board):
        return self.posi[1] > board.getPosi()[1] + boardY and self.posi[1] <= board.getPosi()[1] + boardY + self.radius
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
    def boundaryJudge(self,boardLi):
        if self.posi[1] - self.radius <= 0:#top
            self.speed[1] = -self.speed[1]
        elif self.posi[1] + self.radius >= screenSize[1]:#bottom
            self.speed[1] = -self.speed[1]
        if self.posi[0] - self.radius <= boardX:#left
            if self.isRebound(boardLi[0]):
                self.speed[0] = -self.speed[0]
                self.color = colorLi[1]
                self.belongTo = boardLi[0].getName()
                self.guessedY = self.updateGuessY()
                self.guessedY[3] = 1
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
            else :
                self.out = True
                if self.belongTo == 1 :
                    boardLi[1].addScore()
        elif self.posi[0] + self.radius >= screenSize[0] - boardX:#right
            if self.isRebound(boardLi[1]):
                self.speed[0] = -self.speed[0]
                self.color = colorLi[2]
                self.belongTo = boardLi[1].getName()
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
            else :
                self.out = True
                if self.belongTo == 0 :
                    boardLi[0].addScore()
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
            
