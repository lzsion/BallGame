import pygame
fps = 144   #帧率
circleRadius = 10   
BALL_RADIUS = 10    #球半径
guessRedius = 4
boardVelo = 8   #板子移动速度
BOARD_VELOCITY = 8   #板子移动速度
computerPlayer = []
showGuessPoint = True
maxBallNum = 5
intervalTime = 1    #发球间隔时间
ballVeloRange = (2,6)   #球速度范围
maxTime = 60    #一局时间(秒)
precision = 8
computerEvent = (computerUpEvent,computerDownEvent,computerStopEvent) = ('UP','DOWN','STOP')
COMPUTER_UP_EVENT = 'UP'
COMPUTER_DOWN_EVENT = 'DOWN'
COMPUTER_STOP_EVENT = 'STOP'
boardSize = boardX , boardY = 10,100
screenSize = screenX , screenY = (800,800)
X_AXIS = 0
Y_AXIS = 1
PLAYER_1_CODE = 0
PLAYER_2_CODE = 1
BOARD_X_SIZE = 10    #移动板x长度
BOARD_Y_SIZE = 100   #移动版y长度
SCREEN_X_SIZE = 800  #窗口x长度
SCREEN_Y_SIZE = 800  #窗口y长度
SCREEN_MID_POSI = (SCREEN_X_SIZE//2 , SCREEN_Y_SIZE//2)
BACKGROUND_COLOR = (0,0,0)
UNSELECTED_COLOR = (255,255,255)    #未被选择球的颜色
PLAYER_1_COLOR = (0,0,255)
PLAYER_2_COLOR = (0,255,0)
RAIL_COLOR = (50,50,50)
colorLi = [(255,255,255),
            (0,0,255),
            (0,255,0),
            (255,0,0),
            (50,50,50)]
NULL_NAME = 'LZS'
screenMid = (screenX//2 , screenY//2)
boardInitPosi = [(0,screenY//2 - boardY//2,boardX,boardY), 
                (screenX - boardX,screenY//2 - boardY//2,boardX,boardY)]
boundaryPosi = [(0,0,boardX,screenY), 
                (screenX - boardX,0,boardX,screenY)]
BOUNDARY_LEFT_RECT = (0,0,boardX,screenY)
BOUNDARY_RIGHT_RECT = (screenX - boardX,0,boardX,screenY)
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