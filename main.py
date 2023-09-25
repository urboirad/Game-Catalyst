import pygame
import pygame_gui
import requests
import winapps
import re
import os
import subprocess
from pathlib import Path
from sys import exit

response = requests.get("https://github.com/urboirad/Game-Catalyst/releases/latest")

version = '0.0.0'
#version = response.json()["name"]

class Game:
    def __init__(self, name, version, client, source):
        self.name = name
        self.version = version
        self.client = client
        self.source = source
        
pygame.init()
pygame.font.init()

screen_w = 1280
screen_h = 720
title = pygame.display.set_caption('GAME-CATALYST')
screen = pygame.display.set_mode((screen_w, screen_h))
manager = pygame_gui.UIManager((screen_w, screen_h))
clock = pygame.time.Clock()
font = pygame.font.SysFont('Small Font', 30)

button_layout_rect = pygame.Rect(10, 20, 100, 20)

hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)), text='Say Hello', manager=manager)

games = []

# texts
txt_title = font.render('GAME-CATALYST '+'('+version+')' , False, (255,255,255))


# Search for games
for app in winapps.list_installed():
    if re.search(r'steam', str(app.install_location)):
        x = Game(str(app.name), str(app.version), 'Steam', app.install_location)
        games.append(x)

# Check if no games are found        
if games == []:
    print('No games found...')
else:
    for x in games:
        print(x.name+' - '+x.client+' - '+str(x.source))
        
# Create buttons
button_width = 500
button_height = 50
button_spacing = 20
total_button_height = len(games)*(button_height+button_spacing)

for index, item in enumerate(games):
    y = (screen_h - total_button_height) // 2, y, button_width, button_height), text=item.name, manager=manager, container=None,object_id="#menu_button")
    
def open_game(item):
        
        
while True:
    time_delta = clock.tick(60)/1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
              if event.ui_element == hello_button:
                  base = str(os.path.basename(games[0].source))
                  to_ext = base+'.exe'
                  to_pre = os.path.join(games[0].source, to_ext)
                  to_str = str(to_pre)
                  to = Path(to_str)
                  print(to)
                  subprocess.call(to)
                  #print('Hello World!')
            
        manager.process_events(event)


        #game code
        screen.blit(txt_title,(10,10))


        clock.tick(60)
        
    manager.update(time_delta)
    manager.draw_ui(screen)
    pygame.display.update()