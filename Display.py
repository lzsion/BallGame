from Ball import *
from Board import *
from SelectPlayer import *
import time
import pygame


class Display:
    def __init__(self):
        self.ballLi = []  # 小球列表
        self.BallVelo = 6
        self.boardLi = [Board(PLAYER_1_NAME), Board(PLAYER_2_NAME)]  # 玩家移动的板
        self.selectLi = [SelectPlayer(PLAYER_1_NAME), SelectPlayer(PLAYER_2_NAME)]
        self.start = False  # 游戏阶段开始
        self.countDown = False  # 准备阶段开始倒计时
        self.finished = False  # 游戏结束
        self.serveTime = time.time()  # 上一次发球时间
        self.startTime = time.time()  # 游戏开始时间
        self.timeLast = MAX_TIME  # 剩余时间
        self.timeCountText = '3'

    def begin(self):  # 按空格开始后打开倒计时开关
        self.countDown = True
        self.startTime = time.time()
        # 更新选择了电脑还是玩家
        self.boardLi[PLAYER_1_CODE].setIsComputer(self.selectLi[PLAYER_1_CODE].isSelectComputer())
        self.boardLi[PLAYER_2_CODE].setIsComputer(self.selectLi[PLAYER_2_CODE].isSelectComputer())

    def isStart(self):
        return self.start

    def intervaled(self):  # 时间过了intervalTime秒
        return time.time() - self.serveTime >= SERVE_INTERVAL_TIME

    def setServeTime(self):
        self.serveTime = time.time()

    def serveBall(self):  # 发球
        self.timeCounter()  # 更新倒计时
        if self.countDown:  # 在准备倒计时阶段
            self.timeCountDown()  # 准备倒计时
        if self.start and self.intervaled():  # 发球
            if len(self.ballLi) < MAX_BALL_NUM:  # 场上球数小于最大球数
                self.ballLi.append(Ball())  # 加一个球
                self.setServeTime()  # 更新发球时间

    def timeCounter(self):  # 更新剩余时间
        if self.start and int(time.time() - self.startTime) >= MAX_TIME - self.timeLast + 1:
            self.timeLast -= 1
            if self.timeLast == 0:  # 剩余时间为0 游戏结束
                self.finished = True

    def timeCountDown(self):
        if time.time() - self.startTime >= 1:
            self.timeCountText = '2'  # 准备倒计时
        if time.time() - self.startTime >= 2:
            self.timeCountText = '1'  # 准备倒计时
            self.setServeTime()  # 更新发球时间
        if time.time() - self.startTime >= 3:  # 准备倒计时结束
            self.countDown = False  # 标记准备倒计时结束
            self.start = True  # 标记游戏开始
            self.startTime = time.time()  # 记录开始时间

    def keyEvent(self, event):  # 按键事件 防止同时按下两个方向的bug 记录下按键的按下和松开状态
        if event.type == pygame.KEYDOWN:
            if self.start and not self.finished:  # 游戏进行过程
                if event.key == pygame.K_w:
                    self.boardLi[PLAYER_1_CODE].upKey.downEvent()  # w键按下
                if event.key == pygame.K_s:
                    self.boardLi[PLAYER_1_CODE].downKey.downEvent()  # s键按下
                if event.key == pygame.K_UP:
                    self.boardLi[PLAYER_2_CODE].upKey.downEvent()  # 上键按下
                if event.key == pygame.K_DOWN:
                    self.boardLi[PLAYER_2_CODE].downKey.downEvent()  # 下键按下
            if self.countDown == False and self.start == False and self.finished == False:  # 开始界面
                if event.key == pygame.K_SPACE:
                    self.begin()  # 空格键开始
                else:
                    if event.key == pygame.K_w:
                        self.selectLi[PLAYER_1_CODE].upKey.downEvent()
                    if event.key == pygame.K_s:
                        self.selectLi[PLAYER_1_CODE].downKey.downEvent()
                    if event.key == pygame.K_UP:
                        self.selectLi[PLAYER_2_CODE].upKey.downEvent()
                    if event.key == pygame.K_DOWN:
                        self.selectLi[PLAYER_2_CODE].downKey.downEvent()
        if event.type == pygame.KEYUP:
            if self.start and not self.finished:  # 游戏进行过程
                if event.key == pygame.K_w:
                    self.boardLi[PLAYER_1_CODE].upKey.upEvent()  # w键松开
                if event.key == pygame.K_s:
                    self.boardLi[PLAYER_1_CODE].downKey.upEvent()  # s键松开
                if event.key == pygame.K_UP:
                    self.boardLi[PLAYER_2_CODE].upKey.upEvent()  # 上键松开
                if event.key == pygame.K_DOWN:
                    self.boardLi[PLAYER_2_CODE].downKey.upEvent()  # 下键松开
            if self.countDown == False and self.start == False and self.finished == False:  # 开始界面
                if event.key == pygame.K_w:
                    self.selectLi[PLAYER_1_CODE].upKey.upEvent()
                if event.key == pygame.K_s:
                    self.selectLi[PLAYER_1_CODE].downKey.upEvent()
                if event.key == pygame.K_UP:
                    self.selectLi[PLAYER_2_CODE].upKey.upEvent()
                if event.key == pygame.K_DOWN:
                    self.selectLi[PLAYER_2_CODE].downKey.upEvent()

    def updateSelect(self):  # 更新选择
        for each in self.selectLi:
            if each.upKey.isDown() and each.downKey.isUp():
                each.eventKeyUp()
            elif each.downKey.isDown() and each.upKey.isUp():
                each.eventKeyDown()
            each.move()

    def updateBoard(self):  # 更新板子
        for eachBoard in self.boardLi:
            if not eachBoard.getIsComputer():  # 如果不是电脑
                if eachBoard.upKey.isDown() and eachBoard.downKey.isUp():  # 如果按下'上' 松开'下'
                    eachBoard.eventKeyUp()  # 板子向上移动
                elif eachBoard.downKey.isDown() and eachBoard.upKey.isUp():  # 如果按下'下' 松开'上'
                    eachBoard.eventKeyDown()  # 板子向下移动
            else:  # 如果是电脑
                if eachBoard.computerEvent(self.ballLi) == COMPUTER_UP_EVENT:
                    eachBoard.eventKeyUp()
                elif eachBoard.computerEvent(self.ballLi) == COMPUTER_DOWN_EVENT:
                    eachBoard.eventKeyDown()

    def showStartFace(self, screen):
        screen.blit(TITLE_TEXT_BLIT[0], TITLE_TEXT_BLIT[1])
        screen.blit(PREPARE_TEXT_BLIT[0], PREPARE_TEXT_BLIT[1])
        for each in self.selectLi:
            each.show(screen)
        screen.blit(EDITOR_TEXT_BLIT[0], EDITOR_TEXT_BLIT[1])
        screen.blit(VERSION_TEXT_BLIT[0], VERSION_TEXT_BLIT[1])

    def showReadyCounterFace(self, screen):
        countdownTextSurf = FONT_3.render(self.timeCountText, True, WHITE_COLOR)
        screen.blit(countdownTextSurf, READY_COUNTDOWN_TEXT_POSI)

    def showGameProcessesFace(self, screen):
        scoreTextP1 = 'P1: {:^3d}'.format(self.boardLi[PLAYER_1_CODE].getScore())  # 比分
        scoreTextP2 = 'P2: {:^3d}'.format(self.boardLi[PLAYER_2_CODE].getScore())
        timeText = '{:^3d}'.format(self.timeLast)  # 倒计时时间
        scoreTextSurfP1 = FONT_1.render(scoreTextP1, True, PLAYER_1_COLOR)
        scoreTextSurfP2 = FONT_1.render(scoreTextP2, True, PLAYER_2_COLOR)
        timeTextSurf = FONT_1.render(timeText, True, WHITE_COLOR)
        screen.blit(scoreTextSurfP1, GAME_PROCESSES_P1_SCORE_TEXT_POSI)
        screen.blit(scoreTextSurfP2, GAME_PROCESSES_P2_SCORE_TEXT_POSI)
        screen.blit(timeTextSurf, GAME_PROCESSES_TIME_TEXT_POSI)

    def showGameOverFace(self, screen):
        scoreTextP1 = 'P1: {:^3d}'.format(self.boardLi[PLAYER_1_CODE].getScore())
        scoreTextP2 = 'P2: {:^3d}'.format(self.boardLi[PLAYER_2_CODE].getScore())
        scoreTextSurfP1 = FONT_2.render(scoreTextP1, True, PLAYER_1_COLOR)
        scoreTextSurfP2 = FONT_2.render(scoreTextP2, True, PLAYER_2_COLOR)
        if self.boardLi[PLAYER_1_CODE].getScore() > self.boardLi[PLAYER_2_CODE].getScore():
            screen.blit(P1_WIN_TEXT_BLIT[0], P1_WIN_TEXT_BLIT[1])  # p1获胜
        elif self.boardLi[PLAYER_1_CODE].getScore() < self.boardLi[PLAYER_2_CODE].getScore():
            screen.blit(P2_WIN_TEXT_BLIT[0], P2_WIN_TEXT_BLIT[1])  # p2获胜
        else:  # 平局
            screen.blit(DRAW_TEXT_BLIT[0], DRAW_TEXT_BLIT[1])
        screen.blit(scoreTextSurfP1, GAME_OVER_P1_SCORE_TEXT_POSI)
        screen.blit(scoreTextSurfP2, GAME_OVER_P2_SCORE_TEXT_POSI)
        screen.blit(REMAKE_TEXT_BLIT[0], REMAKE_TEXT_BLIT[1])
        screen.blit(TIME_OUT_TEXT_BLIT[0], TIME_OUT_TEXT_BLIT[1])
        screen.blit(EDITOR_TEXT_BLIT[0], EDITOR_TEXT_BLIT[1])
        screen.blit(VERSION_TEXT_BLIT[0], VERSION_TEXT_BLIT[1])

    def setScreen(self, screen):
        screen.fill(BACKGROUND_COLOR)  # 黑色背景
        if self.finished == False:  # 如果游戏没结束
            pygame.draw.rect(screen, BOUNDARY_COLOR, BOUNDARY_LEFT_RECT, 0)  # 显示灰色轨道条
            pygame.draw.rect(screen, BOUNDARY_COLOR, BOUNDARY_RIGHT_RECT, 0)
        if self.countDown == False and self.start == False and self.finished == False:  # 开始界面
            self.updateSelect()
        if self.start and not self.finished:  # 游戏进行过程
            self.updateBoard()  # 更新板子
            for eachBall in self.ballLi:  # 遍历所有球
                if eachBall.isOut():  # 如果球出界
                    self.ballLi.remove(eachBall)  # 移除该球
                    continue
                eachBall.move(self.boardLi)  # 正常的球
                eachBall.show(screen)  # 显示球
        if self.finished == False:  # 如果游戏没结束
            for eachBoard in self.boardLi:
                eachBoard.show(screen)  # 显示板子
        if self.start == False and self.countDown == False and self.finished == False:  # 最开始界面
            self.showStartFace(screen)
        elif self.start == False and self.countDown == True and self.finished == False:  # 准备倒计时界面
            self.showReadyCounterFace(screen)
        if self.start == True and self.finished == False:  # 游戏过程中
            self.showGameProcessesFace(screen)
        elif self.finished == True:  # 游戏结束
            self.showGameOverFace(screen)
