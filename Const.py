import pygame
fps = 144   #帧率
circleRadius = 10
guessRedius = 4
boardVelo = 8
computerPlayer = [0]
showGuessPoint = True
maxBallNum = 5
intervalTime = 1    #发球间隔时间
ballVeloRange = (2,6)
maxTime = 60
precision = 8
computerEvent = (computerUpEvent,computerDownEvent,computerStopEvent) = ('UP','DOWN','STOP')
boardSize = boardX , boardY = 10,100
screenSize = screenX , screenY = (800,800)
colorLi = [(255,255,255),
            (0,0,255),
            (0,255,0),
            (255,0,0),
            (50,50,50)]
initName = 'LZS'
screenMid = (screenX//2 , screenY//2)
boardInitPosi = [(0,screenY//2 - boardY//2,boardX,boardY), 
                (screenX - boardX,screenY//2 - boardY//2,boardX,boardY)]
boundaryPosi = [(0,0,boardX,screenY), 
                (screenX - boardX,0,boardX,screenY)]

pygame.font.init()
font_1 = pygame.font.Font('E:/data/learn/pygame/game_3/font/microsoftyahei.ttf', 22)
font_2 = pygame.font.Font('E:/data/learn/pygame/game_3/font/microsoftyahei.ttf', 28)
font_3 = pygame.font.Font('E:/data/learn/pygame/game_3/font/microsoftyahei.ttf', 60)
prepareText = 'Press [SPACE] to start'
prepareTextP1 = 'P1: use [w] [s] to move'
prepareTextP2 = 'P2: use [↑] [↓] to move'
editorText = 'editor: LZS'
remakeText = 'Press [r] to remake'
timeOutText = 'TIME OUT'
winText = 'WINNER'
drawText = 'DRAW'
preTextSurf = []
preTextSurf.append(font_2.render(prepareText,True,colorLi[0]))
preTextSurf.append(font_2.render(prepareTextP1,True,colorLi[1]))
preTextSurf.append(font_2.render(prepareTextP2,True,colorLi[2]))
preTextSurf.append(font_1.render(editorText,True,colorLi[0]))
preTextSurf.append(font_2.render(remakeText,True,colorLi[0]))
preTextSurf.append(font_3.render(timeOutText,True,colorLi[0]))
preTextPosi = [(screenX//2 - 150,screenY//2 - 20),
                (screenX//2 - 380,screenY//2 - 200),
                (screenX//2 + 60,screenY//2 - 200),
                (screenX//2 - 50,screenY - 30),
                ((screenX//2 - 130,screenY - 200)),
                ((screenX//2 - 150,150))]