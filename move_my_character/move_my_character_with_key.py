from pico2d import *


open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
# xlenght : 64 / ylenght : 64


def handle_events():
    global quit, running, dirX, dirY, dir, frame

    # fill here
    events = get_events()
    for event in events:
        # fill here
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                quit = True
            elif running == False:
                running = True
                if event.key == SDLK_RIGHT:
                    dir = 0
                    dirX = 1
                elif event.key == SDLK_LEFT:
                    dir = 2
                    dirX = -1
                elif event.key == SDLK_UP:
                    dir = 3
                    dirY = 1
                elif event.key == SDLK_DOWN:
                    dir = 1
                    dirY = -1
                
        elif event.type == SDL_KEYUP and running == True:
            running = False
            frame = 0
            if event.key == SDLK_RIGHT:
                dir = 1
                dirX = 0
            elif event.key == SDLK_LEFT:
                dir = 1
                dirX = 0
            elif event.key == SDLK_UP:
                dir = 1
                dirY = 0
            elif event.key == SDLK_DOWN:
                dir = 1
                dirY = 0

running = False
quit = False
x = 800 // 2
y = 600 // 2
frame = 0
dirX = 0
dirY = 0
dir = 0

# fill here
while not quit:
    clear_canvas()
    grass.draw(400, 90)
    character.clip_draw(frame*64, dir*64 , 64, 64, x, y, 100, 100)
    update_canvas()
    handle_events()
    if running:
        frame = (frame + 1) % 8
    x += dirX * 10
    if x > 766:
        x = 766
    elif x < 34:
        x = 34
    y += dirY * 10
    if y > 566:
        y = 566
    elif y < 54:
        y = 54
    delay(0.05)
    # 상하좌우 : WSAD / 게임종료 : ESC

close_canvas()

