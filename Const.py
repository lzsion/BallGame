import pygame
FPS = 144   #帧率
BALL_RADIUS = 10    #发射的球半径
GUESS_BALL_R = 4    #估计落点球半径
BOARD_VELOCITY = 8   #板子移动速度
computerPlayer = [0]
showGuessPoint = True
MAX_BALL_NUM = 5    #场上最大球数
SERVE_INTERVAL_TIME = 1 #发球间隔时间
BALL_VELOCITY_RANGE = (2,6) #球速度范围
MAX_TIME = 60   #一局时间(秒)
COMPUTER_CATCH_PRECISION = 8    #计算机接球精度
COMPUTER_UP_EVENT = 'UP'    #分析向上
COMPUTER_DOWN_EVENT = 'DOWN'    #分析向下
COMPUTER_STOP_EVENT = 'STOP'    #分析不动
X_AXIS = 0  #x轴
Y_AXIS = 1  #y轴
PLAYER_1_CODE = 0   #P1
PLAYER_2_CODE = 1   #p2
PLAYER_NULL_CODE = 2    #空白
BOARD_X_SIZE = 10    #移动板x长度
BOARD_Y_SIZE = 100   #移动版y长度
SCREEN_X_SIZE = 800  #窗口x长度
SCREEN_Y_SIZE = 800  #窗口y长度
BLACK_COLOR = (0,0,0)   #黑色
WHITE_COLOR = (255,255,255) #白色
RED_COLOR = (255,0,0)   #红色
BACKGROUND_COLOR = BLACK_COLOR  #背景颜色
UNSELECTED_COLOR = WHITE_COLOR  #未被选择球的颜色
PLAYER_1_COLOR = (0,0,255)  #P1颜色
PLAYER_2_COLOR = (0,255,0)  #p2颜色
BOUNDARY_COLOR = (50,50,50)     #轨道颜色
NULL_NAME = 'LZS'   #空白名字
BOARD_LEFT_POSI = (0,SCREEN_Y_SIZE//2 - BOARD_X_SIZE//2)    #左边板子初始位置
BOARD_RIGHT_POSI = (SCREEN_X_SIZE - BOARD_X_SIZE,SCREEN_Y_SIZE//2 - BOARD_X_SIZE//2)    #右边板子初始位置
BOUNDARY_LEFT_RECT = (0,0,BOARD_X_SIZE,SCREEN_Y_SIZE)   #左边界矩形
BOUNDARY_RIGHT_RECT = (SCREEN_X_SIZE - BOARD_X_SIZE,0,BOARD_X_SIZE,SCREEN_Y_SIZE)     #右边界矩形
GUESSED_Y_DROP_ONTO = 0
GUESSED_Y_GUESS_Y = 1
GUESSED_Y_TICK = 2
GUESSED_Y_BELONG_TO = 3
PATH = 'E:/data/learn/pygame/BallGame'
pygame.font.init()  #字体
FONT_1 = pygame.font.Font(PATH + '/font/microsoftyahei.ttf', 22)
FONT_2 = pygame.font.Font(PATH + '/font/microsoftyahei.ttf', 28)
FONT_3 = pygame.font.Font(PATH + '/font/microsoftyahei.ttf', 60)
VERSION_TEXT = 'v2.0.1'
TITLE_TEXT = 'Ball Game'
PREPARE_TEXT = 'Press [SPACE] to start'
PREPARE_P1_TEXT = 'P1: use [w] [s] to move'
PREPARE_P2_TEXT = 'P2: use [↑] [↓] to move'
EDITOR_TEXT = 'editor: LZS'
REMAKE_TEXT = 'Press [r] to remake'
TIME_OUT_TEXT = 'TIME OUT'
WIN_TEXT = 'WINNER'
DRAW_TEXT = 'DRAW'
PREPARE_TEXT_BLIT = (
    FONT_2.render(PREPARE_TEXT,True,WHITE_COLOR),
    (SCREEN_X_SIZE//2 - 150,SCREEN_Y_SIZE//2 - 20)
)
PREPARE_P1_TEXT_BLIT = (
    FONT_2.render(PREPARE_P1_TEXT,True,PLAYER_1_COLOR),
    (SCREEN_X_SIZE//2 - 380,SCREEN_Y_SIZE//2 - 200)
)
PREPARE_P2_TEXT_BLIT = (
    FONT_2.render(PREPARE_P2_TEXT,True,PLAYER_2_COLOR),
    (SCREEN_X_SIZE//2 + 60,SCREEN_Y_SIZE//2 - 200)
)
EDITOR_TEXT_BLIT = (
    FONT_1.render(EDITOR_TEXT,True,WHITE_COLOR),
    (SCREEN_X_SIZE - 150,SCREEN_Y_SIZE - 50)
)
VERSION_TEXT_BLIT = (
    FONT_1.render(VERSION_TEXT,True,WHITE_COLOR),
    (30,SCREEN_Y_SIZE - 50)
)
REMAKE_TEXT_BLIT = (
    FONT_2.render(REMAKE_TEXT,True,WHITE_COLOR),
    (SCREEN_X_SIZE//2 - 130,SCREEN_Y_SIZE - 200)
)
TIME_OUT_TEXT_BLIT = (
    FONT_3.render(TIME_OUT_TEXT,True,WHITE_COLOR),
    (SCREEN_X_SIZE//2 - 150,150)
)