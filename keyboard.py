import time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def add_with_keyboard():
    time.sleep(1)
    with keyboard.pressed(Key.shift):
        for _ in range(2):
            time.sleep(0.1)
            keyboard.tap(Key.tab)
            time.sleep(0.1)
            keyboard.tap(Key.tab)
        keyboard.tap(Key.enter)
    time.sleep(1)