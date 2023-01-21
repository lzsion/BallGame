from Const import *
from Key import *
class SelectPlayer:
    def __init__(self,name):
        if name == PLAYER_1_NAME :
            self.color = PLAYER_1_COLOR
            self.name = PLAYER_1_CODE
            self.noticeTextBlit = PREPARE_P1_TEXT_BLIT
            self.selectedBlit = P1_SELECTED_BLIT
            self.colorTextBlit = P1_COLOR_TEXT_BLIT
            self.playerTextSurf =  P1_PLAYER_TEXT_SURF
            self.playerTextPosi = P1_PLAYER_TEXT_POSI
            self.computerTextSurf =  P1_COMPUTER_TEXT_SURF
            self.computerTextPosi = P1_COMPUTER_TEXT_POSI
        elif name == PLAYER_2_NAME :
            self.color = PLAYER_2_COLOR
            self.name = PLAYER_2_CODE
            self.noticeTextBlit = PREPARE_P2_TEXT_BLIT
            self.selectedBlit = P2_SELECTED_BLIT
            self.colorTextBlit = P2_COLOR_TEXT_BLIT
            self.playerTextSurf =  P2_PLAYER_TEXT_SURF
            self.playerTextPosi = P2_PLAYER_TEXT_POSI
            self.computerTextSurf =  P2_COMPUTER_TEXT_SURF
            self.computerTextPosi = P2_COMPUTER_TEXT_POSI
        self.upKey = Key()
        self.downKey = Key()
        self.speed = [0,0]
        self.selectComputer = False
    def isSelectComputer(self):
        return self.selectComputer
    def setSelectComputer(self,selectComputer):
        self.selectComputer = selectComputer
    def show(self,screen):
        screen.blit(self.noticeTextBlit[0],self.noticeTextBlit[1])
        screen.blit(self.selectedBlit[0],self.selectedBlit[1])
        screen.blit(self.colorTextBlit[0],self.colorTextBlit[1])
        screen.blit(self.playerTextSurf,self.playerTextPosi)
        screen.blit(self.computerTextSurf,self.computerTextPosi)
    def boundaryJudge(self):    #边界判定
        if self.playerTextPosi[Y_AXIS] + self.speed[Y_AXIS] <= SELECT_Y_LEVEL - LINE_Y_SIZE:  #上边界
            self.speed = [0,0]  
            return True          
        elif self.playerTextPosi[Y_AXIS] + self.speed[Y_AXIS] >= SELECT_Y_LEVEL:   #下边界
            self.speed = [0,0]
            return True
        return False
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
   
