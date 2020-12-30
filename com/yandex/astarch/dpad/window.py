import pkgutil
import tkinter
from tkinter import *
from com.yandex.astarch.dpad.adb_commands import send_adb_keyevent


def send_adb_left():
    send_adb_keyevent(21)


def send_adb_up():
    send_adb_keyevent(19)


def send_adb_center():
    send_adb_keyevent(23)


def send_adb_right():
    send_adb_keyevent(22)


def send_adb_down():
    send_adb_keyevent(20)


window = Tk()
window.title("Dpad")

# Place buttons
btnLeft = Button(window, text="LEFT", command=send_adb_left)
btnUp = Button(window, text="UP", command=send_adb_up)
btnCenter = Button(window, text="CENTER", command=send_adb_center)
btnRight = Button(window, text="RIGHT", command=send_adb_right)
btnDown = Button(window, text="DOWN", command=send_adb_down)

btnLeft.grid(row=2, column=1)
btnUp.grid(row=1, column=2)
btnCenter.grid(row=2, column=2)
btnRight.grid(row=2, column=3)
btnDown.grid(row=3, column=2)

window.mainloop()
