from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController
from pynput import keyboard
import time
import threading
import sys

# Global variables to control the loop
running = True
mouse = MouseController()
keyboard = KeyboardController()

# Function to hold down the key 'w' for 20 seconds
def hold_w():
    start_time = time.time()
    while time.time() - start_time < 20 and running:
        keyboard.press('w')

# Function to hold down the key 's' for 20 seconds
def hold_s():
    start_time = time.time()
    while time.time() - start_time < 20 and running:
        keyboard.press('s')

# Function to hold down the keys 'w', 'a', 'ctrl' for 5 seconds
def hold_w_a_ctrl():
    start_time = time.time()
    while time.time() - start_time < 5 and running:
        keyboard.press('w')
        keyboard.press('a')
        keyboard.press(Key.ctrl)

# Function to end the process
def end_process():
    global running
    running = False

# Function to handle key press events
def on_press(key):
    if key != Key.w and key != Key.s and key != Key.a and key != Key.ctrl:
        end_process()
        return False

# Create and start the threads for each action
threads = [
    threading.Thread(target=hold_w),
    threading.Thread(target=hold_s),
    threading.Thread(target=hold_w_a_ctrl)
]

# Hold down the left click
mouse.press(Button.left)

# Start all threads
for thread in threads:
    thread.start()

# Start the key listener thread

listener = keyboard(on_press=on_press)
listener.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

# Release the left click and all held keys before exiting
mouse.release(Button.left)
keyboard.release('w')
keyboard.release('s')
keyboard.release('a')
keyboard.release(Key.ctrl)
listener.join()