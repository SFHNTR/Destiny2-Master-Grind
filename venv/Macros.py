import keyboard
import time
import random
import mouse


def drunkenSailor():
    while(1):
        drunktimer = random.uniform(.1, 2)
        stop = time.time() + drunktimer
        wasdList = ["w", "a", "s", "d" ]
        selectedInput = random.choice(wasdList)
        print(selectedInput)
        while(time.time() < stop):
            keyboard.press(selectedInput)
            time.sleep(.5)
        print("stopping")
        keyboard.release(selectedInput)
    return

def insaneRecoil():
    print("waiting")
    time.sleep(5)
    print("recording starting")
    recording = mouse.record(button='right')
    print("recording stopped, playing")
    mouse.play(recording, speed_factor=2.0, include_clicks=True, include_moves=True, include_wheel=True)
    mouse.right_click()

def fatFingered():
    fatTimer = 45
    testTime = time.time() + fatTimer
    while(1):
        if(time.time() > testTime):
            fiftyFifty = random.choice([1,2])
            if (fiftyFifty == 1):
                keyboard.press("f")
                time.sleep(.1)
                keyboard.release("f")
            fatTimer = 10
            testTime = time.time() + fatTimer

def indecisive():
    indecisiveTimer = random.uniform(15, 30)
    switchTime = time.time() + indecisiveTimer
    while(1):
        if(time.time() > switchTime):
            weaponSelect = random.choice([1, 2, 3])
            if (weaponSelect == 1):
                keyboard.press("1")
                time.sleep(.1)
                keyboard.release("1")
            elif (weaponSelect == 2):
                keyboard.press("2")
                time.sleep(.1)
                keyboard.release("2")
            elif (weaponSelect == 3):
                keyboard.press("3")
                time.sleep(.1)
                keyboard.release("3")

            indecisiveTimer = random.uniform(15, 30)
            switchTime = time.time() + indecisiveTimer

def randomDancing():
    dancingTimer = random.uniform(20, 30)
    danceTime = time.time() + dancingTimer
    while(1):
        if (time.time() > danceTime):
            danceSelect = random.choice(["up", "down", "left", "right"])
            keyboard.press(danceSelect)
            time.sleep(.1)
            keyboard.release(danceSelect)
            dancingTimer = random.uniform(20, 30)
            danceTime = time.time() + dancingTimer

def tripping():
    trippingTimer = random.uniform(10, 45)
    tripTime = time.time() + trippingTimer
    while(1):
        if (time.time() > tripTime):
            keyboard.press("ctrl")
            time.sleep(.1)
            keyboard.release("ctrl")
            trippingTimer = random.uniform(10, 45)
            tripTime = time.time() + trippingTimer

def hops():
    hopsTimer = random.uniform(10, 45)
    hopsTime = time.time() + hopsTimer
    while(1):
        if (time.time() > hopsTime):
            print("hopping")
            keyboard.press("space")
            time.sleep(.1)
            keyboard.release("space")
            hopsTimer = random.uniform(10, 45)
            hopsTime = time.time() + hopsTimer

def compulsiveReload():
    reloadTimer = random.uniform(5, 15)
    reloadTime = time.time() +reloadTimer
    while (1):
        if (time.time() > reloadTime):
            print("reloading")
            keyboard.press("r")
            time.sleep(.1)
            keyboard.release("r")
            reloadTimer = random.uniform(5, 15)
            reloadTime = time.time() + reloadTimer
