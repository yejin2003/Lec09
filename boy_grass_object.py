from pico2d import *
import random

open_canvas()
grass = load_image('grass.png')
boy = load_image('character.png')
ball_s=load_image('ball21x21.png')


class Ball_s:
    def __init__(self):
        self.x,self.y=random.randint(100,700),599
        self.frame=random.randint(0,7)
        self.image=load_image('ball21x21.png')

    def update(self):
        self.frame=(self.frame+1)%8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 50, 0, 100, 100, self.x, self.y)

class Boy:
    def __init__(self):
        self.x,self.y=random.randint(100,700),90
        self.frame= random.randint(0,7)
        self.image=load_image('run_animation.png')

    def update(self):
        self.frame=(self.frame+1)%8
        self.x+=5

    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

class Grass:
    def __init__(self):
        self.image=load_image('grass.png')

    def draw(self):
        self.image.draw(400,30)

    def update(self):pass
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()

def reset_world():
    global running
    global grass
    global team
    global world
    global ball_s

    running=True
    world=[]

    grass=Grass()
    world.append(grass)

    team=[Boy() for i in range(10)]
    world+=team

    ball_s=[Ball_s() for i in range(20)]
    world+=ball_s

def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()

open_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
