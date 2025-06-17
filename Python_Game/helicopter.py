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
        self.lives = 40

    def move(self,dx,dy):
        nx, ny = dx+self.x, dy + self.y
        if (nx >= 0 and ny>=0 and nx<self.h and ny<self.w):
            self.x, self.y = nx,ny

    def print_menu(self):
        print("HEALTH ", self.lives, sep="", end=" | ")
        print("TANK ", self.tank,"/", self.mxtank, sep="", end=" | ")
        print("SCORE: ", self.score)

    def export_data(self):
        return {"score": self.score,
                "lives": self.lives,
                "x": self.x,"y":self.y,
                "tank":self.tank,"mxtank":self.mxtank}

    def import_data(self, data):
        self.x = data["x"] or 0
        self.y = data["y"] or 0
        self.tank = data["tank"] or 0
        self.mxtank = data["mxtank"] or 1
        self.lives = data["lives"] or 40
        self.score = data["score"] or 0