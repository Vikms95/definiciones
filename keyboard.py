import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def add_with_keyboard():
    time.sleep(0.25)
    with keyboard.pressed(Key.shift):
        for _ in range(4):
            time.sleep(0.1)
            keyboard.tap(Key.tab)
        keyboard.tap(Key.enter)
        time.sleep(0.1)
        keyboard.tap(Key.esc)
        time.sleep(0.1)