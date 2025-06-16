from utils import randcell

class Helicopter:
    def __init__(self,w,h):
        rc = randcell(w,h)
        rx, ry = rc[0],rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.tank = int(0)
        self.mxtank = int(1)
        self.score = int(0)
        self.lives = 2

    def move(self,dx,dy):
        nx, ny = dx+self.x, dy + self.y
        if (nx >= 0 and ny>=0 and nx<self.h and ny<self.w):
            self.x, self.y = nx,ny

    def print_menu(self):
        print("HEALTH ", self.lives, sep="", end=" | ")
        print("TANK ", self.tank,"/", self.mxtank, sep="", end=" | ")
        print("SCORE: ", self.score)