from utils import randbool
from utils import randcell
from utils import randcell2


# 0 - field
# 1 - tree
# 2 - river
# 3 - hospital
# 4 - upgrade-shop
# 5 - fire

CELL_TYPES="🟩🌳🌊🏨🏪🔥"

TREE_BONUS=int(10)

UPGRADE_COST = 100
LIFE_COST = 1000

class Map:


    def __init__(self,w,h):
        self.w=int(w)
        self.h=int(h)
        self.cells = [[0 for i in range(w)]for j in range(h)]
        self.generate_forest(3,10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_river(10)
        self.generate_upgrade_shop()
        self.generate_hospital()


    def print_map(self, helicopter, clouds):
        print("⬛" * (self.w+2))
        for ri in range(self.h):
            print("⬛",end="")
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if(clouds.cells[ri][ci]==1):
                    print("⚪",end="")
                elif (clouds.cells[ri][ci]==2):
                    print("⭐",end="")
                elif(helicopter.x == ri and helicopter.y == ci):
                    print("🚁",end="")
                elif(cell>=0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell],end="")
            print("⬛")
        print("⬛" * (self.w+2))


    def check_bounds(self, x, y):
        if(x<0 or y<0 or x>=self.h or y >= self.w):
            return False
        return True


    def generate_river(self, l):
        rc = randcell(self.w,self.h)
        rx = rc[0]
        ry = rc[1]
        self.cells[rx][ry] = 2
        while l>0:
            rc2 = randcell2(rx,ry)
            rx2,ry2 = rc2[0],rc2[1]
            if(self.check_bounds(rx2,ry2)):
                self.cells[rx2][ry2] = 2
                rx,ry = rx2, ry2
                l-=1


    def generate_forest(self,r,mxr):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r,mxr):
                    self.cells[ri][ci] = 1


    def generate_tree(self):
        c = randcell(self.w,self.h)
        cx, cy = c[0], c[1]
        if ( self.check_bounds(cx,cy) and self.cells[cx][cy] == 0):
            self.cells[cx][cy] = 1


    def generate_fire(self):
        c = randcell(self.w, self.h)
        cx, cy = c[0], c[1]
        if self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5

    def generate_upgrade_shop(self):
        c = randcell(self.w,self.h)
        cx, cy = c[0],c[1]
        if self.cells[cx][cy]!=4:
            self.cells[cx][cy]=3
        else:
            self.generate_hospital()

    def generate_hospital(self):
        c = randcell(self.w,self.h)
        cx, cy = c[0],c[1]
        self.cells[cx][cy] = 4

    def update_fires(self):
        for ri in range(self.h):
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if cell == 5:
                    self.cells[ri][ci] = 0
        for i in range(10):
            self.generate_fire()

    def process_helicopter(self, helicopter, clouds):
        c = self.cells[helicopter.x][helicopter.y]
        d = clouds.cells[helicopter.x][helicopter.y]
        if(c==2):
            if helicopter.tank<helicopter.mxtank:
                helicopter.tank +=1
        if(c==5):
            if helicopter.tank>=1:
                helicopter.tank-=1
                helicopter.score+= TREE_BONUS
                self.cells[helicopter.x][helicopter.y]=1
        if(c == 4 and helicopter.score >= UPGRADE_COST):
            helicopter.mxtank+=1
            helicopter.score -= UPGRADE_COST
        if(c == 3 and helicopter.score >= LIFE_COST):
            helicopter.lives+=1
            helicopter.score -= LIFE_COST
        if(c == 3 and helicopter.score >= LIFE_COST):
            helicopter.lives+=20
            helicopter.score -= LIFE_COST
        if(d == 2):
            helicopter.lives-=1
            if helicopter.lives<=0:
                print("GAME OVER! YOUR FINAL SCORE IS:", helicopter.score)
                exit(0)

    def export_data(self):
        return {"cells": self.cells}

    def import_data(self, data):
        self.cells = data["cells"] or [[0 for i in range(self.w)]for j in range(self.h)]