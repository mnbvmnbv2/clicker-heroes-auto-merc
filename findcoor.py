from pynput import keyboard
from pynput.mouse import Button, Controller
import time

mouse = Controller()
pos = [(594,346),(454,480),(454,488),(454,617),(454,622),(454,762),(454,750)]

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

def on_press_mouse(key):
    if key == keyboard.Key.shift:
        print('Now we have moved it to {0}'.format(
        mouse.position))

def main():
    

    xos = [(1119, 782),(1182, 468),(674, 519),(1181, 163),(1418, 62)]
    for xo in xos:
        mouse.position = xo
        time.sleep(0.04)
        mouse.click(Button.left, 1)
        time.sleep(0.04)

def activate():
    time.sleep(1)

    #with keyboard.Listener(on_press=on_press_mouse) as listener:
    #    listener.join()

    with keyboard.Listener(on_press=on_press_start) as listener:
        listener.join() # wait for F11...

    with keyboard.Listener(on_press=on_press_loop) as listener:
        for _ in range(times):
            main()
            if not listener.running:
                break
            

if __name__ == '__main__':
    poll = activate()