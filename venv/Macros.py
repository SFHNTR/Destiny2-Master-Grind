import keyboard;
import time;
import random;
import mouse;


def drunkenSailor():
    timer = random.uniform(.1, 2)
    print("Time dif: " + str(timer))
    stop = time.time() + timer
    print("going left")
    while(time.time() < stop):
        keyboard.press("a")
        time.sleep(.1)
    print("stopping")
    keyboard.release("a")

def insaneRecoil():
    print("waiting")
    time.sleep(5)
    print("recording starting")
    recording = mouse.record(button='right')
    print("recording stopped, playing")
    mouse.play(recording, speed_factor=2.0, include_clicks=True, include_moves=True, include_wheel=True)
    mouse.right_click()


