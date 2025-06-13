from map import Map
from helicopter import Helicopter as Helicopter
from pynput import keyboard
import time
import os

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 100
MAP_W, MAP_H = 20, 10

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



field = Map(MAP_W, MAP_H)
field.generate_forest(3,10)
field.generate_river(10)
field.generate_river(10)
field.generate_river(10)


helicopter = Helicopter(MAP_W,MAP_H)

MOVES = {'w':(-1,0),'d':(0,1),'s':(1,0),'a':(0,-1)}
def on_release(key):
    global helicopter
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0],MOVES[c][1]
        helicopter.move(dx,dy)
        

listener = keyboard.Listener(
    on_press=None,
    on_release=on_release)
listener.start()
tick = 1

while True:
    clear_console()
    print("TICK", tick)
    helicopter.print_menu()
    field.print_map(helicopter)
    tick +=1
    time.sleep(TICK_SLEEP)
    if(tick % TREE_UPDATE == 0):
        field.generate_tree()
    if( tick% FIRE_UPDATE == 0):
        field.update_fires()