from pico2d import *
import random

class Grass:
    def __init__(self): # 개체의 속성을 정의하고 초기화 하는 기능(생성자 함수)
        self.image = load_image('grass.png') # self는 객체 자기 자신을 가리킴
    pass

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = 400
        self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, 90) # clip_draw는 이미지의 일부분을 그리는 함수. 에니메이션이기 때문에 clip_draw를 사용

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True

open_canvas()

def reset_world():
    global running
    global grass
    global boy

    grass = Grass()
    boy = Boy()
    pass

def update_world():
    pass

def render_world(): # 월드에 객체들을 그린다
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    pass

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
