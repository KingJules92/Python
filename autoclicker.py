import time
import pyautogui
import threading

# Getting Cursor-Position
cursor_position = pyautogui.position()

# Change the Countdown time (in minutes)
minutes = 1

def Countdown():
    global my_timer
    my_timer = 60*minutes
    for x in range(my_timer):
        my_timer -= 1
        time.sleep(1)

def Autoclick():
    while my_timer > 0:
        pyautogui.doubleClick(cursor_position)

# Starting Countdown 
thread_countdown = threading.Thread(target = Countdown)
thread_countdown.start()

# Starting multiple "clicking-threads" (short delay)
for i in range(30):
    i = threading.Thread(target = Autoclick)
    i.start()

