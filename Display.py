from Ball import *
from Board import * 
from Key import * 
import time
import pygame
class Display:
    def __init__(self):
        self.ballLi = []
        self.BallVelo = 6
        self.boardLi = [Board('player1'),Board('player2')]
        for eachCP in computerPlayer:
            self.boardLi[eachCP].setIsComputer()
        # ballLi.append(Ball(velo//3))
        # for i in range(ballNum):
        #     ballLi.append(Ball())
        self.upKey1 = Key()
        self.downKey1 = Key()
        self.upKey2 = Key()
        self.downKey2 = Key()
        self.start = False
        self.countDown = False
        self.finished = False
        self.serveTime = time.time()
        self.startTime = time.time()
        self.timeLast = maxTime
        # self.textP1 = 'P1: {:^3d}'.format(self.boardLi[0].getScore())
        # self.textP2 = 'P2: {:^3d}'.format(self.boardLi[1].getScore())
        # self.timeText = '{:^3d}'.format(self.timeLast)
        self.timeCountText = '3'
    def begin(self):
        self.countDown = True
        self.startTime = time.time()
    def isStart(self):
        return self.start
    def intervaled(self):
        return time.time() - self.serveTime >= intervalTime
    def setServeTime(self):
        self.serveTime = time.time()
    def getTime(self):
        return self.time
    def serveBall(self):
        self.timeCounter()
        if self.countDown:
            self.timeCountDown()
        if self.start and self.intervaled():
            if len(self.ballLi) < maxBallNum:
                # addBall = Ball()
                self.ballLi.append(Ball())
                # self.boardLi[addBall.getGuessedY()[0]].appendGuessY(addBall.getGuessedY())
                self.setServeTime()
    def timeCounter(self):
        if self.start and int(time.time() - self.startTime) >= maxTime - self.timeLast + 1:
            self.timeLast -= 1
            if self.timeLast == 0:
                self.finished = True
    def timeCountDown(self):
        if time.time() - self.startTime >= 1:
            self.timeCountText = '2'
        if time.time() - self.startTime >= 2:
            self.timeCountText = '1'
            self.setServeTime()
        if time.time() - self.startTime >= 3:
            self.countDown = False
            self.start = True
            self.startTime = time.time()
    def keyEvent(self,event):
        if event.type == pygame.KEYDOWN:
            if self.start and not self.finished:
                if event.key == pygame.K_w:
                    self.upKey1.downEvent()
                if event.key == pygame.K_s:
                    self.downKey1.downEvent()
                if event.key == pygame.K_UP:
                    self.upKey2.downEvent()
                if event.key == pygame.K_DOWN:
                    self.downKey2.downEvent()
            if event.key == pygame.K_SPACE and self.countDown == False and self.start == False and self.finished == False:
                self.begin()
        if event.type == pygame.KEYUP:
            if self.start and not self.finished:
                if event.key == pygame.K_w:
                    self.upKey1.upEvent()
                if event.key == pygame.K_s:
                    self.downKey1.upEvent()
                if event.key == pygame.K_UP:
                    self.upKey2.upEvent()
                if event.key == pygame.K_DOWN:
                    self.downKey2.upEvent()
    def setScreen(self,screen):
        screen.fill((0,0,0))
        if self.finished == False:
            pygame.draw.rect(screen,colorLi[4],boundaryPosi[0],0)
            pygame.draw.rect(screen,colorLi[4],boundaryPosi[1],0)
        if self.start and not self.finished:
            for eachBall in self.ballLi:
                if eachBall.isOut():
                    self.ballLi.remove(eachBall)
                    continue
                eachBall.move(self.boardLi)
                eachBall.show(screen)
        if not self.boardLi[0].getIsComputer():
            if self.upKey1.isDown() and self.downKey1.isUp():
                self.boardLi[0].eventKeyUp()
            elif self.downKey1.isDown() and self.upKey1.isUp():
                self.boardLi[0].eventKeyDown()
        elif self.start and not self.finished :
            if self.boardLi[0].computerEvent(self.ballLi) == computerUpEvent:
                self.boardLi[0].eventKeyUp()
            elif self.boardLi[0].computerEvent(self.ballLi) == computerDownEvent:
                self.boardLi[0].eventKeyDown()
        if not self.boardLi[1].getIsComputer():
            if self.upKey2.isDown() and self.downKey2.isUp():
                self.boardLi[1].eventKeyUp()
            elif self.downKey2.isDown() and self.upKey2.isUp():
                self.boardLi[1].eventKeyDown()
        elif self.start and not self.finished :
            if self.boardLi[1].computerEvent(self.ballLi) == computerUpEvent:
                self.boardLi[1].eventKeyUp()
            elif self.boardLi[1].computerEvent(self.ballLi) == computerDownEvent:
                self.boardLi[1].eventKeyDown()
        if self.finished == False:
            for eachBoard in self.boardLi:
                eachBoard.show(screen)
        if self.start == False and self.countDown == False and self.finished == False:
            for i in range(4):
                screen.blit(preTextSurf[i],preTextPosi[i])
        elif self.start == False and self.countDown == True and self.finished == False:
            countTextSurf = font_3.render(self.timeCountText,True,colorLi[0])
            screen.blit(countTextSurf,(screenX//2 - 40,screenY//2 - 40))
        if self.start == True and self.finished == False:
            textP1 = 'P1: {:^3d}'.format(self.boardLi[0].getScore())
            textP2 = 'P2: {:^3d}'.format(self.boardLi[1].getScore())
            timeText = '{:^3d}'.format(self.timeLast)
            textSurf1 = font_1.render(textP1,True,colorLi[1])
            textSurf2 = font_1.render(textP2,True,colorLi[2])
            timeTextSurf = font_1.render(timeText,True,colorLi[0])
            screen.blit(textSurf1,(screenX//2 - 100,0))
            screen.blit(textSurf2,(screenX//2 + 50 ,0))
            screen.blit(timeTextSurf,(screenX//2 -10,0))
        elif self.finished == True:
            textP1 = 'P1: {:^3d}'.format(self.boardLi[0].getScore())
            textP2 = 'P2: {:^3d}'.format(self.boardLi[1].getScore())
            textSurf1 = font_2.render(textP1,True,colorLi[1])
            textSurf2 = font_2.render(textP2,True,colorLi[2])
            if self.boardLi[0].getScore() > self.boardLi[1].getScore():
                winSurf = font_2.render(winText,True,colorLi[3])
                winPosi = (screenX//2 - 170,screenY//2 - 80)
            elif self.boardLi[0].getScore() < self.boardLi[1].getScore():
                winSurf = font_2.render(winText,True,colorLi[3])
                winPosi = (screenX//2 + 80,screenY//2 - 80)
            else :
                winSurf = font_2.render(drawText,True,colorLi[0])
                winPosi = (screenX//2 - 30,screenY//2 - 100)
            screen.blit(textSurf1,(screenX//2 -150,screenY//2 - 20))
            screen.blit(textSurf2,(screenX//2 +100,screenY//2 - 20))
            screen.blit(winSurf,winPosi)
            screen.blit(preTextSurf[3],preTextPosi[3])
            screen.blit(preTextSurf[4],preTextPosi[4])
            screen.blit(preTextSurf[5],preTextPosi[5])


