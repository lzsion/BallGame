from Ball import *
from Board import * 
from Key import * 
import time
import pygame
class Display:
    def __init__(self):
        self.ballLi = []    #小球列表
        self.BallVelo = 6
        self.boardLi = [Board('player1'),Board('player2')]  #玩家移动的板       
        for eachCP in computerPlayer:   #设置玩家为电脑
            self.boardLi[eachCP].setIsComputer()
        # ballLi.append(Ball(velo//3))
        # for i in range(ballNum):
        #     ballLi.append(Ball())
        self.upKey1 = Key()     #p1向上
        self.downKey1 = Key()   #p1向下
        self.upKey2 = Key()     #p2向上
        self.downKey2 = Key()   #p2向下
        self.start = False  #游戏阶段
        self.countDown = False  #准备阶段开始倒计时
        self.finished = False   #游戏结束
        self.serveTime = time.time()    #上一次发球时间
        self.startTime = time.time()    #游戏开始时间
        self.timeLast = maxTime     #剩余时间
        # self.textP1 = 'P1: {:^3d}'.format(self.boardLi[0].getScore())
        # self.textP2 = 'P2: {:^3d}'.format(self.boardLi[1].getScore())
        # self.timeText = '{:^3d}'.format(self.timeLast)
        self.timeCountText = '3'
    def begin(self):    #按空格开始后打开倒计时开关
        self.countDown = True
        self.startTime = time.time()
    def isStart(self):
        return self.start
    def intervaled(self):   #时间过了intervalTime秒
        return time.time() - self.serveTime >= intervalTime
    def setServeTime(self):
        self.serveTime = time.time()
    def getTime(self):
        return self.time
    def serveBall(self):    #发球
        self.timeCounter()  #更新倒计时
        if self.countDown:  #在准备倒计时阶段
            self.timeCountDown()    #准备倒计时
        if self.start and self.intervaled():    #发球
            if len(self.ballLi) < maxBallNum:   #场上球数小于最大球数
                # addBall = Ball()
                self.ballLi.append(Ball())  #加一个球
                # self.boardLi[addBall.getGuessedY()[0]].appendGuessY(addBall.getGuessedY())
                self.setServeTime() #更新发球时间
    def timeCounter(self):
        if self.start and int(time.time() - self.startTime) >= maxTime - self.timeLast + 1:
            self.timeLast -= 1
            if self.timeLast == 0:
                self.finished = True
    def timeCountDown(self):
        if time.time() - self.startTime >= 1:
            self.timeCountText = '2'    #准备倒计时
        if time.time() - self.startTime >= 2:
            self.timeCountText = '1'    #准备倒计时
            self.setServeTime()     #更新发球时间
        if time.time() - self.startTime >= 3:   #准备倒计时结束
            self.countDown = False  #标记准备倒计时结束
            self.start = True   #标记游戏开始
            self.startTime = time.time()    #记录开始时间
    def keyEvent(self,event):#按键事件 防止同时按下两个方向的bug 记录下按键的按下和松开状态
        if event.type == pygame.KEYDOWN:
            if self.start and not self.finished:    #游戏进行过程
                if event.key == pygame.K_w:
                    self.upKey1.downEvent()     #w键按下 反映为p1的上
                if event.key == pygame.K_s:
                    self.downKey1.downEvent()   #s键按下 反映为p1的下
                if event.key == pygame.K_UP:
                    self.upKey2.downEvent()     #上键按下 反映为p2的上
                if event.key == pygame.K_DOWN:
                    self.downKey2.downEvent()   #下键按下 反映为p2的下
            if event.key == pygame.K_SPACE and self.countDown == False and self.start == False and self.finished == False:
                self.begin()    #空格键开始
        if event.type == pygame.KEYUP:
            if self.start and not self.finished:    #游戏进行过程
                if event.key == pygame.K_w:
                    self.upKey1.upEvent()       #w键松开 p1停止向上
                if event.key == pygame.K_s:
                    self.downKey1.upEvent()     #s键松开 p1停止向下
                if event.key == pygame.K_UP:
                    self.upKey2.upEvent()       #上键松开 p2停止向上
                if event.key == pygame.K_DOWN:
                    self.downKey2.upEvent()     #下键松开 p2停止向下
    def setScreen(self,screen):
        screen.fill((0,0,0))    #黑色背景
        if self.finished == False:
            pygame.draw.rect(screen,colorLi[4],boundaryPosi[0],0)   #灰色轨道条
            pygame.draw.rect(screen,colorLi[4],boundaryPosi[1],0)
        if self.start and not self.finished:    #游戏进行过程
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


