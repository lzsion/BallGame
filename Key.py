class Key:
    def __init__(self):  # 按键状态 up/down [需要改为判定一个]
        self.down = False
        self.up = True

    def downEvent(self):
        self.down = True
        self.up = False

    def upEvent(self):
        self.down = False
        self.up = True

    def isDown(self):
        return self.down and not self.up

    def isUp(self):
        return self.up and not self.down
