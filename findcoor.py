from pynput import keyboard
from pynput.mouse import Button, Controller
import time

mouse = Controller()
pos = [(593,352),(593,488),(593,622),(593,768)]

times = 5000000

def yesclick():
    time.sleep(0.04)
    mouse.position = (666,523)
    time.sleep(0.04)
    mouse.click(Button.left, 1)
    time.sleep(0.04)
        
def mercbuy():
    time.sleep(0.04)
    mouse.position = (410,730)
    time.sleep(0.04)
    mouse.click(Button.left, 1)
    yesclick()

def on_press_start(key):
    if key == keyboard.Key.esc:
        print('starting...')
        return False

def on_press_loop(key):
    if key == keyboard.Key.space:
        return False

def main():
    for po in pos:
        mouse.position = po
        time.sleep(0.04)
        mouse.click(Button.left, 1)
        time.sleep(0.04)
        mouse.click(Button.left, 1)
        yesclick()
        mouse.position = (610,263)
        time.sleep(0.04)
        mouse.click(Button.left, 1)
        time.sleep(0.04)
        mouse.position = (1042,458)
        time.sleep(0.04)
        mouse.click(Button.left, 1)
        time.sleep(0.04)

    xos = [(1046,763),(443,458),(820,678),(666,523),(766,550),(1138,107),(1400,78)]
    for xo in xos:
        mouse.position = xo
        time.sleep(0.04)
        mouse.click(Button.left, 1)
        time.sleep(0.04)

def activate():
    time.sleep(1)

    with keyboard.Listener(on_press=on_press_start) as listener:
        listener.join() # wait for F11...

    with keyboard.Listener(on_press=on_press_loop) as listener:
        for _ in range(times):
            main()
            if not listener.running:
                break
            

if __name__ == '__main__':
    poll = activate()