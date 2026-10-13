from pico2d import *
import random


# Game object class here

# 게임 객체를 파악.
# boy, grass 가 필요하다.

Grass = None
Boy = None
Zombie = None

class Grass: # 클래스는 대문자로 시작함
    # 잔디 속성을 초기화
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): # 잔디는 움직이지 않으므로 update는 필요없지만
        pass          # 형식적으로 만들어줘야한다.

class Boy:
    def __init__(self):
        self.x = random.randint(100, 700)
        self.y = 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)

class Zombie:
    def __init__(self):
        self.x, self.y = 100, 170
        self.frame = 0
        self.image = load_image('zombie_run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 10
        self.x += 5

    def draw(self):
        frame_width = self.image.w // 10
        frame_height = self.image.h
        self.image.clip_draw(self.frame * frame_width, 0, 
                             frame_width, frame_height, 
                             self.x, self.y, frame_width // 2, frame_height // 2)
        

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

def reset_world():
    global running

    global world
    world = [] # 월드 전체를 나타내는 리스트, 월드의 모든 객체가 들어있다.
    running = True

    # 잔디 객체를 찍어낸다.
    grass = Grass()
    world.append(grass)

    zombie = Zombie()
    world.append(zombie)

    team = [Boy() for i in range(11)]

    world += team # world 리스트에 team 리스트를 합한다.


def update_world():
    for o in world:
        o.update()

def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()

# 초기화 코드
reset_world() # 세상을 구성하는 객체들을 초기화

# 게임 루프 코드
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.01)

# 종료 코드
close_canvas()
