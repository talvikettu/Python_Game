from clouds import Clouds
from map import Map
from helicopter import Helicopter as Helicopter
from pynput import keyboard
import json
import time
import os

TICK_SLEEP = 0.05
TREE_UPDATE = 50
FIRE_UPDATE = 75
CLOUDS_UPDATE = 100
MAP_W, MAP_H = 20, 10

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')



field = Map(MAP_W, MAP_H)
clouds = Clouds(MAP_W,MAP_H)
helicopter = Helicopter(MAP_W,MAP_H)
tick = 1


MOVES = {'w':(-1,0),'d':(0,1),'s':(1,0),'a':(0,-1)}
# f - save button, g - reload save

def on_release(key):
    global helicopter, clouds, field,tick
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0],MOVES[c][1]
        helicopter.move(dx,dy)
    elif c == "f":
        data={"helicopter":helicopter.export_data(),
              "clouds":clouds.export_data(),
              "field":field.export_data(),
              "tick": tick}
        with open("level.json","w+") as lvl:
            json.dump(data,lvl)

    elif c =="g":
        with open("level.json","r") as lvl:
            data = json.load(lvl)
            tick = data["tick"] or 1
            helicopter.import_data(data["helicopter"])
            clouds.import_data(data["clouds"])
            field.import_data(data["field"])


listener = keyboard.Listener(
    on_press=None,
    on_release=on_release)
listener.start()


while True:
    clear_console()
    print("TICK", tick)
    field.process_helicopter(helicopter, clouds)
    helicopter.print_menu()
    field.print_map(helicopter,clouds)
    tick +=1
    time.sleep(TICK_SLEEP)
    if( tick % TREE_UPDATE == 0):
        field.generate_tree()
    if( tick % FIRE_UPDATE == 0):
        field.update_fires()
    if( tick % CLOUDS_UPDATE == 0):
        clouds.update()