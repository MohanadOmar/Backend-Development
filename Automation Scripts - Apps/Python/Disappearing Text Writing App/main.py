from tkinter import *
from datetime import datetime

live_words_tracking = []


def check(text, live_list):
    if text == live_list[-1]:
        print("test")
    else:
        print("shit")


def callback(sv):
    while True:
        now = datetime.now().strftime("%S")
        text = sv.get()
        live_words_tracking.append(text)
        later = datetime.now().strftime("%S")
        print(now)
        print(later)

win = Tk()
sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
e = Entry(win, textvariable=sv)
e.pack()



win.mainloop()