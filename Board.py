from tkinter import N
import pygame
import random
import math
from Const import *
class Board:
    def __init__(self,name):
        if name == 'player1':
            self.color = colorLi[1]
            self.posi = boardInitPosi[0]
            self.name = 0
        elif name == 'player2':
            self.color = colorLi[2]
            self.posi = boardInitPosi[1]
            self.name = 1
        self.size = boardSize
        self.speed = [0,0]
        self.score = 0
        # self.guessedY = []
        self.isComputer = False
    def setIsComputer(self):
        self.isComputer = True
    def getIsComputer(self):
        return self.isComputer
    # def appendGuessY(self,item):
    #     self.guessedY.append(item)
    # def removeGuessY(self,item):
    #     self.guessedY.remove(item)
    # def getGuessedY(self):
    #     return self.guessedY
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
    def boundaryJudge(self):
        if self.posi[1] + self.speed[1] < 0:#top
            self.speed = [0,0]
            return False
        elif self.posi[1] + boardY + self.speed[1] > screenSize[1]:#bottom
            self.speed = [0,0]
            return False
    def move(self):
        self.boundaryJudge()
        self.posi = (self.posi[0] , self.posi[1] + self.speed[1],boardX,boardY)

    def eventKeyUp(self):
        self.speed = [0,-boardVelo]
        self.move()
    def eventKeyDown(self):
        self.speed = [0,boardVelo]
        self.move()
    def show(self,screen):
        pygame.draw.rect(screen,self.color,self.posi,0)
    def computerEvent(self,allBallLi):
        sideBallLi = []
        sideBoardTop = self.getPosi()[1]
        sideBoardBottom = sideBoardTop + boardY
        for eachBall in allBallLi:
            guessedY = eachBall.getGuessedY()
            if guessedY[0] == self.name:
                if sideBoardTop - guessedY[2] * boardVelo > guessedY[1]: 
                    continue
                if sideBoardBottom + guessedY[2] * boardVelo < guessedY[1]:
                    continue
                sideBallLi.append(guessedY)
                # if guessedY[2] < minTick:
                #     minTick = guessedY[2]
                #     minBall = eachBall
                #     haveBall = True
        if len(sideBallLi) == 1:
            minGuessY = min(sideBallLi,key = lambda x : x[2])
            if minGuessY[1] > screenY // 2 :
                if minGuessY[1] < sideBoardBottom - precision:
                    return computerUpEvent
                elif minGuessY[1] > sideBoardBottom:
                    return computerDownEvent
                else :
                    return computerStopEvent
            elif minGuessY[1] < screenY // 2 :
                if minGuessY[1] < sideBoardTop:
                    return computerUpEvent
                elif minGuessY[1] > sideBoardTop + precision:
                    return computerDownEvent
                else :
                    return computerStopEvent
            # if minGuessY[1] < sideBoardTop:
            #     return computerUpEvent
            # elif minGuessY[1] > sideBoardBottom:
            #     return computerDownEvent
            # else :
            #     return computerStopEvent
        elif len(sideBallLi) > 1:
            sideBallLi.sort(key = lambda x : x[2])
            minGuessY = sideBallLi[0]
            secGuessY = sideBallLi[1]
            if minGuessY[1] > secGuessY[1] :
                if minGuessY[1] < sideBoardBottom - precision:
                    return computerUpEvent
                elif minGuessY[1] > sideBoardBottom:
                    return computerDownEvent
                else :
                    return computerStopEvent
            elif minGuessY[1] < secGuessY[1] :
                if minGuessY[1] < sideBoardTop:
                    return computerUpEvent
                elif minGuessY[1] > sideBoardTop + precision:
                    return computerDownEvent
                else :
                    return computerStopEvent
        else :
            if sideBoardTop + boardY // 2 > screenY // 2 + precision:
                return computerUpEvent
            elif sideBoardTop + boardY // 2 < screenY // 2 - precision:
                return computerDownEvent
        return computerStopEvent


