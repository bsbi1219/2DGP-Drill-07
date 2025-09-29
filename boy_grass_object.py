from pico2d import *
import random

class Grass:
    def __init__(self): # 개체의 속성을 정의하고 초기화 하는 기능(생성자 함수)
        self.image = load_image('grass.png') # self는 객체 자기 자신을 가리킴

    def draw(self):
        self.image.draw(400, 30)

    def update(self):
        pass


class Boy:
    def __init__(self):
        self.image = load_image('run_animation.png')
        self.x = random.randint(100, 700)
        self.frame = random.randint(0, 7)

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, 90) # clip_draw는 이미지의 일부분을 그리는 함수. 에니메이션이기 때문에 clip_draw를 사용

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 8

class Zombie:
    def __init__(self):
        self.image = load_image('zombie_run_animation.png')
        self.x, self.y = 100, 170
        self.frame = 0

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, frame_width, frame_height,
                             self.x, self.y, frame_width // 2, frame_height // 2)

    def update(self):
        self.x += 5
        self.frame = (self.frame + 1) % 10

class Big_Ball:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x = random.randint(100, 700)
        self.y = 599

class Small_Ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x = random.randint(100, 700)
        self.y = 599

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
    global world # world list - 모든 객체들을 갖고 있는 리스트

    world = [] # 하나도 객체가 없는 월드
    running = True

    grass = Grass()
    world.append(grass) # 땅을 만들고 월드에 추가

    team = [Boy() for _ in range(11)] # 매개변수 안써도 됨
    world += team # 소년들을 만들고 월드에 추가. 리스트에 리스트를 더하면 하나의 리스트로 합쳐짐

    zombie = Zombie()
    world.append(zombie) # 좀비를 만들고 월드에 추가

def update_world(): # 게임 로직
    for game_object in world:
        game_object.update()

def render_world(): # 월드에 객체들을 그린다
    clear_canvas()
    for game_object in world:
        game_object.draw()
    update_canvas()

reset_world()

while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

close_canvas()
