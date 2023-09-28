import random

from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')

def hand_arrow_draw():
    global x, y
    x = (random.randint(0,1280))
    y = (random.randint(0,1024))

    hand.clip_draw(0, 0, 50, 50, x, y)

def stop_events():
    global running
    event = get_events()
    for event in event:
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand_arrow_draw()
    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    stop_events()
    delay(0.1)

close_canvas()




