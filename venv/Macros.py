import keyboard
import time
import random
import mouse


def drunkenSailor(event):
    while(1):
        timer = random.uniform(.1, 2)
        stop = time.time() + timer
        wasdList = ["w", "a", "s", "d" ]
        selectedInput = random.choice(wasdList)
        print(selectedInput)
        while(time.time() < stop):
            keyboard.press(selectedInput)
            time.sleep(.5)
        print("stopping")
        keyboard.release(selectedInput)
        if event.isSet():
            print("Drunken Thread Killed")
            break
    return

def insaneRecoil():
    print("waiting")
    time.sleep(5)
    print("recording starting")
    recording = mouse.record(button='right')
    print("recording stopped, playing")
    mouse.play(recording, speed_factor=2.0, include_clicks=True, include_moves=True, include_wheel=True)
    mouse.right_click()

def fatFingered(event):
    timer = 45
    testTime = time.time() + timer
    while(1):
        if(time.time() > testTime):
            fiftyFifty = random.choice([1,2])
            if (fiftyFifty == 1):
                keyboard.press("f")
            timer = 10
            testTime = time.time() + timer
        if event.isSet():
            break
def indecisive(event):
    timer = random.uniform(15, 30)
    switchTime = time.time() + timer
    while(1):
        if(time.time() > switchTime):
            weaponSelect = random.choice([1, 2, 3])
            if (weaponSelect == 1):
                keyboard.press("1")
            elif (weaponSelect == 2):
                keyboard.press("2")
            elif (weaponSelect == 3):
                keyboard.press("3")

            timer = random.uniform(15, 30)
            switchTime = time.time() + timer
        if event.isSet():
            break
