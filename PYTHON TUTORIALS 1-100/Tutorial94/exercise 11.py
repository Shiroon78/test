import time
import winsound
import tkinter as tk

root = tk.Tk()

def beep():
    winsound.Beep(600, 500)

def notify():
    root.after_idle(root.destroy)
    root.update()
    winsound.Beep(1000, 500)

while True:
    time.sleep(7200)
    notify()