from Const import *
from Key import *
class SelectPlayer:
    def __init__(self,name):
        if name == PLAYER_1_NAME :
            self.noticeTextBlit = PREPARE_P1_TEXT_BLIT  #提示信息blit
            self.selectedBlit = P1_SELECTED_BLIT    #><选择框文本blit
            self.colorTextBlit = P1_COLOR_TEXT_BLIT #P1/P2文本blit
            self.playerTextSurf =  P1_PLAYER_TEXT_SURF  #'player'
            self.playerTextPosi = P1_PLAYER_TEXT_POSI   #'player'初始位置
            self.computerTextSurf =  P1_COMPUTER_TEXT_SURF  #'computer'
            self.computerTextPosi = P1_COMPUTER_TEXT_POSI   #'computer'初始位置
        elif name == PLAYER_2_NAME :
            self.noticeTextBlit = PREPARE_P2_TEXT_BLIT
            self.selectedBlit = P2_SELECTED_BLIT
            self.colorTextBlit = P2_COLOR_TEXT_BLIT
            self.playerTextSurf =  P2_PLAYER_TEXT_SURF
            self.playerTextPosi = P2_PLAYER_TEXT_POSI
            self.computerTextSurf =  P2_COMPUTER_TEXT_SURF
            self.computerTextPosi = P2_COMPUTER_TEXT_POSI
        self.upKey = Key()  #往上按键
        self.downKey = Key()    #往下按键
        self.speed = [0,0]  #速度
        self.selectComputer = False #是否选择电脑
    def isSelectComputer(self):
        return self.selectComputer
    def setSelectComputer(self,selectComputer):
        self.selectComputer = selectComputer
    def show(self,screen):  #显示所有文本信息
        screen.blit(self.noticeTextBlit[0],self.noticeTextBlit[1])
        screen.blit(self.selectedBlit[0],self.selectedBlit[1])
        screen.blit(self.colorTextBlit[0],self.colorTextBlit[1])
        screen.blit(self.playerTextSurf,self.playerTextPosi)
        screen.blit(self.computerTextSurf,self.computerTextPosi)
    def boundaryJudge(self):    #边界判定
        if self.playerTextPosi[Y_AXIS] + self.speed[Y_AXIS] <= SELECT_Y_LEVEL - LINE_Y_SIZE:  #上边界
            self.speed = [0,0]
        elif self.playerTextPosi[Y_AXIS] + self.speed[Y_AXIS] >= SELECT_Y_LEVEL:   #下边界
            self.speed = [0,0]
    def move(self):     #移动
        self.boundaryJudge()    #判断边界
        self.playerTextPosi = (
            self.playerTextPosi[X_AXIS],
            self.playerTextPosi[Y_AXIS] + self.speed[Y_AXIS])    #更新位置
        self.computerTextPosi = (
            self.computerTextPosi[X_AXIS],
            self.computerTextPosi[Y_AXIS] + self.speed[Y_AXIS])    #更新位置
    def eventKeyUp(self):   #向上事件
        self.speed = [0,-SELECTED_VELOCITY]    #设定速度
        self.selectComputer = True
    def eventKeyDown(self): #向下事件
        self.speed = [0,SELECTED_VELOCITY]     #设定速度
        self.selectComputer = False
   
